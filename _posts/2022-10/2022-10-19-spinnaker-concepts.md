---
title: 'Spinnaker Concepts'
published: true
tags: CI/CD
---

Spinnaker is an open-source, multi-cloud continuous delivery platform that
helps you release software changes with high velocity and confidence.

## Application management

You use Spinnaker’s application management features to view and manage your cloud resources.

Modern tech organizations operate collections of services—sometimes referred to as “applications” or “microservices.” A Spinnaker application models this concept.

Applications , clusters , and server groups are the key concepts Spinnaker
uses to describe your services. Load balancers and firewalls describe how your
services are exposed to users.

### Application

An application in Spinnaker is a collection of clusters, which in turn are collections of server groups. The application also includes firewalls and load balancers.

An application represents the service which you are going to deploy using Spinnaker, all configuration for that service, and all the infrastructure on which it will run.

You will typically create a different application for each service, though Spinnaker does not enforce that.

### Cluster

You can define Clusters, which are logical groupings of Server Groups in Spinnaker.

- **Note**: cluster, here, does not map to a Kubernetes cluster. It’s merely a collection of Server Groups, irrespective of any Kubernetes clusters that might be included in your underlying architecture.

## Reference

- [https://spinnaker.io/docs/concepts/](https://spinnaker.io/docs/concepts/)