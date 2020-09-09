---
title: "docker-compose ports vs expose"
published: true
tags: Docker
---

## Ports

Ports is defined as

> Exports ports. Either specify both ports (HOST:CONTAINER), or just the container port (a
> random host port will be chosen)

- Ports mentioned in `docker-compose.yml` wil be shared amount different services started
  by the docker-compose
- Ports will be exposed to the host machine to a random port or a given port

`docker-compose.yml`

```docker-compose
mysql:
  image: mysql:5.7
  ports:
    - "3306"
```

`docker-compose ps`

```shell
  Name                     Command               State            Ports
-------------------------------------------------------------------------------------
  mysql_1       docker-entrypoint.sh mysqld      Up      0.0.0.0:32769->3306/tcp
```

## expose

Expose is defined as

> Expose ports without publishing them to the host machine - they'll only be accessible to
> linked services. Only the internal port can be specified

- Ports are not exposed to host machine, only exposed to other services

```
mysql:
  image: mysql:5.7
  expose:
    - "3306"
```

```
 Name                  Command             State    Ports
---------------------------------------------------------------
 mysql_1      docker-entrypoint.sh mysqld   Up      3306/tcp
```

## References

- [https://stackoverflow.com/questions/40801772/what-is-the-difference-between-docker-compose-ports-vs-expose#:~:text=Ports%20is%20defined%20as%3A,started%20by%20the%20docker%2Dcompose.](https://stackoverflow.com/questions/40801772/what-is-the-difference-between-docker-compose-ports-vs-expose#:~:text=Ports%20is%20defined%20as%3A,started%20by%20the%20docker%2Dcompose.)