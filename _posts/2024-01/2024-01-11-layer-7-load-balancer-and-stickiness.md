---
title: "Layer 7 Load Balancer and Stickiness"
published: true
tags: Network
---

Layer 7 load balancers also face another challenge known as stickiness or
persistence. The principle is that they generally have to direct multiple
subsequent requests or connections from a same origin (such as an end user) to
the same target. The best known example is the shopping cart on an online
store. If each click leads to a new connection, the user must always be sent
to the server which holds his shopping cart. Content-awareness makes it easier
to spot some elements in the request to identify the server to deliver it to,
but that's not always enough. For example if the source address is used as a
key to pick a server, it can be decided that a hash-based algorithm will be
used and that a given IP address will always be sent to the same server based
on a divide of the address by the number of available servers. But if one
server fails, the result changes and all users are suddenly sent to a different
server and lose their shopping cart. The solution against this issue consists
in memorizing the chosen target so that each time the same visitor is seen,
he's directed to the same server regardless of the number of available servers.
The information may be stored in the load balancer's memory, in which case it
may have to be replicated to other load balancers if it's not alone, or it may
be stored in the client's memory using various methods provided that the client
is able to present this information back with every request (cookie insertion,
redirection to a sub-domain, etc). This mechanism provides the extra benefit of
not having to rely on unstable or unevenly distributed information (such as the
source IP address). This is in fact the strongest reason to adopt a layer 7
load balancer instead of a layer 4 one.

## Reference

- [https://docs.haproxy.org/2.8/intro.html#2](https://docs.haproxy.org/2.8/intro.html#2)