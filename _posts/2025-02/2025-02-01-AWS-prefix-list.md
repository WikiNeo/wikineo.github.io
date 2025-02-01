---
title: "AWS Prefix List"
published: true
tags: AWS
---

In AWS, a **Prefix List** is a set of one or more CIDR blocks that can be used
as a reference in security groups, route tables, and network ACLs. It simplifies
network management by allowing you to group multiple IP ranges under a single
identifier instead of managing multiple individual CIDR blocks.

## Types of Prefix Lists

1. AWS-Managed Prefix Lists
   - Maintained by AWS and contain public CIDR blocks for AWS services like S3, DynamoDB, CloudFront, etc.
   - Examples:
     - `pl-63a5400a` → Amazon S3
     - `pl-81a92ef7` → Amazon DynamoDB
   - Useful for allowing access to AWS services without manually adding IPs.
2. Customer-Managed Prefix Lists
   - Created and managed by customers.
   - Useful for defining custom IP ranges that can be referenced in security rules.

## Use Cases

- Simplify security group and route table configurations.
- Reduce the need for frequent updates when AWS services change their IPs.
- Improve readability and manageability of network policies.

## How to Use Prefix Lists

- Route Tables: Add a prefix list as a destination to simplify routing rules.
- Security Groups: Use a prefix list as a source/destination in inbound/outbound rules.
- Network ACLs: Reference a prefix list in network ACL rules.
