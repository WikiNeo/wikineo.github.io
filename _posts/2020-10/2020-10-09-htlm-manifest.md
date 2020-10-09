---
title: "HTML <html> manifest Attribute"
published: true
tags: HTML
---

A HTML document with a cache manifest (for offline broswing)

```html
<!DOCTYPE HTML>
<html manifest="demo.appcache">
<head>
<title>Title of the document</title>
</head>

<body>
The content of the document......
</body>

</html>
```

## Definition and Usage

The manifest attribute specifies the location of document's cache manifest.

HTML5 introduces application cache, which means that a web application is
cached, and accessible without an internet connection.

Application cache gives an application three advantages:

1. Offline browsing - users can use the application when they're offline
2. Speed - cached resources load faster
3. Reduced server load - the browser will only download updated/changed
   resources from the server

The manifest attribute should be included on every page of your web application
that you want cached.

The manifest file is a simple test file that lists the resources the browser
should cache for offline access.

## References

- [https://www.quanzhanketang.com/tags/att_html_manifest.html#:~:text=The%20manifest%20attribute%20specifies%20the,accessible%20without%20an%20internet%20connection.](https://www.quanzhanketang.com/tags/att_html_manifest.html#:~:text=The%20manifest%20attribute%20specifies%20the,accessible%20without%20an%20internet%20connection.)