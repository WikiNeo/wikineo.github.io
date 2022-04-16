---
title: 'SOLID Principles Using TypeScript'
published: true
tags: DesignPattern
---

## What is SOLID?

SOLID is an acronym for five software design principles introduced by Robert
C. Martin in the 2000s, that aims to help us structure our code in order to:

- Tolerate change.
- Ease code understanding.
- Write components that can be used in many software systems.

SOLID stands for:

- **S**: Single Responsibility Principle
- **O**: Open-Closed Principle
- **L**: Liskov Substitution Principle
- **I**: Interface Segregation Principle
- **D**: Dependency Inversion Principle

## Single Responsibility Principle

*A class should have one, and only one, reason to change*

If our classes assume **multiple responsibilities**, they will be **highly
coupled thus making them more difficult to maintain**.

### What's a reason to change?

Uncle Bob stats that this principle is about people. This means that when you
write a software module, and changes are required on that module, those
changes can only originate from a single person or a tightly group of people
representing a single narrowly defined business function.

Another definition for this principle is:

*Gather together those things that change for the same reason, and separate
those things that changes for different reasons.*

This can also be considered the definition of **[Separation of
Concerns](https://en.wikipedia.org/wiki/Separation_of_concerns)**

The following piece of code shows a violation of SRP in which the `Book` class
is both a representation of an entity and also implements the persistence of
such entity

```typescript
class Book {
  constructor(private _author: string, private _title: string) {}

  get author(): string {
    return this._author;
  }

  get title(): string {
    return this._title;
  }

  save(): void {
    // Save book in the database.
  }
}
```

By applying Separation of Concerns, we split the `Book` class to have
representation of the book in a class and the persistence logic in another
one:

```typescript
class Book {
  constructor(private _author: string, private _title: string) {}

  get author(): string {
    return this._author;
  }

  get title(): string {
    return this._title;
  }
}

interface RepositoryInterface<T> {
  save(entity: T): void;
}

class BookRepository<T extends Book> implements RepositoryInterface<T> {
  save(book: Book): void {
    // Save book in the database
  }
}
```

## Open-Closed Principle

*Software entities should be open for extension, but closed for modification.*

This principle states that software **entities muse be extensible without
having to modify the existing code**. In order to achieve this, we need to
make abstraction. By doing this, we'll be able to extend the behavior of a
class without changing a single line of code in it.

The following snippet shows an `AreaCalculator` class that accumulates the
areas of different shapes, that will have to be modified every time we add a
new Shape:

```typescript
class Rectangle {
  constructor(private _width: number, private _height: number) {}

  get height(): number {
    return this._height; 
  }

  get width(): number {
    return this._width;
  }
}

class Square {
  constructor(private _height: number) {}

  get height(): number {
    return this._height; 
  }
}

class AreaCalculator {
  private shapes: any[];

  constructor(shapes: any[]) {
    this.shapes = shapes;
  }

  public sum() {
    return this.shapes.reduce((acc, shape) => {
      if (shape instanceof Square) {
        acc += Math.pow(shape.height, 2);
      }
      if (shape instanceof Rectangle) {
        acc += shape.height * shape.width;
      }
      return acc;
    }, 0);
  }
}
```

A solution for this would be to implement a `Shape` interface in every shape.
This way we implement a simple method to calculate the sum of the areas. Every
time we need to add a new shape, it will implement the `Shape` interface and
we won't have to make any changes on the calculator.

```typescript
  area() : number;
}

class Rectangle implements Shape {
  constructor(private _width: number, private _height: number) {}

  public area() : number {
    return this._height * this._width;
  }
}

export class Square implements Shape {
  constructor(private _height: number) {}

  public area() : number {
    return Math.pow(this._height, 2);
  }
}

class AreaCalculator {
  private shapes: Shape[];

  constructor(shapes: Shape[]) {
    this.shapes = shapes;
  }

  public sum() : number {
    return this.shapes
      .reduce((acc, shape) => acc += shape.area(), 0);
  }
}
```

## Liskov Substitution Principle

*Let q(x) be a property provable about object of x of type T. Then q(y) should
be provable for object y of the S where S is a subtype of T.*

This principle states that objects must be **replaceable by instances of their
subtypes without altering the correct functioning of the system**.

A classic example of a violation of this principle is the **[Rectangle-Square
problem](http://www.blackwasp.co.uk/SquareRectangle.aspx)**. The `Square`
class extends the `Rectangle` class and assumes that the width and height are
equal. When calculating the area of a square, we'd get a wrong value.

```typescript
class Rectangle {
  constructor(private _width: number, private _height: number) {}

  public area() : number {
    return this._height * this._width;
  }
}

class Square extends Rectangle {}
```

To solve it, implements a `Shape` interface that will have to be implemented
by every new shape added.

```typescript
interface Shape {
  area() : number;
}

class Rectangle implements Shape {
  constructor(private _width: number, private _height: number) {}

  public area() : number {
    return this._height * this._width;
  }
}

class Square implements Shape {
  constructor(private _height: number) {}

  public area() : number {
    return Math.pow(this._height, 2);
  }
}
```

## Interface Segregation Principle

*Many client-specific interfaces are better than one general-purpose
interface.*

This principle stats that classes **should never implement interfaces that
they don't need to usd.** If they do, we'll end up having **not implemented
methods** in our classes. This can be solved **creating specific interfaces
instead of general-purpose interfaces**.

```typescript
interface VehicleInterface {
  drive(): string;
  fly(): string;
}

class FutureCar implements VehicleInterface {
  public drive() : string {
    return 'Driving Car.';
  }

  public fly() : string {
    return 'Flying Car.';
  }
}

class Car implements VehicleInterface {
  public drive() : string {
    return 'Driving Car.';
  }

  public fly() : string {
    throw new Error('Not implemented method.');
  }
}

class Airplane implements VehicleInterface {
  public drive() : string {
    throw new Error('Not implemented method.');
  }
  
  public fly() : string {
    return 'Flying Airplane.';
  }
}
```

The solution is splitting `VehicleInterface` into specific interfaces

```typescript
interface CarInterface {
  drive() : string;
}

interface AirplaneInterface {
  fly() : string;
}

class FutureCar implements CarInterface, AirplaneInterface {
  public drive() {
      return 'Driving Car.';
  }

  public fly() {
      return 'Flying Car.'
  }
}

class Car implements CarInterface {
  public drive() {
      return 'Driving Car.';
  }
}

class Airplane implements AirplaneInterface {
  public fly() {
      return 'Flying Airplane.';
  }
}
```

## Dependency Inversion Principle

*Entities must depend on abstraction not on concretions. It stats that the
high level module must not depend on the low level module, but they should
depend on the abstractions.*

This principle states that a class should not depend on another class, but
instead on an abstraction of that class. It allows loosing-coupling and more
reusability.

```typescript
class MemoryStorage {
  private storage: any[];

  constructor() {
    this.storage = [];
  }

  public insert(record: any): void {
    this.storage.push(record);
  }
}

class PostService {
  private db = new MemoryStorage();

  createPost(title: string) {
    this.db.insert(title);
  }
}
```

Here, the `PostService` class depends on the `MemoryStorage` class to save new
posts. What happens if we need to change the storage used to save posts? We'll
have to modify the `PostService` class to change the type of the `db`
property, thus violating the `Open-Closed Principle`.

If `PostService` relies on an interface instead of a class, we wouldn't have
to make changes on it.

```typescript
interface DatabaseStorage {
  insert(record: any): void;
}

class MemoryStorage implements DatabaseStorage {
  private storage: any[];

  constructor() {
    this.storage = [];
  }

  public insert(record: any): void {
    this.storage.push(record);
  }
}

class PostService {
  private db: DatabaseStorage;

  constructor(db: DatabaseStorage) {
    this.db = db;
  }

  createPost(title: string) {
    this.db.insert(title);
  }
}
```

## Reference

- [https://medium.com/@alejandromarr/solid-principles-using-typescript-c475031efcd3](https://medium.com/@alejandromarr/solid-principles-using-typescript-c475031efcd3)