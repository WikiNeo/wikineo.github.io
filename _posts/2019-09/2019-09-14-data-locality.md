---
title:  "Game Programming Patterns - Optimization Patterns - Data Locality"
published: true
tags: DesignPattern
---

## Intent

Accelerate memory access by arranging data to rake advantage of CPU caching.

## CPU Cache

Modern computers have little chunk of memory right inside the chip. The little chunk of
memory is called cache (in particular, the chunk on the chip is the *L1 cache*). Whenever
your chip needs a byte of data from RAM, it automatically grabs a while chunk of
contiguous memory - usually around 64 to 128 bytes - and put it in the cache.

If the next byte of data you need happens to be in that chunk, the CPU reads it straight
from the cache, which is much faster than hitting RAM. Successfully finding a piece of
data in the cache is called a *cache hit*. If it can't find it in there and has to go to
main memory, that's a *cache miss*.

## Data is Performance

Because of caching, the way you organize data directly impacts performance. The goal then
is to *organize your data structures so that the things you are processing are next to
each other in memory*.

## The Pattern

Modern CPUs have **caches to speed up memory access**. These can access memory **adjacent
to recently accessed memory much quicker**. Take advantage of that to improve performance
by **increasing data locality** -- keeping data in **contiguous memory in the order that
you process it**.

## Keep in Mind

In C++, using interfaces implies accessing objects through pointer or references. But
going through a pointer means hopping across memory which leads to the cache misses this
pattern works to avoid.

In order to please this pattern, you will have to sacrifice some of your precious
abstractions. The more you design your program around data locality, the more you will
have to give up inheritance, interfaces, and the benefits those tools can provide.

## Sample Code

### Contiguous Arrays

```cpp
class GameEntity
{
public:
  GameEntity(AIComponent* ai,
             PhysicsComponent* physics,
             RenderComponent* render)
  : ai_(ai), physics_(physics), render_(render)
  {}

  AIComponent* ai() { return ai_; }
  PhysicsComponent* physics() { return physics_; }
  RenderComponent* render() { return render_; }

private:
  AIComponent* ai_;
  PhysicsComponent* physics_;
  RenderComponent* render_;
};
```

Update methods

```cpp
class AIComponent
{
public:
  void update() { /* Work with and modify state... */ }

private:
  // Goals, mood, etc. ...
};

class PhysicsComponent
{
public:
  void update() { /* Work with and modify state... */ }

private:
  // Rigid body, velocity, mass, etc. ...
};

class RenderComponent
{
public:
  void render() { /* Work with and modify state... */ }

private:
  // Mesh, textures, shaders, etc. ...
};
```

To update

```cpp
while (!gameOver)
{
  // Process AI.
  for (int i = 0; i < numEntities; i++)
  {
    entities[i]->ai()->update();
  }

  // Update physics.
  for (int i = 0; i < numEntities; i++)
  {
    entities[i]->physics()->update();
  }

  // Draw to screen.
  for (int i = 0; i < numEntities; i++)
  {
    entities[i]->render()->render();
  }

  // Other game loop machinery for timing...
}
```

Change 1

```cpp
AIComponent* aiComponents = new AIComponent[MAX_ENTITIES];
PhysicsComponent* physicsComponents = new PhysicsComponent[MAX_ENTITIES];
RenderComponent* renderComponents = new RenderComponent[MAX_ENTITIES];

while (!gameOver)
{
  // Process AI.
  for (int i = 0; i < numEntities; i++)
  {
    aiComponents[i].update();
  }

  // Update physics.
  for (int i = 0; i < numEntities; i++)
  {
    physicsComponents[i].update();
  }

  // Draw to screen.
  for (int i = 0; i < numEntities; i++)
  {
    renderComponents[i].render();
  }

  // Other game loop machinery for timing...
}
```

### Packed Data

Manager class

```cpp
class Particle
{
public:
  void update() { /* Gravity, etc. ... */ }
  // Position, velocity, etc. ...
};

class ParticleSystem
{
public:
  ParticleSystem()
  : numParticles_(0)
  {}

  void update();
private:
  static const int MAX_PARTICLES = 100000;

  int numParticles_;
  Particle particles_[MAX_PARTICLES];
};
```

Update

```cpp
void ParticleSystem::update()
{
  for (int i = 0; i < numParticles_; i++)
  {
    particles_[i].update();
  }
}
```

Only update active ones

```cpp
for (int i = 0; i < numParticles_; i++)
{
  if (particles_[i].isActive())
  {
    particles_[i].update();
  }
}
```

#### Branch Prediction

Doing `if` check for every particle can cause a *branch misprediction* and *pipeline
stall*. In modern CPUs, a single "instruction" actually takes several clock cycles. To
keep the CPU busy, instructions are *pipelined* so that the subsequent instructions start
processing before first one finishes.

To do that, the CPU has to guess which instructions it will be executing next. In straight
line code, that's easy, but with control flow, it's harder.

The chip does *branch prediction* - it sees which branches your code previously took and
guesses it will do that again. But when the loop is constantly toggling between particles
that are and aren't active, that prediction fails.

When it does, the CPU has to ditch the instructions it had started speculatively
processing (a *pipeline flush*) and start over. The performance impact of this varies
widely by machine, but this is why you sometimes see developers avoid flow control in hot
code.

Instead of *checking* the active flag, we'll *sort* by it. We'll keep all of the active
particles in the front of the list.

```cpp
for (int i = 0; i < numActive_; i++)
{
  particles[i].update();
}
```

To keep the array sorted

```cpp
void ParticleSystem::activateParticle(int index)
{
  // Shouldn't already be active!
  assert(index >= numActive_);

  // Swap it with the first inactive particle
  // right after the active ones.
  Particle temp = particles_[numActive_];
  particles_[numActive_] = particles_[index];
  particles_[index] = temp;

  // Now there's one more.
  numActive_++;
}

void ParticleSystem::deactivateParticle(int index)
{
  // Shouldn't already be inactive!
  assert(index < numActive_);

  // There's one fewer.
  numActive_--;

  // Swap it with the last active particle
  // right before the inactive ones.
  Particle temp = particles_[numActive_];
  particles_[numActive_] = particles_[index];
  particles_[index] = temp;
}
```

### Hot/Cold Splitting

This is an AI component for some game entity. It has some state in it -- the animation
it's currently playing, a goal position its heading towards, energy level, etc. -- stuff
it checks and tweaks every single frame.

```cpp
class AIComponent
{
public:
  void update() { /* ... */ }

private:
  Animation* animation_;
  double energy_;
  Vector goalPos_;
};
```

But it also has some state for rarer eventualities.

```cpp
class AIComponent
{
public:
  void update() { /* ... */ }

private:
  // Previous fields...
  LootType drop_;
  int minDrops_;
  int maxDrops_;
  double chanceOfDrop_;
};
```

Assuming we followed the earlier patterns, when we update these AI components, we walk
through a nice packed, contiguous array of data. But that data includes all of the drop
information. That makes each component bigger, which reduces the number of components we
can fit in a cache line. We get more cache misses because the total memory walk over is
larger. The loot data gets pulled into the cache for every component in every frame, even
though we aren't even touching it.

The solution for this is called "hot/cold splitting". The idea is to break our data
structure into two separate pieces. The first holds the "hot" data, the state we need to
touch every frame. The other piece is the "cold" data, everything else that gets used less
frequently.

```cpp
class AIComponent
{
public:
  // Methods...
private:
  Animation* animation_;
  double energy_;
  Vector goalPos_;

  LootDrop* loot_;
};

class LootDrop
{
  friend class AIComponent;
  LootType drop_;
  int minDrops_;
  int maxDrops_;
  dou
```

We could conceivably ditch the pointer too by having parallel arrays for the hot and cold
components. Then we can find the cold AI data for a component since both pieces will be at
the same index in their respective arrays.

References: [https://gameprogrammingpatterns.com/data-locality.html](https://gameprogrammingpatterns.com/data-locality.html)
