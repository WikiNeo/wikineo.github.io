---
title: "WebSocket"
published: true
tags: Network
---

The `WebSocket` protocol, described in the specification [RFC
6455](https://tools.ietf.org/html/rfc6455) provides a way to exchange data between browser
and server via a persistent connection. The data can be passed in both directions as
"packets", without breaking the connection and additional HTTP-requests.

WebSocket is especially great for services that require continuous data exchange, e.g.
online games, real-time trading systems and so on.

## A simple example

To open a websocket connection, we need to create `new WebSocket` using the special
protocol `es` in the url:

```javascript
let socket = new WebSocket("ws://javascript.info");
```

There's also encrypted `wss://` protocol. It's like HTTPS for websocket.

Once the socket is created, we should listen to events on it. There are totally 4 events:

- `open` - connection established.
- `message` - data received.
- `error` - websocket error.
- `close` - connection closed.

And if we'd like to send something, when `socket.send(data)` will do that.

```javascript
let socket = new WebSocket("wss://javascript.info/article/websocket/demo/hello");

socket.onopen = function(e) {
  alert("[open] Connection established");
  alert("Sending to server");
  socket.send("My name is John");
};

socket.onmessage = function(event) {
  alert(`[message] Data received from server: ${event.data}`);
};

socket.onclose = function(event) {
  if (event.wasClean) {
    alert(`[close] Connection closed cleanly, code=${event.code} reason=${event.reason}`);
  } else {
    // e.g. server process killed or network down
    // event.code is usually 1006 in this case
    alert('[close] Connection died');
  }
};

socket.onerror = function(error) {
  alert(`[error] ${error.message}`);
};
```

## Opening a websocket

When `new WebSocket(url)` is created, it starts connecting immediately.

During the connection the browser (using headers) asks the server: "Do you support
WebSocket?" And if the server replies "yes", then the talk continues in WebSocket
protocol, which is not HTTP at all.

Here's an example of browser headers for request made by `new
WebSocket("wss://javascript.info/chat")`

```bash
GET /chat
Host: javascript.info
Origin: https://javascript.info
Connection: Upgrade
Upgrade: websocket
Sec-WebSocket-Key: Iv8io/9s+lYFgZWcXczP8Q==
Sec-WebSocket-Version: 13
```

- `Origin` - the origin of the client page, e.g. `https://javascript.info`. WebSocket
  objects are cross-origin by nature. There are no special headers or other limitations.
  Old servers are unable to handle WebSocket anyway, so there are no compabitility issues.
  But `Origin` header is import, as it allows the server to decide whether or not to talk
  WebSocket with this website.
- `Connection: Upgrade` - signals that the client would like to change the protocol.
- `Upgrade: websocket` - the requested protocol is `websocket`
- `Sec-Websocket-Key` - a random browser-generated key for security.
- `Sec-WebSocket-Version` - WebSocket protocol version, 13 is the current one.

If the server agrees to switch to WebSocket, it should send code 101 response:

```bash
101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: hsBlbuDTkk24srzEOTBUlZAlC2g=
```

Here `Sec-WebSocket-Accept` is `Sec-Websocket-Key`, recoded using a special algorithm. The
browser uses it to make sure that the response corresponds to the request.

Afterwards, the data is transferred using WebSocket protocol, we'll see its
structure("frames") soon. And that's not HTTP at all.

## Data transfer

WebSocket communication consists of "frames" - data fragments, that can be sent from
either side, and can be of several kinds:

- "text frames" - contain text data that parties send to each other.
- "binary data frames" - contain binary data that parties send to each other.
- "ping/pong frames" are used to check the connection, sent from the server, the browser
  responds to these automatically.
- there's also "connection close frame" and a few other service frames.

In the browser, we directly work only with text or binary frames.

**WebSocket `.send()` method can send either text or binary data**.

A call `socket.send(body)` allows `body` in string or a binary format, including `Blob`,
`ArrayBuffer`, etc. No settings required: just send it out in any format.

**When we receive the data, text always comes as string. And for binary data, we can
choose between `Blob` and `ArrayBuffer` formats**.

References:

- [https://javascript.info/websocket](https://javascript.info/websocket)
