---
title: 'Locking Records for Update'
published: true
tags: Ruby
---

Locking is helpful for preventing race conditions when updating records in the database and ensuring atomic updates.

## Optimistic Locking

Optimistic locking allows multiple users to access the same record for edits,
and assumes a minimum of conflicts with the data. It does this by checking
whether another process has made changes to a record since it was opened. An
`ActiveRecord::StaleObjectError` exception is thrown if that has occurred and
the update is ignored.

### Optimistic locking column

In order to use optimistic locking, the table needs to have a column called
`lock_version` of type integer. Each time the record is updated, Active Record
increments the `lock_version` column. If an update request is made with a lower
value in the lock_version field than is currently in the `lock_version` column
in the database, the update request will fail with an
`ActiveRecord::StaleObjectError`.

For example:

```ruby
c1 = Customer.find(1)
c2 = Customer.find(1)

c1.first_name = "Sandra"
c1.save

c2.first_name = "Michael"
c2.save # Raises an ActiveRecord::StaleObjectError
```

You're then responsible for dealing with the conflict by rescuing the exception and either rolling back, merging, or otherwise apply the business logic needed to resolve the conflict.

This behavior can be turned off by setting `ActiveRecord::Base.lock_optimistically = false`.

To override the name of the `lock_version` column, `ActiveRecord::Base`
provides a class attribute called `locking_column`:

```ruby
class Customer < ApplicationRecord
  self.locking_column = :lock_customer_column
end
```

## Pessimistic Locking

Pessimistic locking uses a locking mechanism provided by the underlying
database. Using `lock` when building a relation obtains an exclusive lock on the
selected rows. Relations using `lock` are usually wrapped inside a transaction
for preventing deadlock conditions.

For example

```ruby
Book.transaction do
  book = Book.lock.first
  book.title = 'Algorithms, second edition'
  book.save!
end
```

The above session produces the following SQL for a MySQL backend:

```sql
SQL (0.2ms)   BEGIN
Book Load (0.3ms)   SELECT * FROM `books` LIMIT 1 FOR UPDATE
Book Update (0.4ms)   UPDATE `books` SET `updated_at` = '2009-02-07 18:05:56', `title` = 'Algorithms, second edition' WHERE `id` = 1
SQL (0.8ms)   COMMIT
```

You can also pass raw SQL to the `lock` method for allowing different types of
locks. For example, MySQL has an expression called `LOCK IN SHARE MODE` where
you can lock a record but still allow other queries to read it. To specify
this expression just pass it in as the lock option:

```ruby
Book.transaction do
  book = Book.lock("LOCK IN SHARE MODE").find(1)
  book.increment!(:views)
end
```

If you already have an instance of your model, you can start a transaction and acquire the lock in one go using the following code:

```ruby
book = Book.first
book.with_lock do
  # This block is called within a transaction,
  # book is already locked.
  book.increment!(:views)
end
```

## Reference

- [https://guides.rubyonrails.org/active_record_querying.html#locking-records-for-update](https://guides.rubyonrails.org/active_record_querying.html#locking-records-for-update)