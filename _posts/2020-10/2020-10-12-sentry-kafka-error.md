---
title: "Sentry Post Process Forwarder - KafkaError"
published: true
tags: Sentry
---

Sentry no more catches errors with this error, but the web interface still
works.

In some cases,the Post Process Forwarder gets into a bad state and you need to
do some manual cleanup.

1. Stop Sentry

    ```bash
    docker-compose stop
    ```

2. Start only Zookeeper and Kafka

    ```bash
    docker start sentry_onpremise_kafka_1 sentry_onpremise_zookeeper_1
    ```

3. Hop into the Kafka instance interactively

    ```bash
    docker exec -it sentry_onpremise_kafka_1 /bin/bash
    ```

4. Receive consumers list

    ```bash
    kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --list
    ```

5. Get group ifo

    ```bash
    kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --group snuba-post-processor -describe
    ```

6. Set the offsets to latest

    ```bash
    kafka-consumer-groups --bootstrap-server 127.0.0.1:9092 --group snuba-post-processor --topic events --reset-offsets --to-latest --execute
    ```

7. Exit Kafka instance

    ```bash
    exit
    ```

8. Stop Zookeeper and Kafka

    ```bash
    docker stop sentry_onpremise_kafka_1 sentry_onpremise_zookeeper_1
    ```

9. Restart Sentry

    ```bash
    docker-compose up
    ```

## References

- [https://forum.sentry.io/t/sentry-no-more-catch-errors/10500](https://forum.sentry.io/t/sentry-no-more-catch-errors/10500)
- [https://github.com/getsentry/onpremise/issues/478](https://github.com/getsentry/onpremise/issues/478)