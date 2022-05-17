---
title: 'Self Joins'
published: true
tags: Ruby
---

In designing a data model, you will sometimes find a model that should have a
relation to itself. For example, you may want to store all employees in a
single database model, but be able to trace relationships such as between
manager and subordinates. This situation can be modeled with self-joining
associations

```ruby
class Employee < ApplicationRecord
  has_many :subordinates, class_name: "Employee",
                          foreign_key: "manager_id"

  belongs_to :manager, class_name: "Employee", optional: true
end
```

With this setup, you can retrieve `@employee.subordinates` and
`@employee.manager`.

In your migrations/schema, you will add a references column to the model
itself.

```ruby
class CreateEmployees < ActiveRecord::Migration[7.0]
  def change
    create_table :employees do |t|
      t.references :manager, foreign_key: { to_table: :employees }
      t.timestamps
    end
  end
end
```

## Reference

- [https://guides.rubyonrails.org/association_basics.html#self-joins](https://guides.rubyonrails.org/association_basics.html#self-joins)