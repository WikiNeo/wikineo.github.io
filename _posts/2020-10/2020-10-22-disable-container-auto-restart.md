---
title: "Docker: how to disable container auto-restart"
published: true
tags: Docker
---

Change the restart-policy for an existing container

```shell
docker update --restart=no my-container
```

## Reference

- [docker - how do you disable auto-restart on a container?](https://stackoverflow.com/questions/37599128/docker-how-do-you-disable-auto-restart-on-a-container)
- [Restart policies(--restart)](https://docs.docker.com/engine/reference/run/#restart-policies---restart)
