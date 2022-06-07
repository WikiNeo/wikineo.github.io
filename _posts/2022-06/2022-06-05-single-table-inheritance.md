---
title: '[Rails] Single Table Inheritance'
published: true
tags: Ruby
---

Sometimes, you may want to share fields and behavior between different models.
Let's say we have `Car`, `Motorcycle`, and `Bicycle` models. We will want to share
the `color` and `price` fields and some methods for all of them, but having
some specific behavior for each, and separated controllers too.

First, let's generate the base `Vehicle` model:

```bash
bin/rails generate model vehicle type:string color:string price:decimal{10.2}
```

Did you note we are adding a "type" field? Since all models will be saved in a single database table, Rails will save in this column the name of the model that is being saved. In our example, this can be "Car", "Motorcycle" or "Bicycle." STI won't work without a "type" field in the table.

Next, we will generate the Car model that inherits from Vehicle. For this, we can use the `--parent=PARENT` option, which will generate a model that inherits from the specified parent and without equivalent migration (since the table already exists).

For example, to generate the Car model:

```bash
bin/rails generate model car --parent=Vehicle
```

The generated model will look like this:

```ruby
class Car < Vehicle
end
```

This means that all behavior added to Vehicle is available for Car too, as associations, public methods, etc.

Creating a car will save it in the `vehicles` table with "Car" as the `type`
field:

```sql
INSERT INTO "vehicles" ("type", "color", "price") VALUES ('Car', 'Red', 10000)
```

Querying car records will search only for vehicles that are cars:

```ruby
Car.all
```

will run a query like:

```sql
SELECT "vehicles".* FROM "vehicles" WHERE "vehicles"."type" IN ('Car')
```

## Reference

- [https://guides.rubyonrails.org/association_basics.html#single-table-inheritance-sti](https://guides.rubyonrails.org/association_basics.html#single-table-inheritance-sti)