---
title: 'Docker bridge vs host'
published: true
tags: Docker
---

According to the docker documentation about bridge networking:

> In terms of Docker, a bridge network uses a software bridge which allows containers connected to the same bridge network to communicate, while providing isolation from containers which are not connected to that bridge network.

According to the docker documentation about host networking

> If you use the host network driver for a container, that container’s network stack is not isolated from the Docker host. For instance, if you run a container which binds to port 80 and you use host networking, the container’s application will be available on port 80 on the host’s IP address.

If you want to deploy multiple containers connected between them with a private internal network use bridge networking. If you want to deploy a container connected to the same network stack as the host (and access the same networks as the host) use host networking. If you simply want to publish some ports, run the container with the `--publish` or `-p` option, such as `-p 8080:80`.

## Reference

- [https://stackoverflow.com/questions/56825258/difference-between-docker-bridge-and-host-driver](https://stackoverflow.com/questions/56825258/difference-between-docker-bridge-and-host-driver)