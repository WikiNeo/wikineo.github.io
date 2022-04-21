---
title: 'Install mysql2 gem on MacOS'
published: true
tags: Ruby
---

To fix for a manual gem install:

```
brew install openssl
gem install mysql2 -- --with-opt-dir="$(brew --prefix openssl)"
```

To fix for all bundle installs:

```
brew install openssl
bundle config --global build.mysql2 --with-opt-dir="$(brew --prefix openssl)"
bundle install
```

## Reference

- [https://stackoverflow.com/questions/5409761/installing-mysql2-gem-for-ruby-on-rails-with-mac-osx-10-6](https://stackoverflow.com/questions/5409761/installing-mysql2-gem-for-ruby-on-rails-with-mac-osx-10-6)