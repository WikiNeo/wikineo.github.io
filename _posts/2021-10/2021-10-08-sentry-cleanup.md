---
title: "Sentry Clean Up"
published: true
tags: Sentry 
---

## Remove logs older than 30 days

```shell
docker-compose --file ./docker-compose.yml exec worker sentry cleanup --days 30
```

## Change Sentry event retention days

```python
SENTRY_OPTIONS["system.event-retention-days"] = int(
    env("SENTRY_EVENT_RETENTION_DAYS", "30")
)
```

## Reference

- [https://forum.sentry.io/t/how-to-cleanup-sentry-in-docker/5877](https://forum.sentry.io/t/how-to-cleanup-sentry-in-docker/5877)