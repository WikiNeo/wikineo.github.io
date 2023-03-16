---
title: "Subnets Types"
published: true
tags: AWS
---

## Subnet types

Depending on how you configure routing for your subnets, they are considered
either public, private, or VPN-only:

**Public subnet**: The subnet has a direct route to an internet gateway. Resources
in a public subnet can access the public internet.

**Private subnet**: The subnet does not have a direct route to an internet
gateway. Resources in a private subnet require a NAT device to access the
public internet.

**VPN-only subnet**: The subnet has a route to a Site-to-Site VPN connection
through a virtual private gateway. The subnet does not have a route to an
internet gateway.

When you create a subnet, you specify its IP addresses, depending on the
configuration of the VPC:

**IPv4 only**: The subnet has an IPv4 CIDR block but does not have an IPv6
CIDR block. Resources in an IPv4-only subnet must communicate over IPv4.

**Dual stack**: The subnet has both an IPv4 CIDR block and an IPv6 CIDR block.
The VPC must have both an IPv4 CIDR block and an IPv6 CIDR block. Resources in
a dual-stack subnet can communicate over IPv4 and IPv6.

**IPv6 only**: The subnet has an IPv6 CIDR block but does not have an IPv4
CIDR block. The VPC must have an IPv6 CIDR block. Resources in an IPv6-only
subnet must communicate over IPv6.

Regardless of the type of subnet, the internal IPv4 address range of the
subnet is always private—we do not announce the address block to the internet.
For more information about private IP addressing in VPCs, see IP addressing.

## Reference

- [https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)