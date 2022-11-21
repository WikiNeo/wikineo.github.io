---
title: 'Same-Origin Policy'
published: true
tags: Network
---

The **same-origin policy** is a critical security mechanism that restricts how a
document or script loaded by one origin can interact with a resource from
another origin.

It helps isolate potentially malicious documents, reducing possible attack
vectors. For example, it prevents a malicious website on the Internet from
running JS in a browser to read data from a third-party webmail service (which
the user is signed into) or a company intranet (which is protected from direct
access by the attacker by not having a public IP address) and relaying that
data to the attacker.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy)