---
title: 'Load Balancing'
published: true
tags: SystemDesign
---

Load Balancer helps to spread the traffic across a cluster of servers to
improve responsiveness and availability of applications, websites or
databases. LB also keeps track of the status of all the resources while
distributing requests. If a server is not available to take new requests or is
not responding or has elevated error rate, LB will stop sending traffic to
such a server.

## Loading Balancing Algorithms

### Health Checks

To monitor the health of a backend server, "health check" regularly attempts
to connect to backend servers to ensure that servers are listening. If a
server fails a health check, it is automatically removed from the pool, and
traffic will not be forwarded to it until it responds to the health checks
again.

- Least Connection Method
  - This method directs traffic to the server with the fewest active
    connections. This approach is quite useful when there are a large number
    of persistent client connections which are unevenly distributed between
    the servers.
- Least Response Time Method
  - This algorithm directs traffic to the server with the fewest active
    connections and the lowest average response time.
- Least Bandwidth method
  - This method selects the server that is currently serving the least amount
    of traffic measured in megabits per second (Mbps).
- Round Robin Method
  - This method cycles through a list of servers and sends each new request to
    the next server. It is most useful when the servers are of equal
    specification and there are not may persistent connections.
- Weighted Round Robin Method
  - The weighted round-robin scheduling is designed to better handle servers
    with different processing capacities. Each server is assigned a weight (an
    integer value that indicates the processing capacity). Servers with higher
    weights receive new connections before those with less weights and servers
    with higher weights get more connections than those with less weights.
- IP Hash
  - Under this method, a hash of the IP address of the client is calculated to
    redirect the request to a server.

## Redundant Load Balancers

The load balancers can be a single point of failure; to overcome this, a
second load balancer can be connected to the first to form a cluster. Each LB
monitors the health of the other and, since both of them are equality capable
of serving traffic and failure detection, in the event the main load balancer
fails, the second load balancer takes over.