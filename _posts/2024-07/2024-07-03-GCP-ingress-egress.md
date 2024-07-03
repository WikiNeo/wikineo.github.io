---
title: GCP ingress and egress
published: true
tags: GCP
---

The definitions of ingress and egress are independent of the operation being
invoked on the resource. Thus, the definitions refer to the direction of the
request and not to the direction of data movement.

- Ingress: Refers to any access by an API client from outside the service
  perimeter to resources within a service perimeter. Example:

  - A Cloud Storage client outside a service perimeter calling Cloud Storage
    read, write, or copy operations on a Cloud Storage resource within the
    perimeter.

- Egress Refers to any access that involves an API client or resources within
  the service perimeter and resources outside a service perimeter. Examples:

  - A Compute Engine client within a service perimeter calling a Compute Engine
    create operation where the image resource is outside the perimeter.
  - A Cloud Storage client – within or outside the perimeter – that calls a copy
    command where one bucket is within the perimeter and the other bucket is
    outside it.

## Reference

- [https://cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#definition-ingress-egress](https://cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#definition-ingress-egress)
