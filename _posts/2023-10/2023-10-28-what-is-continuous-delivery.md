---
title: "What is Continuous Delivery?"
published: true
tags: CI&CD
---

Continuous delivery is a software development practice where code changes are
automatically prepared for a release to production. A pillar of modern
application development, continuous delivery expands upon continuous
integration by deploying all code changes to a testing environment and/or a
production environment after the build stage. When properly implemented,
developers will always have a deployment-ready build artifact that has passed
through a standardized test process. 

Continuous delivery lets developers automate testing beyond just unit tests so
they can verify application updates across multiple dimensions before
deploying to customers. These tests may include UI testing, load testing,
integration testing, API reliability testing, etc. This helps developers more
thoroughly validate updates and pre-emptively discover issues. With the cloud,
it is easy and cost-effective to automate the creation and replication of
multiple environments for testing, which was previously difficult to do
on-premises.

## Continuous Delivery vs. Continuous Deployment

With continuous delivery, every code change is built, tested, and then pushed
to a non-production testing or staging environment. There can be multiple,
parallel test stages before a production deployment. The difference between
continuous delivery and continuous deployment is the presence of a manual
approval to update to production. With continuous deployment, production
happens automatically without explicit approval. 

Continuous delivery automates the entire software release process. Every
revision that is committed triggers an automated flow that builds, tests, and
then stages the update. The final decision to deploy to a live production
environment is triggered by the developer.

## Continuous Delivery Benefits

### Automate the Software Release Process

Continuous delivery lets your team automatically build, test, and prepare code
changes for release to production so that your software delivery is more
efficient and rapid.

### Improve Developer Productivity

These practices help your team be more productive by freeing developers from
manual tasks and encouraging behaviors that help reduce the number of errors
and bugs deployed to customers.

### Find and Address Bugs Quicker

Your team can discover and address bugs earlier before they grow into larger
problems later with more frequent and comprehensive testing. Continuous
delivery lets you more easily perform additional types of tests on your code
because the entire process has been automated.

### Deliver Updates Faster

Continuous delivery helps your team deliver updates to customers faster and
more frequently. When continuous delivery is implemented properly, you will
always have a deployment-ready build artifact that has passed through a
standardized test process.  

## Reference

- [https://aws.amazon.com/devops/continuous-delivery/](https://aws.amazon.com/devops/continuous-delivery/)