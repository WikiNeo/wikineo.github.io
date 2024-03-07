---
title: "Nginx server"
published: true
tags: Nginx
---

```
Syntax:		server { ... }
Default:	—
Context:	http
```

Sets configuration for a virtual server. There is no clear separation between IP-based (based on the IP address) and name-based (based on the “Host” request header field) virtual servers. Instead, the listen directives describe all addresses and ports that should accept connections for the server, and the server_name directive lists all server names.

## Reference

- [https://nginx.org/en/docs/http/ngx_http_core_module.html#server](https://nginx.org/en/docs/http/ngx_http_core_module.html#server)