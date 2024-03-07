---
title: "Nginx proxy_hide_header"
published: true
tags: Nginx
---


```
Syntax:		proxy_hide_header field;
Default:	—
Context:	http, server, location
```

By default, nginx does not pass the header fields “Date”, “Server”, “X-Pad”, and “X-Accel-...” from the response of a proxied server to a client. The proxy_hide_header directive sets additional fields that will not be passed.

## Reference

- [https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_hide_header](https://nginx.org/en/docs/http/ngx_http_proxy_module.html#proxy_hide_header)