---
title: 'Dependency Injection'
published: true
tags: DesignPattern
---

In software engineering, dependency injection is a design pattern in which an
object or function receives other objects or functions that it depends on. A
form of inversion of control, dependency injection aims to separate the
concerns of constructing objects and using them, leading to loosely coupled
programs.[1][2][3] The pattern ensures that an object or function which wants
to use a given service should not have to know how to construct those
services. Instead, the receiving 'client' (object or function) is provided
with its dependencies by external code (an 'injector'), which it is not aware
of.[4] Dependency injection helps by making implicit dependencies explicit and
helps solve the following problems:[5]

- How can a class be independent from the creation of the objects it depends on?
- How can an application, and the objects it uses support different configurations?
- How can the behavior of a piece of code be changed without editing it
  directly?

Fundamentally, dependency injection consists of passing parameters to a method.[6]

Because the client does not build or find the service itself, it typically
only needs to declare the interfaces of the services it uses, rather than
their concrete implementations. This makes it easier to change which services
are actually used at runtime, especially in statically-typed languages where
changing the underlying objects would otherwise require re-compiling the
source code.

An example of inversion of control without dependency injection is the
template method pattern, where polymorphism is achieved through
subclassing.[7] In contrast, dependency injection implements inversion of
control through composition, and is often similar to the strategy pattern. A
difference is that the strategy pattern is intended for dependencies that are
interchangeable throughout an object's lifetime, whereas with dependency
injection typically only a single instance of a dependency is used.[8]

## Roles

Dependency injection involves four roles: services, clients, interfaces and
injectors.

### Services and clients

A service is any class which contains useful functionality. In turn, a client is any class which uses services.

Any object can be a service or a client; the names relate only to the role the
objects play in an injection. The same object may even be both a client (it
uses injected services) and a service (it is injected into other objects).
Upon injection, the service is made part of the client's state, available for
use.[11]

### Interfaces

Clients should not know how their dependencies are implemented, only their names and API. A service which retrieves emails, for instance, may use the IMAP or POP3 protocols behind the scenes, but this detail is likely irrelevant to calling code that merely wants an email retrieved. By ignoring implementation details, clients do not need to change when their dependencies do.

### Injectors

The injector, sometimes also called an assembler, container, provider or
factory, introduces services to the client.

The role of injectors is to construct and connect complex object graphs, where
objects may be both clients and services. The injector itself may be many
objects working together, but must not be the client, as this would create a
circular dependency.

Because dependency injection separates how objects are constructed from how
they are used, it often diminishes the importance of the new keyword found in
most object-oriented languages. Because the framework handles creating
services, the programmer tends to only directly construct value objects which
represents entities in the program's domain (such as an Employee object in a
business app or an Order object in a shopping app).

### Analogy

As an analogy, cars can be thought of as services which perform the useful
work of transporting people from one place to another. Car engines can require
gas, diesel or electricity, but this detail is unimportant to the client—a
driver—who only cares if it can get them to their destination.

Cars present a uniform interface through their pedals, steering wheels and
other controls. As such, which engine they were 'injected' with on the factory
line ceases to matter and drivers can switch between any kind of car as
needed.

## Advantages and disadvantages

### Advantages

A basic benefit of dependency injection is decreased coupling between classes and their dependencies.[16][17]

By removing a client's knowledge of how its dependencies are implemented, programs become more reusable, testable and maintainable.[18]

This also results in increased flexibility: a client may act on anything that supports the intrinsic interface the client expects.[19]

More generally, dependency injection reduces boilerplate code, since all dependency creation is handled by a singular component.[18]

Finally, dependency injection allows concurrent development. Two developers
can independently develop classes that use each other, while only needing to
know the interface the classes will communicate through. Plugins are often
developed by third-parties that never even talk to developers of the original
product.

#### Testing

Many of dependency injection's benefits are particularly relevant to unit-testing.

For example, dependency injection can be used to externalize a system's
configuration details into configuration files, allowing the system to be
reconfigured without recompilation. Separate configurations can be written for
different situations that require different implementations of components.[21]

Similarly, because dependency injection does not require any change in code
behavior, it can be applied to legacy code as a refactoring. This makes
clients more independent and are easier to unit test in isolation, using stubs
or mock objects, that simulate other objects not under test.

This ease of testing is often the first benefit noticed when using dependency
injection.

### Disadvantages

Critics of dependency injection argue that it:

- Creates clients that demand configuration details, which can be onerous when obvious defaults are available.[20]
- Makes code difficult to trace because it separates behavior from construction.[20]
- Is typically implemented with reflection or dynamic programming, hindering IDE automation.[23]
- Typically requires more upfront development effort.[24]
- Encourages dependence on a framework.

## Types of dependency injection

There are three main ways in which a client can receive injected services:[28]

- Constructor injection, where dependencies are provided through a client's class constructor.
- Setter injection, where the client exposes a setter method which accepts the dependency.
- Interface injection, where the dependency's interface provides an injector
  method that will inject the dependency into any client passed to it.

In some frameworks, clients do not need to actively accept dependency
injection at all. In Java, for example, reflection can make private attributes
public when testing and inject services directly.

### Without dependency injection

In the following Java example, the `Client` class contains a `Service` member
variable initialized in the constructor. The client directly constructs and
controls which service it uses, creating a hard-coded dependency.

```java
public class Client {
    private Service service;

    Client() {
        // The dependency is hard-coded.
        this.service = new ExampleService();
    }
}
```

### Constructor injection

The most common form of dependency injection is for a class to request its
dependencies through its constructor. This ensures the client is always in a
valid state, since it cannot be instantiated without its necessary
dependencies.

```java
public class Client {
    private Service service;

    // The dependency is injected through a constructor.
    Client(Service service) {
        if (service == null) {
            throw new InvalidParameterException("service must not be null");
        }
        this.service = service;
    }
}
```

### Setter injection

By accepting dependencies through a setter method, rather than a constructor,
clients can allow injectors to manipulate their dependencies at any time. This
offers flexibility, but makes it difficult to ensure that all dependencies are
injected and valid before the client is used.

```java
public class Client {
    private Service service;

    // The dependency is injected through a setter method.
    public void setService(Service service) {
        if (service == null) {
            throw new InvalidParameterException("service must not be null");
        }
        this.service = service;
    }
}
```

### Interface injection

With interface injection, dependencies are completely ignorant of their clients, yet still send and receive references to new clients.

In this way, the dependencies become injectors. The key is that the injecting method is provided through an interface.

An assembler is still needed to introduce the client and its dependencies. The assembler takes a reference to the client, casts it to the setter interface that sets that dependency, and passes it to that dependency object which in turn passes a reference to itself back to the client.

For interface injection to have value, the dependency must do something in addition to simply passing back a reference to itself. This could be acting as a factory or sub-assembler to resolve other dependencies, thus abstracting some details from the main assembler. It could be reference-counting so that the dependency knows how many clients are using it. If the dependency maintains a collection of clients, it could later inject them all with a different instance of itself.

```java
public interface ServiceSetter {
    public void setService(Service service);
}

public class Client implements ServiceSetter {
    private Service service;

    @Override
    public void setService(Service service) {
        if (service == null) {
            throw new InvalidParameterException("service must not be null");
        }
        this.service = service;
    }
}

public class ServiceInjector {
	private Set<ServiceSetter> clients;

	public void inject(ServiceSetter client) {
		this.clients.add(client);
		client.setService(new ExampleService());
	}

	public void switch() {
		for (Client client : this.clients) {
			client.setService(new AnotherExampleService());
		}
	}
}

public class ExampleService implements Service {}

public class AnotherExampleService implements Service {}
```

## Reference

- [https://en.wikipedia.org/wiki/Dependency_injection](https://en.wikipedia.org/wiki/Dependency_injection)