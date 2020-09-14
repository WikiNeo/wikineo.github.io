---
title: "127.0.0.1 vs 0.0.0.0"
published: true
tags: Network
---

## What's the difference between 127.0.0.1 and 0.0.0.0

### 127.0.0.1

- is the loopback address (also known as localhost)
- is normally the IP address assigned to the "loopback" or local-only interface.
  This is a "fake" network adapter that can only communicate within the same
  host. It is often used when you want a network-capable application to only
  serve clients on the same host. A process that is listening on `127.0.0.1` for
  connections will only receive local connections on that socket.

### localhost

- is normally the hostname for `127.0.0.1` IP address. It is usually set in
  `/etc/hosts`. You can use it just like any other hostname.

### 0.0.0.0

- is a non-routable meta-address used to designate an invalid, unknown or non
  applicable target (a no particular address placeholder)
- In the context of a route entry, it usually means the default route.
- In the context of servers, `0.0.0.0` means "all IPv4 address on the local
  machine". If a host has two ip addresses, `192.168.1.1` and `10.1.2.1`, and a
  server running on the host listens `0.0.0.0`, it will be reachable at both of
  those IPs.

## Reference

- [https://superuser.com/questions/949428/whats-the-difference-between-127-0-0-1-and-0-0-0-0](https://superuser.com/questions/949428/whats-the-difference-between-127-0-0-1-and-0-0-0-0)
- [https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost](https://stackoverflow.com/questions/20778771/what-is-the-difference-between-0-0-0-0-127-0-0-1-and-localhost)