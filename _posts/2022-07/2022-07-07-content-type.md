---
title: 'HTTP Headers Content-Type'
published: true
tags: Network
---

The Content-Type representation header is used to indicate the original media type of the resource (prior to any content encoding applied for sending).

In responses, a Content-Type header provides the client with the actual content type of the returned content. This header's value may be ignored, for example when browsers perform MIME sniffing; set the X-Content-Type-Options header value to nosniff to prevent this behavior.

In requests, (such as POST or PUT), the client tells the server what type of data is actually sent.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type)