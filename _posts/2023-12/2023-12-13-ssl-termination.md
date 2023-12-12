---
title: "SSL Termination Definition"
published: true
tags: Network
---

SSL termination describes the transition process when data traffic becomes
encrypted and unencrypted. This happens at the server end of a secure socket
layer (SSL) connection.

## What Is SSL Termination?

SSL termination is a process by which SSL-encrypted data traffic is decrypted
(or offloaded). Servers with a secure socket layer (SSL) connection can
simultaneously handle many connections or sessions. An SSL connection sends
encrypted data between an end-user’s computer and web server by using a
certificate for authentication. SSL termination helps speed the decryption
process and reduces the processing burden on backend servers.

## How Does SSL Termination Work?

SSL termination intercepts encrypted https traffic when a server receives data
from a secure socket layer (SSL) connection in an SSL session. SSL termination
or SSL offloading decrypts and verifies data on the load balancer instead of
the application server. Spared of having to organize incoming connections, the
server can prioritize on other tasks like loading web pages. This helps
increase server speed. SSL termination represents the end — or termination
point — of an SSL connection.

## What is SSL Termination Load Balancer?

SSL termination at load balancer is desired because decryption is resource and
CPU intensive. Putting the decryption burden on the load balancer enables the
server to spend processing power on application tasks, which helps improve
performance. It also simplifies the management of SSL certificates.

## Is SSL Termination Secure?

Secure socket layer (SSL) connections are important for sensitive data. One
point to note is that after SSL termination unencrypted traffic is sent
between the load balancer and the backend server on the local area network.
However, for security purposes, administrators can choose to re-encrypt the
traffic at the load balancer before sending it to the servers.

SSL termination at load balancer alleviates web servers of the extra compute
cycles needed to decrypt SSL traffic. The security risk of terminating at the
load balancer is lessened when the load balancer is within the same data
center as the web servers. Some load balancers also provide the ability to use
a self-signed SSL between the load balancer and web servers. This provides a
secure connection, but requires more compute power.

## Can SSL Termination be Performed in Software?

With the advancement of Intel x86-based CPU technology, support for SSL on
standard Intel hardware has increased dramatically. The use of Elliptic Curve
Cryptography (ECC) keys with shorter key lengths than traditional RSA 2K keys
for SSL encryption has put software based load balancers on x86 servers ahead
in many cases.

An Advanced Encryption Standard New Instructions (AES-NI) is now integrated
into many processors. The purpose of the instruction set is to improve the
speed, as well as the resistance to side-channel attacks, of applications
performing encryption and decryption the latest security standards. Another
key reason to use software-based SSL termination is to completely decouple the
dependence on hardware to a simple software version upgrade, and to get
support for the latest security versions and bug fixes.

## Reference

- [https://avinetworks.com/glossary/ssl-termination/](https://avinetworks.com/glossary/ssl-termination/)