---
title: TARGET_CONNECT_TIMEOUT and TARGET_READ_TIMEOUT
published: true
tags: Apigee
---

## VPC Peering 503 Service Unavailable error with TARGET_CONNECT_TIMEOUT

The "TARGET_CONNECT_TIMEOUT" reason indicates a connection timeout between the Apigee instance and the target when using VPC Peering.

```javascript
{"fault":{"faultstring":"The Service is temporarily unavailable",
"detail":{"errorcode":"messaging.adaptors.http.flow.ServiceUnavailable",
"reason":"TARGET_CONNECT_TIMEOUT"}}}
```

## 504 Gateway timeout - TARGET_READ_TIMEOUT

The TARGET_READ_TIMEOUT reason indicates that Apigee runtime did not receive a
timely response from the target during the execution of a request. The default
target read timeout value (io.timeout.millis) is 55 seconds. Which means that if
after 55 seconds the target doesn't respond, Apigee throws this error:

```javascript
{"fault":{"faultstring":"Gateway Timeout",
  "detail":{"errorcode":"messaging.adaptors.http.flow.GatewayTimeout",
  "reason":"TARGET_READ_TIMEOUT"}}}
```

## References

- [https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/vpc-503-target-connect-timeout](https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/vpc-503-target-connect-timeout)
- [https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout](https://cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/runtime/504-target-read-timeout)
