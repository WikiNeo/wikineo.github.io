---
title: "Creational-Abstract-Factory"
published: true
---

Abstract factory pattern has creational purpose and provides an interface for
creating families of related or dependent objects without specifying their
concrete classes. Pattern applies to object and deal with object relationships,
which are more dynamic contrast to Factory Method, Abstract Factory pattern
produces family of types that are related, ie. it has more than one method types
it produces.

## Real world example

Extending our door example from Simple Factory. Based on your needs you might
get a wooden door from a wooden door shop, iron door from an iron shop or a PVC
door from the relevant ship. Plus you might need a guy with different kind of
specialities to fit the door, for example a carpenter for wooden door, welder
for iron door etc. As you can see there is a dependency between the doors now,
wooden door needs carpenter, iron door needs a welder etc.

## In plain words

A factory of factories; a factory that groups the individual but
related/dependent factories together without specifying their concrete classes.

## Wikipedia says

The abstract factory pattern provides a way to encapsulate a group of individual
factories that have a common theme without specifying their concrete classes

## PHP Example

Translating the door example above. First of all we have our `Door` interface
and some implementation for it

```php
interface Door
{
    public function getDescription();
}

class WoodenDoor implements Door
{
    public function getDescription()
    {
        echo 'I am a wooden door';
    }
}

class IronDoor implements Door
{
    public function getDescription()
    {
        echo 'I am an iron door';
    }
}
```

Then we have some fitting experts for each door type

```php
interface DoorFittingExpert
{
    public function getDescription();
}

class Welder implements DoorFittingExpert
{
    public function getDescription()
    {
        echo 'I can only fit iron doors';
    }
}

class Carpenter implements DoorFittingExpert
{
    public function getDescription()
    {
        echo 'I can only fit wooden doors';
    }
}
```

Now we have our abstract factory that would let us make family of related
objects i.e. wooden door factory would create a wooden door and wooden door
fitting expert and iron door factory would create an iron door and iron door
fitting expert.

```php
interface DoorFactory
{
    public function makeDoor(): Door;
    public function makeFittingExpert(): DoorFittingExpert;
}

// Wooden factory to return carpenter and wooden door
class WoodenDoorFactory implements DoorFactory
{
    public function makeDoor(): Door
    {
        return new WoodenDoor();
    }

    public function makeFittingExpert(): DoorFittingExpert
    {
        return new Carpenter();
    }
}

// Iron door factory to get iron door and the relevant fitting expert
class IronDoorFactory implements DoorFactory
{
    public function makeDoor(): Door
    {
        return new IronDoor();
    }

    public function makeFittingExpert(): DoorFittingExpert
    {
        return new Welder();
    }
}
```

And then it can be used as

```php
$woodenFactory = new WoodenDoorFactory();

$door = $woodenFactory->makeDoor();
$expert = $woodenFactory->makeFittingExpert();

$door->getDescription();  // Output: I am a wooden door
$expert->getDescription(); // Output: I can only fit wooden doors

// Same for Iron Factory
$ironFactory = new IronDoorFactory();

$door = $ironFactory->makeDoor();
$expert = $ironFactory->makeFittingExpert();

$door->getDescription();  // Output: I am an iron door
$expert->getDescription(); // Output: I can only fit iron doors
```

As you can see the wooden door factory has encapsulated the `carpenter` and the
`wooden door` also iron door factory has encapsulated the `iron door` and
`welder`. And thus it had helped us make sure that for each of the created door,
we do not get a wrong fitting expert.

## C++ Example

```cpp
#include <iostream>

/*
 * Product A
 * products implement the same interface so that the classes can refer
 * to the interface not the concrete product
 */
class ProductA
{
public:
  virtual ~ProductA() {}
  
  virtual const char* getName() = 0;
  // ...
};

/*
 * ConcreteProductAX and ConcreteProductAY
 * define objects to be created by concrete factory
 */
class ConcreteProductAX : public ProductA
{
public:
  ~ConcreteProductAX() {}
  
  const char* getName()
  {
    return "A-X";
  }
  // ...
};

class ConcreteProductAY : public ProductA
{
public:
  ~ConcreteProductAY() {}
  
  const char* getName()
  {
    return "A-Y";
  }
  // ...
};

/*
 * Product B
 * same as Product A, Product B declares interface for concrete products
 * where each can produce an entire set of products
 */
class ProductB
{
public:
  virtual ~ProductB() {}
  
  virtual const char* getName() = 0;
  // ...
};

/*
 * ConcreteProductBX and ConcreteProductBY
 * same as previous concrete product classes
 */
class ConcreteProductBX : public ProductB
{
public:
  ~ConcreteProductBX() {}
  
  const char* getName()
  {
    return "B-X";
  }
  // ...
};

class ConcreteProductBY : public ProductB
{
public:
  ~ConcreteProductBY() {}
  
  const char* getName()
  {
    return "B-Y";
  }
  // ...
};

/*
 * Abstract Factory
 * provides an abstract interface for creating a family of products
 */
class AbstractFactory
{
public:
  virtual ~AbstractFactory() {}
  
  virtual ProductA *createProductA() = 0;
  virtual ProductB *createProductB() = 0;
};

/*
 * Concrete Factory X and Y
 * each concrete factory create a family of products and client uses
 * one of these factories so it never has to instantiate a product object
 */
class ConcreteFactoryX : public AbstractFactory
{
public:
  ~ConcreteFactoryX() {}
  
  ProductA *createProductA()
  {
    return new ConcreteProductAX();
  }
  ProductB *createProductB()
  {
    return new ConcreteProductBX();
  }
  // ...
};

class ConcreteFactoryY : public AbstractFactory
{
public:
  ~ConcreteFactoryY() {}

  ProductA *createProductA()
  {
    return new ConcreteProductAY();
  }
  ProductB *createProductB()
  {
    return new ConcreteProductBY();
  }
  // ...
};


int main()
{
  ConcreteFactoryX *factoryX = new ConcreteFactoryX();
  ConcreteFactoryY *factoryY = new ConcreteFactoryY();

  ProductA *p1 = factoryX->createProductA();
  std::cout << "Product: " << p1->getName() << std::endl;
  
  ProductA *p2 = factoryY->createProductA();
  std::cout << "Product: " << p2->getName() << std::endl;
  
  delete p1;
  delete p2;
  
  delete factoryX;
  delete factoryY;
  
  return 0;
}
```

## When to use?

- When there are interrelated dependencies with not-that-simple creation logic involved.
- A system should be independent of how its products are created, composed, and
  represented
- A system should be configured with one of multiple families of products
- A family of related product objects is designed to be used together
- You want to provide a class library of products, and you want to reveal just
  their interfaces, not their implementations.

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans#-abstract-factory](https://github.com/kamranahmedse/design-patterns-for-humans#-abstract-factory)
- [https://github.com/JakubVojvoda/design-patterns-cpp/tree/master/abstract-factory](https://github.com/JakubVojvoda/design-patterns-cpp/tree/master/abstract-factory)