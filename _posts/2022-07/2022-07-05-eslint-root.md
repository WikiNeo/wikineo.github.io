---
title: 'ESlint root'
published: true
tags: Node.js
---

Some generated project gives error in Webstorm, add the following to fix it

```javascript
{
    "root": true
}
```

By default, ESLint will look for configuration files in all parent folders up
to the root directory. This can be useful if you want all of your projects to
follow a certain convention, but can sometimes lead to unexpected results. To
limit ESLint to a specific project, place `"root": true` inside the `.eslintrc.*`
file or `eslintConfig` field of the `package.json` file or in the `.eslintrc.*` file
at your project’s root level. ESLint will stop looking in parent folders once
it finds a configuration with `"root": true.`

## Reference

- [https://eslint.org/docs/latest/user-guide/configuring/configuration-files](https://eslint.org/docs/latest/user-guide/configuring/configuration-files)