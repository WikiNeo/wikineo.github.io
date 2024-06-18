---
title: Preflight request
published: true
tags: Network
---
A CORS preflight request is a CORS request that checks to see if the CORS
protocol is understood and a server is aware using specific methods and headers.

It is an `OPTIONS` request, using two or three HTTP request headers:
`Access-Control-Request-Method`, `Origin`, and optionally
`Access-Control-Request-Headers`.

A preflight request is automatically issued by a browser and in normal cases,
front-end developers don't need to craft such requests themselves. It appears
when request is qualified as "to be preflighted" and omitted for simple
requests.

For example, a client might be asking a server if it would allow a `DELETE`
request, before sending a `DELETE` request, by using a preflight request:

```HTTP
OPTIONS /resource/foo
Access-Control-Request-Method: DELETE
Access-Control-Request-Headers: x-requested-with
Origin: https://foo.bar.org
```

If the server allows it, then it will respond to the preflight request with an
`Access-Control-Allow-Methods` response header, which lists `DELETE`:

```HTTP
HTTP/1.1 204 No Content
Connection: keep-alive
Access-Control-Allow-Origin: https://foo.bar.org
Access-Control-Allow-Methods: POST, GET, OPTIONS, DELETE
Access-Control-Allow-Headers: X-Requested-With
Access-Control-Max-Age: 86400
```

The preflight response can be optionally cached for the requests created in the
same URL using `Access-Control-Max-Age` header like in the above example. To
cache preflight responses, the browser uses a specific cache that is separate
from the general HTTP cache that the browser manages. Preflight responses are
never cached in the browser's general HTTP cache.

## Reference

- [https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request)

