---
title: "Reverse Proxy Load Balancer"
published: true
tags: Network
---

**Reverse proxy load balancers** are components in a network architecture that serve two main purposes:

---

### 🔁 **1. Reverse Proxy**

A **reverse proxy** sits in front of backend servers and handles client requests on their behalf. It:

- **Receives requests** from clients (e.g., web browsers)
- **Forwards** those requests to one of the backend servers
- **Returns** the server's response to the client

📌 Think of it as a gatekeeper between clients and servers.

---

### ⚖️ **2. Load Balancer**

A **load balancer** distributes incoming traffic across multiple backend servers to:

- Maximize **speed and capacity utilization**
- Prevent any one server from being **overwhelmed**
- Provide **redundancy** and **high availability**

---

### 🔧 Combined: Reverse Proxy Load Balancer

When combined, this system:

- Accepts all client requests
- Chooses a backend server based on a **load balancing algorithm**
- Forwards the request to that server
- Returns the response to the client

### 📊 Common Load Balancing Algorithms

- **Round Robin** – rotates through servers in order
- **Least Connections** – sends to the server with the fewest active connections
- **IP Hash** – hashes the client IP to choose a server
- **Weighted Round Robin / Least Connections** – gives preference to more powerful servers

---

### 🔐 Benefits

- **Scalability** – easily add/remove backend servers
- **Security** – hides internal servers, enabling TLS termination and DDoS protection
- **Caching** – can cache responses to reduce backend load
- **SSL Offloading** – handles encryption at the proxy instead of each backend

---

### 🛠️ Examples

- **Nginx** and **HAProxy** – widely used open-source reverse proxy/load balancers
- **AWS ELB**, **Cloudflare**, **Traefik** – managed or modern alternatives
