---
title: "Passthrough Network Load Balancer"
published: true
tags: Network
---

**Passthrough Network Load Balancers (NLBs)** are a type of load balancer that
operates at the **Transport Layer (Layer 4)** of the OSI model. They pass traffic
directly to backend servers without altering the packets, enabling end-to-end
encryption and preserving the client IP address. This contrasts with load
balancers that terminate TLS, such as Layer 7 load balancers.

## How Passthrough NLBs Work

1. **Direct Connection**: A passthrough NLB forwards incoming client traffic
   (e.g., TCP, UDP) directly to the backend servers without decrypting or
   inspecting the payload.
2. **TLS Handshake**: Any encryption or decryption (e.g., TLS/SSL) happens
   directly between the client and the backend server.
3. **Client IP Preservation**: The original client IP address is maintained in
   the connection, allowing backend servers to log it or use it for routing
   decisions.

## Key Features

1. **Layer 4 Routing**:
   - Routes traffic based on protocol (TCP, UDP) and port numbers.
   - Minimal packet inspection ensures high performance and low latency.
2. **End-to-End Encryption**:
   - Since the NLB does not terminate TLS, the connection remains encrypted
     between the client and backend servers.
   - Ideal for scenarios where backend servers manage their own encryption keys
     and certificates.
3. **Preserves Client IP**:
   - Useful for logging, security policies, or geolocation-based decisions on
     the backend.
4. **High Performance**:
   - Because it does not perform tasks like TLS termination or deep packet
     inspection, passthrough NLBs handle high volumes of traffic with minimal
     overhead.
5. **Protocol Support**:
   - Supports TCP, UDP, and sometimes custom protocols.
   - Typically does not support HTTP-specific features like URL-based routing or
     header inspection.

## Use Cases

1. **Secure Applications**:
   - Applications requiring end-to-end TLS encryption (e.g., financial services
     or healthcare).
2. **Gaming and VoIP**:
   - High-performance routing for latency-sensitive applications using UDP or TCP.
3. **IoT and Custom Protocols**:
   - Supports non-HTTP protocols and custom application-level traffic.
4. **Logging and Security**:
   - Scenarios where client IP preservation is critical.

## Advantages

1. **End-to-End Encryption**:
   - Backend servers handle encryption and decryption, ensuring that no intermediary device has access to plaintext data.
2. **High Throughput and Low Latency**:
   - Optimized for simple, high-speed packet forwarding.
3. **Client IP Preservation**:
   - Enables backend servers to access and use the actual client IP without additional configuration.
4. **Protocol Flexibility**:
   - Can handle a wide variety of protocols beyond HTTP/HTTPS.

## Disadvantages

1. **Backend Overhead**:
   - Backend servers must manage TLS/SSL termination, increasing their computational load.
2. **Limited Features**:
   - Lacks Layer 7 capabilities like URL-based routing, caching, or advanced application-layer features.
3. **Complex Certificate Management**:
   - Certificates must be distributed and maintained on all backend servers.

## Comparison with Other Load Balancers

| Feature                | Passthrough NLB                     | TLS Terminating LB                                                                                       |
| ---------------------- | ----------------------------------- | -------------------------------------------------------------------------------------------------------- |
| Encryption             | End-to-End (TLS handled by backend) | Terminates at LB                                                                                         |
| Performance            | Higher (no decryption overhead)     | Lower(handles encryption/decryption)                                                                     |
| Client IP Preservation | Yes                                 | No (client IP is that of the LB, and it may require special configuration e.g., X-Forwarded-For header ) |
| Protocol Support       | TCP, UDP, custom                    | HTTP, HTTPS, WebSocket                                                                                   |
| Routing                | Basic (IP and port-based)           | Advanced (URL-based, header inspection)                                                                  |

## Popular Passthrough NLB Implementations

1. **AWS Network Load Balancer**:
   - Optimized for high throughput and low latency.
   - Supports TCP, UDP, and TLS passthrough.
2. **Azure Load Balancer**:
   - Provides Layer 4 load balancing for TCP and UDP.
   - Enables direct server return (DSR).
3. **NGINX/HAProxy** (as configured):
   - Open-source options that can be set up for Layer 4 passthrough.
