---
title: 'docker-compose ports'
published: true
tags: Docker
---

## ports

Expose ports

- Port mapping is incompatible with `network_mode: host`
- `docker-compose run` ignores `ports` unless you include `--service-ports`.

### Short syntax

There are three options:

- Specify both ports (`HOST:CONTAINER`)
- Specify just the container port (an ephemeral host port is chose for the host
  port)
- Specify the host IP address to bind to AND both ports (the default is 0.0.0.0,
  meaning all interface): (`IPADDR:HOSTPORT:CONTAINERPORT`). if `HOSTPORT` is
  empty (for example `127.0.0.1::80`), an ephemeral port is chosen to bind to on
  the host.
  - When mapping ports in the `HOST:CONTAINER` format, you may experience
    erroneous results when using a container port lower than 60, because YAML
    parses numbers in the format `xx:yy` as a base-60 value. For this reason, we
    recommend always explicitly specifying your port mappings as strings.
  
```Dockerfile
ports:
  - "3000"
  - "3000-3005"
  - "8000:8000"
  - "9090-9091:8080-8081"
  - "49100:22"
  - "127.0.0.1:8001:8001"
  - "127.0.0.1:5000-5010:5000-5010"
  - "127.0.0.1::5000"
  - "6060:6060/udp"
  - "12400-12500:1240"
```

### Long syntax

The long form syntax allows the configuration of additional fields that can't be
expressed in the short form, The long syntax is new in the v3.2 file format.

- `target`: the port inside the container
- `published`: the publicly exposed port
- `protocol`: the port protocol (`tcp` or `udp`)
- `mode`: `host` for publishing a host port on each node, or `ingress` for a
  swarm mode port to be load balanced.

```Dockerfile
ports:
  - target: 80
    published: 8080
    protocol: tcp
    mode: host
```

## Reference

- [https://docs.docker.com/compose/compose-file/compose-file-v3/](https://docs.docker.com/compose/compose-file/compose-file-v3/)