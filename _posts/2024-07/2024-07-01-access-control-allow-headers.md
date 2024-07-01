---
title: Access-Control-Allow-Headers
published: true
tags: Network
---
The `Access-Control-Allow-Headers` response header is used in response to a
`preflight request` which includes the `Access-Control-Request-Headers` to
indicate which HTTP headers can be used during the actual request.

This header is required if the request has an `Access-Control-Request-Headers`
header.

## Syntax

```HTTP
Access-Control-Allow-Headers: [<header-name>[, <header-name>]*]
Access-Control-Allow-Headers: *
```

## Directives

- `<header-name>`

  - The name of a supported request header. The header may list any number of
    headers, separated by commas.

- `* (wildcard)`
  - The value "_" only counts as a special wildcard value for requests without credentials (requests without HTTP cookies or HTTP authentication information). In requests with credentials, it is treated as the literal header name "_" without special semantics. Note that the Authorization header can't be wildcarded and always needs to be listed explicitly.

