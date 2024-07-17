---
title: "AWS NAT gateways"
published: true
tags: AWS
---

A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT
gateway so that instances in a private subnet can connect to services outside
your VPC but external services cannot initiate a connection with those
instances.

When you create a NAT gateway, you specify one of the following connectivity
types:

- Public – (Default) Instances in private subnets can connect to the internet
  through a public NAT gateway, but cannot receive unsolicited inbound connections
  from the internet. You create a public NAT gateway in a public subnet and must
  associate an elastic IP address with the NAT gateway at creation. You route
  traffic from the NAT gateway to the internet gateway for the VPC. Alternatively,
  you can use a public NAT gateway to connect to other VPCs or your on-premises
  network. In this case, you route traffic from the NAT gateway through a transit
  gateway or a virtual private gateway.

- Private – Instances in private subnets can connect to other VPCs or your
  on-premises network through a private NAT gateway. You can route traffic from
  the NAT gateway through a transit gateway or a virtual private gateway. You
  cannot associate an elastic IP address with a private NAT gateway. You can
  attach an internet gateway to a VPC with a private NAT gateway, but if you route
  traffic from the private NAT gateway to the internet gateway, the internet
  gateway drops the traffic.

Both private and public NAT gateways map the source private IPv4 address of the
instances to the private IPv4 address of the NAT gateway, but in the case of a
public NAT gateway, the internet gateway then maps the private IPv4 address of
the public NAT Gateway to the Elastic IP address associated with the NAT
Gateway. When sending response traffic to the instances, whether it's a public
or private NAT gateway, the NAT gateway translates the address back to the
original source IP address.

## IMPORTANT

You can use either a public or private NAT gateway to route traffic
to transit gateways and virtual private gateways.

If you use a private NAT gateway to connect to a transit gateway or virtual
private gateway, traffic to the destination will come from the private IP
address of the private NAT gateway.

If you use a public NAT gateway to connect to a transit gateway or virtual
private gateway, traffic to the destination will come from the private IP
address of the public NAT gateway unless you use an internet gateway. The public
NAT gateway will only use its EIP as the source IP address when used in
conjunction with an internet gateway.

## Reference

- [https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
