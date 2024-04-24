---
title: "Docker Host Network Driver"
published: true
tags: Docker
---

If you use the `host` network mode for a container, that container's network stack isn't isolated from the Docker host
(the container shares the host's networking namespace), and the container doesn't get its own IP-address allocated. For
instance, if you run a container which binds to port 80 and you use `host` networking, the container's application is
available on port 80 on the host's IP address.

## Note

Given that the container does not have its own IP-address when using `host` mode networking, port-mapping doesn't take
effect, and the `-p`, `--publish`, `-P`, and `--publish-all` option are ignored, producing a warning instead:

### WARNING

- Published ports are discarded when using host network mode

Host mode networking can be useful for the following use cases:

- To optimize performance
- In situations where a container needs to handle a large range of ports

This is because it doesn't require network address translation (NAT), and no "userland-proxy" is created for each port.

## Reference

- [https://docs.docker.com/network/drivers/host/](https://docs.docker.com/network/drivers/host/)