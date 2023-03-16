---
title: "Subnets Settings"
published: true
tags: AWS
---

## Subnet settings

All subnets have a modifiable attribute that determines whether a network
interface created in that subnet is assigned a public IPv4 address and, if
applicable, an IPv6 address. This includes the primary network interface
(eth0) that's created for an instance when you launch an instance in that
subnet. Regardless of the subnet attribute, you can still override this
setting for a specific instance during launch.

After you create a subnet, you can modify the following settings for the
subnet.

**Auto-assign IP settings**: Enables you to configure the auto-assign IP settings
to automatically request a public IPv4 or IPv6 address for a new network
interface in this subnet.

**Resource-based Name (RBN) settings**: Enables you to specify the hostname type
for EC2 instances in this subnet and configure how DNS A and AAAA record
queries are handled. For more information about these settings, see Amazon EC2
instance hostname types in the Amazon EC2 User Guide for Linux Instances.

## Reference

- [https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)