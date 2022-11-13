---
title: 'Clickjacking'
published: true
tags: Network
---

Clickjacking is an interface-based attack that tricks website users into
unwittingly clicking on malicious links. In clickjacking, the attackers embed
their malicious links into buttons or legitimate pages in a website. In an
infected Site, whenever a user clicks on a legitimate link, the attacker gets
the confidential information of that user, which ultimately compromises the
user's privacy on the Internet.

Clickjacking can be prevented by implementing a Content Security Policy
(frame-ancestors) and implementing Set-Cookie attributes.

## Reference

- [https://developer.mozilla.org/en-US/docs/Glossary/Clickjacking](https://developer.mozilla.org/en-US/docs/Glossary/Clickjacking)