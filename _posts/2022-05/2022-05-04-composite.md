---
title: '[Structural] Composite'
published: true
tags: DesignPattern
---

## Real world example

Every organization is composed of employees. Each of the employees has the
same features i.e. has a salary, has some responsibilities, may or may not
report to someone, may or may not have some subordinates etc.

## In plain words

Composite pattern lets clients treat the individual objects in a uniform
manner.

## Wikipedia says

In software engineering, the composite pattern is a partitioning design
pattern. The composite pattern describes that a group of objects is to be
treated in the same way as a single instance of an object. The intent of a
composite is to "compose" objects into tree structures to represent part-whole
hierarchies. Implementing the composite pattern lets clients treat individual
objects and compositions uniformly.

## Programmatic Example

Taking our employees example from above. Here we have different employee types

```typescript

interface Employee {
    getName(): string;
    setSalary(salary: number);
    getSalary(): number;
    getRoles(): [];
}

class Developer implements Employee {
    protected salary: number;
    protected name: string;
    protected roles;

    constructor(name: string, salary: number) {
        this.name = name;
        this.salary = salary;
    }

    getName(): string {
        return this.name;
    }

    getSalary(): number {
        return this.salary;
    }

    getRoles(): [] {
        return this.roles;
    }

    setSalary(salary: number) {
        this.salary = salary;
    }
}

class Designer implements Employee {
    protected salary: number;
    protected name: string;
    protected roles;

    constructor(name: string, salary: number) {
        this.name = name;
        this.salary = salary;
    }

    getName(): string {
        return this.name;
    }

    getSalary(): number {
        return this.salary;
    }

    getRoles(): [] {
        return this.roles;
    }

    setSalary(salary: number) {
        this.salary = salary;
    }
}
```

Then we have an organization which consists of several different types of employees

```typescript
class Organization {
    protected employees: Employee[];

    addEmployee(employee: Employee){
        this.employees.push(employee);
    }

    getNetSalaries(): number {
        return this.employees.reduce((salaries: number, employee: Employee) => {
            return salaries + employee.getSalary()
        }, 0)
    }
}
```

And then it can be used as

```typescript
const john = new Developer('John Doe', 12000)
const jane = new Developer('Jane Doe', 15000)

const organization = new Organization()
organization.addEmployee(john)
organization.addEmployee(jane)
organization.getNetSalaries();
```

## References

- [https://github.com/kamranahmedse/design-patterns-for-humans](https://github.com/kamranahmedse/design-patterns-for-humans)
- [https://github.com/torokmark/design_patterns_in_typescript](https://github.com/torokmark/design_patterns_in_typescript)
- [https://refactoring.guru/design-patterns](https://refactoring.guru/design-patterns)