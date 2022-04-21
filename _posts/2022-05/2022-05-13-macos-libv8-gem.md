---
title: 'Install libv8 gem on MacOS'
published: true
tags: Ruby
---

```bash
brew install v8@3.15
bundle config build.libv8 --with-system-v8
bundle config build.therubyracer --with-v8-dir=$(brew --prefix v8@3.15)
bundle install
```

## Reference

- [https://stackoverflow.com/questions/19577759/installing-libv8-gem-on-os-x-10-9/58842254#58842254](https://stackoverflow.com/questions/19577759/installing-libv8-gem-on-os-x-10-9/58842254#58842254)