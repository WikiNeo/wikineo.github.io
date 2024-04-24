---
title: "docker compose run --rm"
published: true
tags: Docker
---

If you want to remove the container after running while overriding the container’s restart policy, use the `--rm` flag:

```shell
docker compose run --rm web python manage.py db upgrade
```

This runs a database upgrade script, and removes the container when finished running, even if a restart policy is
specified in the service configuration.

## Reference

- [https://docs.docker.com/reference/cli/docker/compose/run/](https://docs.docker.com/reference/cli/docker/compose/run/)