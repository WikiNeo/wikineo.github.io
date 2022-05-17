---
title: 'Polymorphic Associations'
published: true
tags: Ruby
---

With polymorphic associations, a model can belong to more than one other
model, on a single association. For example, you might have a picture model
that belongs to either an employee model or a product model.

```ruby
class Picture < ApplicationRecord
  belongs_to :imageable, polymorphic: true
end

class Employee < ApplicationRecord
  has_many :pictures, as: :imageable
end

class Product < ApplicationRecord
  has_many :pictures, as: :imageable
end
```

You can think of a polymorphic `belongs_to` declaration as setting up an
interface that any other model can use. From an instance of the `Employee`
model, you can retrieve a collection of pictures: `@employee.pictures`.

Similarly, you can retrieve `@product.pictures`.

If you have an instance of the `Picture` model, you can get to its parent via
`@picture.imageable`. To make this work, you need to declare both a foreign
key column and a type column in the model that declares the polymorphic
interface.

```ruby
class CreatePictures < ActiveRecord::Migration[7.0]
  def change
    create_table :pictures do |t|
      t.string  :name
      t.bigint  :imageable_id
      t.string  :imageable_type
      t.timestamps
    end

    add_index :pictures, [:imageable_type, :imageable_id]
  end
end

```

The migration can be simplified by using `t.references` form

```ruby
class CreatePictures < ActiveRecord::Migration[7.0]
  def change
    create_table :pictures do |t|
      t.string :name
      t.references :imageable, polymorphic: true
      t.timestamps
    end
  end
end
```

## Reference

- [https://guides.rubyonrails.org/association_basics.html#polymorphic-associations](https://guides.rubyonrails.org/association_basics.html#polymorphic-associations)