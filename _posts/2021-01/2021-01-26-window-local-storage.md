---
title: 'Window.localStorage'
published: true
tags: Web
---

The read-only `localStorage` property allows you to access a `Storage` object
for the `Document`'s origin; the stored data is saved across browser sessions.
`localStorage` is similar to `sessionStorage`, except that while data stored in
`localStorage` has no expiration time, data stored in `sessionStorage` gets
cleared when the page session ends - that is, when the page is closed. (Data in
a `localStorage` object created in a "private browsing" or `incognito` session
is cleared when the last "private" tab is closed.)

Data stored in either `localStorage` is specific to the protocol of the page. In
particular, data stored by a script on a site accessed with HTTP is put in a
different `localStorage` from the same site accessed with HTTPS

## Syntax

```javascript
myStorage = window.localStorage
```

## Example

```javascript
localStorage.setItem('myCat', 'Tom');
const cat = localStorage.getItem('myCat');
localStorage.removeItem('myCat');
localStorage.clear();
```

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage)