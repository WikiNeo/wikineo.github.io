---
title: "TLS/SSL Offloading"
published: true
tags: Network
---

**TLS offloading** (also called **SSL offloading**) is the process of moving the
computational work of encrypting and decrypting TLS (Transport Layer Security)
traffic from the main web server to a separate device or service, such as a
**load balancer**, **reverse proxy**, or **dedicated TLS terminator**.

### Why TLS Offloading?

TLS encryption is **CPU-intensive**, especially under high traffic. Offloading helps:

- **Reduce load** on the application server
- **Improve performance** and response times
- **Centralize certificate management**

---

### How It Works

1. **Client connects** to the public endpoint (e.g. a load balancer) using HTTPS/TLS.
2. The **load balancer terminates the TLS** session—decrypting the request.
3. The request is **forwarded in plaintext** (HTTP) or re-encrypted (HTTPS) to the internal server.
4. The server processes the request and returns the response.
5. The load balancer **re-encrypts** the response (if needed) and sends it back to the client.

---

### Common Use Cases

- **Cloud services** (e.g., AWS Elastic Load Balancer, Azure Application Gateway)
- **Hardware appliances** (e.g., F5, Citrix ADC)
- **Reverse proxies** (e.g., NGINX, HAProxy, Envoy)

---

### Variants

- **TLS Termination**: TLS ends at the proxy/load balancer; backend gets plain HTTP.
- **TLS Passthrough**: TLS traffic is not decrypted until it reaches the backend.
- **TLS Bridging**: Decrypt TLS at the edge, inspect/modify, then re-encrypt and forward.

---
