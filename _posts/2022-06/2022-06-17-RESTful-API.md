---
title: 'RESTful API'
published: true
tags: DesignPattern
---

## What is RESTful API?

RESTful API is an interface that two computer systems use to exchange
information securely over the internet. RESTful APIs support information
exchange by following secure, reliable, and efficient software communication
standards.

## What is an API?

An application programming interface (API) defines the rules that you must
follow to communicate with other software systems.

### Clients

Clients are users who want to access information from the web.

### Resources

Resources are the information that different applications provide to their
clients.

### Server

The machine that gives the resources to the client is called the server.

## What is REST?

Representational State Transfer (REST) is a software architecture that imposes
conditions on how an API should work.

### Uniform interface

It indicates that the server transfers information in a standard format.

1. Requests should identify resources. They do so by using a uniform resource identifier.
2. Clients have enough information in the resource representation to modify or delete the resource if they want to. The server meets this condition by sending metadata that describes the resource further.
3. Clients receive information about how to process the representation further. The server achieves this by sending self-descriptive messages that contain metadata about how the client can best use them.
4. Clients receive information about all other related resources they need to complete a task. The server achieves this by sending hyperlinks in the representation so that clients can dynamically discover more resources.

### Statelessness

In REST architecture, statelessness refers to a communication method in which the server completes every client request independently of all previous requests

### Layered system

In a layered system architecture, the client can connect to other authorized intermediaries between the client and server, and it will still receive responses from the server.

### Cacheability

RESTful web services support caching, which is the process of storing some responses on the client or on an intermediary to improve server response time.

### Code on demand

In REST architectural style, servers can temporarily extend or customize
client functionality by transferring software programming code to the client.
For example, when you fill a registration form on any website, your browser
immediately highlights any mistakes you make, such as incorrect phone numbers.
It can do this because of the code sent by the server.


## Reference

- [https://aws.amazon.com/what-is/restful-api/](https://aws.amazon.com/what-is/restful-api/)