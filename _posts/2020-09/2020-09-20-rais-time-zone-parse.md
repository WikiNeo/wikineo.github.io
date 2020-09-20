---
title: "Rails Time.zone.parse"
published: true
tags: Ruby
---

```ruby
class ActiveSupport:TimeZone

parse(str, now = now()) public
```

Method for creating new `ActiveSupport::TimeWithZone` instance in the zone of `self` from
parsed string.

```ruby
Time.zone = 'Hawaii'                   # => "Hawaii"
Time.zone.parse('1999-12-31 14:00:00') # => Fri, 31 Dec 1999 14:00:00 HST -10:00
```

If upper components are missing from the string, they are supplied from `TimeZone#now`

```ruby
Time.zone.now               # => Fri, 31 Dec 1999 14:00:00 HST -10:00
Time.zone.parse('22:30:00') # => Fri, 31 Dec 1999 22:30:00 HST -10:00
```

However, if the date component is not provided, but any other upper components are
supplied, then the day of the month defaults to 1

```ruby
Time.zone.parse('Mar 2000') # => Wed, 01 Mar 2000 00:00:00 HST -10:00
```

If the string is invalid then an `ArgumentError` could be raised.

## Reference

- [https://apidock.com/rails/ActiveSupport/TimeZone/parse](https://apidock.com/rails/ActiveSupport/TimeZone/parse)