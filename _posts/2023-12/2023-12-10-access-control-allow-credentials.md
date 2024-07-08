---
title: "Access-Control-Allow-Credentials"
published: true
tags: Network
---

The `Access-Control-Allow-Credentials` response header tells browsers whether to
expose the response to the frontend JavaScript code when the request's
credentials mode (Request.credentials) is `include`.

When a request's credentials mode (Request.credentials) is `include`, browsers
will only expose the response to the frontend JavaScript code if the
`Access-Control-Allow-Credentials` value is `true`.

Credentials are cookies, authorization headers, or TLS client certificates.

When used as part of a response to a preflight request, this indicates whether
or not the actual request can be made using credentials. Note that simple GET
requests are not preflighted. So, if a request is made for a resource with
credentials, and if this header is not returned with the resource, the
response is ignored by the browser and not returned to the web content.

The `Access-Control-Allow-Credentials` header works in conjunction with the
XMLHttpRequest.withCredentials property or with the `credentials` option in the
Request() constructor of the Fetch API. For a CORS request with credentials,
for browsers to expose the response to the frontend JavaScript code, both the
server (using the `Access-Control-Allow-Credentials` header) and the client (by
setting the credentials mode for the XHR, Fetch, or Ajax request) must
indicate that they're opting into including credentials.

## Syntax

```http
Access-Control-Allow-Credentials: true
```

## Directives

- true
  - The only valid value for this header is `true` (case-sensitive). If you don't need credentials, omit this header entirely (rather than setting its value to `false`).

## Examples

XHR

```javascript
const xhr = new XMLHttpRequest();
xhr.open("GET", "https://example.com/", true);
xhr.withCredentials = true;
xhr.send(null);

```

Fetch

```javascript
fetch(url, {
  credentials: "include",
});
```

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Allow-Credentials)