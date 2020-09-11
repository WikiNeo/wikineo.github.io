---
title: "Change default timezone for Active Record n Rails"
published: true
tags: Ruby
---

> In `application.rb`, `config.active_record.default_timezone` determines whether
> to use `Time.local` (if set to `:local`) or `Time.utc` (if set to `:utc`) when
> pulling dates and times from the database. The default is `:utc`.
> http://guides.rubyonrails.org/configuring.html

---------------------------------------
If you want to change Rails timezone, but continues to have Active Record to
save in the database in UTC, use

```ruby
# application.rb
config.time_zone = 'Eastern Time (US & Canada)'
```

--------------------------------------------;

If you want to change Rails timezone AND have Active Record store times in this
timezone, use

```ruby
# application.rb
config.time_zone = 'Eastern Time (US & Canada)'
config.active_record.default_timezone = :local
```

WARNING: you really should think twice, even thrice, before saving times in the
database in a non-UTC format.

NOTES: Do not forget to restart your Rails server after modifying
`application.rb`

-----------------------------------------------------;

Remember that `config.active_record.default_timezone` can take only two values

- `:local` (converts to the timezone defined in `config.time_zone`)
- `:utc` (converts to UTC)

------------------------------------------------------;

Here's how you can find all available timezones

```shell
rake time:zones:all
```

## Reference

- [https://stackoverflow.com/questions/6118779/how-to-change-default-timezone-for-active-record-in-rails](https://stackoverflow.com/questions/6118779/how-to-change-default-timezone-for-active-record-in-rails)