---
title: "Nginx $upstream_http_name"
published: true
tags: Nginx
---

```
$upstream_http_name

keep server response header fields. For example, the “Server” response header field is available through the $upstream_http_server variable. The rules of converting header field names to variable names are the same as for the variables that start with the “$http_” prefix. Only the header fields from the response of the last server are saved.
```


## Reference

- [https://nginx.org/en/docs/http/ngx_http_upstream_module.html#variables](https://nginx.org/en/docs/http/ngx_http_upstream_module.html#variables)