---
title: '[Rails] Use Github Gem in Gemfile'
published: true
tags: Ruby
---

To solve the warnings of insecure Github gem download with git protocol, use
https instead

```shell
gem 'nokogiri', '1.7.0.1', git: 'https://github.com/sparklemotion/nokogiri'
```

## Reference

- [https://bundler.io/guides/git.html](https://bundler.io/guides/git.html)