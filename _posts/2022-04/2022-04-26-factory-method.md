---
title: '[Creational] Factory Method'
published: true
tags: DesignPattern
---

## Real world example

Consider the case of a hiring manager. It is impossible for one person to
interview for each of the positions. Based on the job opening, she has to
decide and delegate the interview steps to different people.

## In plain words

It provides a way to delegate the instantiation logic to child classes.

## Wikipedia says

In class-based programming, the factory method pattern is a creational pattern
that uses factory methods to deal with the problem of creating objects without
having to specify the exact class of the object that will be created. This is
done by creating objects by calling a factory method—either specified in an
interface and implemented by child classes, or implemented in a base class and
optionally overridden by derived classes—rather than by calling a constructor.

## Programmatic Example

Taking our hiring manager example above. First of all we have an interviewer
interface and some implementations for it

```typescript
interface Interviewer {
    askQuestions();
}

class Developer implements Interviewer {
    askQuestions() {
        console.log('Asking about design patterns');
    }
}

class CommunityExecutive implements Interviewer {
    askQuestions() {
        console.log('Asking about community building');
    }
}
```

Now let us create our `HiringManager`

```typescript
abstract class HiringManager {
    // factory method
    protected abstract makeInterviewer(): Interviewer;

    public takeInterview(){
        let interviewer: Interviewer = this.makeInterviewer();
        interviewer.askQuestions();
    }
}
```

Now any child can extend it and provide the required interviewer


```typescript
class DevelopmentManager extends HiringManager {
    protected makeInterviewer(): Interviewer {
        return new Developer();
    }
}

class MarketingManager extends HiringManager{
    protected makeInterviewer(): Interviewer {
        return new CommunityExecutive();
    }
}
```

and then it can be used as

```typescript
let devManager = new DevelopmentManager();
devManager.takeInterview();

let marketingManager = new MarketingManager();
marketingManager.takeInterview();
```

## When to use?

Useful when there is some generic processing in a class but the required
sub-class is dynamically decided at runtime. Or putting it in other words,
when the client doesn't know what exact sub-class it might need.

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)