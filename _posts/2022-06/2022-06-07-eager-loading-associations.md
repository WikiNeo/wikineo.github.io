---
title: '[Rails] Eager Loading Associations'
published: true
tags: Ruby
---

Eager loadings the mechanism for loading the associated records of the objects
returned by `Model.find` using as few queries as possible.

## N + 1 queries problem

Consider the following code, which finds 10 books and prints their authors' last_name:

```ruby
books = Book.limit(10)

books.each do |book|
  puts book.author.last_name
end
```

This code looks fine at the first sight. But the problem lies within the total
number of queries executed. The above code executes 1 (to find 10 books) + 10
(one per each book to load the author) = 11 queries in total.

## Solution to N + 1 queries problem

Active Record lets you specify in advance all the associations that are going
to be loaded.

## includes

With `includes`, Active Record ensures that all of the specified associations are loaded using the minimum possible number of queries.

Revisiting the above case using the `includes` method, we could rewrite `Book.limit(10)` to eager load authors:

```ruby
books = Book.includes(:author).limit(10)

books.each do |book|
  puts book.author.last_name
end
```

The above code will execute just **2** queries, as opposed to the **11** queries from the original case:

```sql
SELECT `books`.* FROM `books` LIMIT 10
SELECT `authors`.* FROM `authors`
  WHERE `authors`.`book_id` IN (1,2,3,4,5,6,7,8,9,10)
```

### Eager Loading Multiple Associations

Active Record lets you eager load any number of associations with a single
`Model.find` call by using an array, hash, or a nested hash of array/hash with
the `includes` method.

### Array of Multiple Associations

```ruby
Customer.includes(:orders, :reviews)
```

This loads all the customers and the associated orders and reviews for each.

### Nested Associations Hash

```ruby
Customer.includes(orders: {books: [:supplier, :author]}).find(1)
```

This will find the customer with id 1 and eager load all of the associated orders for it, the books for all of the orders, and the author and supplier for each of the books.

### Specifying Conditions on Eager Loaded Associations

Even though Active Record lets you specify conditions on the eager loaded
associations just like `joins`, the recommended way is to use joins instead.

However if you must do this, you may use `where` as you would normally.

```ruby
Author.includes(:books).where(books: { out_of_print: true })
```

This would generate a query which contains a `LEFT OUTER JOIN` whereas the `joins`
method would generate one using the `INNER JOIN` function instead.

```sql
  SELECT authors.id AS t0_r0, ... books.updated_at AS t1_r5 FROM authors LEFT OUTER JOIN "books" ON "books"."author_id" = "authors"."id" WHERE (books.out_of_print = 1)
```

## preload

```ruby
books = Book.preload(:author).limit(10)

books.each do |book|
  puts book.author.last_name
end
```

The above code will execute just 2 queries, as opposed to the 11 queries from the original case:


```sql
SELECT `books`.* FROM `books` LIMIT 10
SELECT `authors`.* FROM `authors`
  WHERE `authors`.`book_id` IN (1,2,3,4,5,6,7,8,9,10)
```

The `preload` method uses an array, hash, or a nested hash of array/hash in the
same way as the `includes` method to load any number of associations with a
single `Model.find` call. However, unlike the `includes` method, it is not
possible to specify conditions for preloaded associations.

## eager_load

With `eager_load`, Active Record loads all specified associations using a `LEFT OUTER JOIN`.

```ruby
books = Book.eager_load(:author).limit(10)

books.each do |book|
  puts book.author.last_name
end
```

The above code will execute just 2 queries, as opposed to the 11 queries from the original case:

```sql
SELECT DISTINCT `books`.`id` FROM `books` LEFT OUTER JOIN `authors` ON `authors`.`book_id` = `books`.`id` LIMIT 10
SELECT `books`.`id` AS t0_r0, `books`.`last_name` AS t0_r1, ...
  FROM `books` LEFT OUTER JOIN `authors` ON `authors`.`book_id` = `books`.`id`
  WHERE `books`.`id` IN (1,2,3,4,5,6,7,8,9,10)
```

The `eager_load` method uses an array, hash, or a nested hash of array/hash in
the same way as the `includes` method to load any number of associations with a
single `Model.find` call. Also, like the `includes` method, you can specify
conditions for eager loaded associations.

## Reference

- [https://guides.rubyonrails.org/active_record_querying.html#eager-loading-associations](https://guides.rubyonrails.org/active_record_querying.html#eager-loading-associations)
