---
title: "HTTP headers"
published: true
tags: Network
---

HTTP headers let the client and the server pass additional information with an
HTTP request or response. An HTTP header consists of its case-insensitive name
followed by a colon (`:`), then by its value. Whitespace before the value is
ignored.

Custom proprietary headers have historically been used with an `X-` prefix, but
this convention was deprecated in June 2012 because of the inconveniences it
caused when nonstandard fields became standard in RFC 6648; others are listed
in an IANA registry, whose original content was defined in RFC 4229. IANA also
maintains a registry of proposed new HTTP headers.

Headers can be grouped according to their contexts:

- **Request headers** contain more information about the resource to be fetched, or
about the client requesting the resource.

- **Response headers** hold additional information about the response, like its location or about the server providing it.

- **Representation headers** contain information about the body of the
  resource, like its MIME type, or encoding/compression applied.

- **Payload headers** contain representation-independent information about payload
data, including content length and the encoding used for transport.

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)