---
title: "Subnets Basics"
published: true
tags: AWS
---

A subnet is a range of IP addresses in your VPC. You can launch AWS resources
into your subnets.

## Subnet basics

A subnet is a range of IP addresses in your VPC. You can launch AWS resources,
such as EC2 instances, into a specific subnet. When you create a subnet, you
specify the IPv4 CIDR block for the subnet, which is a subset of the VPC CIDR
block. Each subnet must reside entirely within one Availability Zone and
cannot span zones. By launching instances in separate Availability Zones, you
can protect your applications from the failure of a single zone.

You can optionally add subnets in a Local Zone, which is an AWS infrastructure
deployment that places compute, storage, database, and other select services
closer to your end users. A Local Zone enables your end users to run
applications that require single-digit millisecond latencies. For more
information, see Local Zones in the Amazon EC2 User Guide for Linux Instances.

## Reference

- [https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html)