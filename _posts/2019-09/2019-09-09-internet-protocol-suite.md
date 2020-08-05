---
title:  "Internet Protocol Suite"
published: true
tags: Network
---

The **Internet protocol suite** is the conceptual model and set of communications
protocols used in the internet and similar computer networks. It is commonly known as
**TCP/IP** because the foundational protocols in the suite are the **Transmission Control
Protocol** (TCP) and the **Internet Protocol** (IP).

The Internet protocol suite provides end-to-end data communication specifying how data
should be packeized, addressed, transmitted, routed and received. This functionality is
organized into four abstraction layers, which classify all related protocols according to
the scope of networking involved. From lowest to highest, the layers are the link layer,
containing communication methods for data that remains within a single network segment
(link); the internet layer, providing internetworking between independent networks; the
transport layer, handling host-to-host communication; and the application layer, providing
process-to-process data exchange for applications.

## Application Layer

The application layer is the scope within which applications, or processes, create user
data and communicate this data to other applications on another or the same host. The
applications make use of the services provided by the underlying lower layers, especially
the transport layer which provides reliable or unreliable pipes to other processes. The
comminucations partners are characterized by the application architecture, such as the
client-server model and peer-to-peer networking. This is the layer in which all
application protocols such as SMTP, FTP, SSH, HTTP operate. Processes are addressed via
ports which essentially represent services.

## Transport Layer

The transport layer performs host-to-host communications on either the local network or
remote networks separated by routers. It provides a channel for the communication needs of
applications. UDP is the basic transport layer protocol, providing an unreliable
connectionless datagram service. The Transmission Control Protocol provides flow-control,
connection establishment, and reliable transmission of data.

## Internet Layer

The internet layer exchanges datagrams across network boundaries. It provides a uniform
networking interface that hides the actual topology (layout) of the underlying network
connections. It is therefore also the layer that establishes internetworking. Indeed, it
defines and establishes the Internet. This layer defines the addressing and routing
structures used for the TCP/IP protocol suite. The primary protocol in this scope is the
Internet Protocol, which defines IP addresses. Its function in routing is to transport
datagram to the next host, functioning as an IP router, that has the connectivity to a
network closer to the final destination.

## Link Layer

The link layer defines the networking methods within the scope of the local network link
on which hosts communicate without intervening routers. This layer includes the protocols
used to described the local network topology and the interfaces needed to affect
transmission of Internet layer datagrams to next-neighbor hosts.

References: [https://en.wikipedia.org/wiki/Internet_protocol_suite](https://en.wikipedia.org/wiki/Internet_protocol_suite)
