---
title:  "TCP Connection Establishment and Termination"
published: true
tags: Network
---

## Connection establishment

To establish a connection, TCP uses a three-way handshake. Before a client attempts to
connect with server, the server must first bind to and listen at a port to open it up for
connections: this is called a passive open. Once the passive open is established, a client
may initiate an active open. To establish a connection the three-way (or 3-step) handshake
occurs:

1. **SYN**: The active open is performed by the client sending a SYN to the server. The
   client sets the segment's sequence number to a random value A.
2. **SYN-ACK**: In response, the server replies with a SYN-ACK. The acknowledgement number
   is set one more than the received sequence number i.e. A+1, and the sequence number
   that the server chooses for the packet is another random umber, B.
3. **ACK**: Finally, the client sends an ACK back to the server. The sequence number is
   set to the received acknowledge value i.e. A+1, and the acknowledgement number is set
   to one more than the received sequence number i.e. B+1.

At this point, both the client and server have received an acknowledgement of the
connection. The step 1, 2 establish the connection parameter (sequence number) for one
direction and it is acknowledged. The step 2, 3 establish the connection parameter
(sequence number) for the other direction and it is acknowledged. With these, a
full-duplex communication is established.

## Connection termination

The connection termination phase uses a four-way handshake, with each side of the
connection terminating independently. When an endpoint wishes to stop its half of the
connection, it transmits a FIN packet, which the other end acknowledges with an ACK.
Therefore, a typical tear-down requires a pair of FIN and ACK segments from each TCP
endpoint. After the side that sent the first FIN has responded with the final ACK, it
waits for a timeout before finally closing the connection, during which time the local
port is unavailable for new connections; this prevents confusion due to delayed packets
being delivered during subsequent connections.

A connection can be "half-open", in which case one side has terminated its end, but the
other has not. The side that has terminated can no longer send any data into the
connection, the the other side can. The terminating side should continue reading the data
until the other side terminates as well.

It is also possible to terminate the connection by a 3-way handshake, when host A sends a
FIN and host B replies with a FIN & ACK (merely combines 2 steps into one) and host A
replies with an ACK.

References: [https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment](https://en.wikipedia.org/wiki/Transmission_Control_Protocol#Connection_establishment)
