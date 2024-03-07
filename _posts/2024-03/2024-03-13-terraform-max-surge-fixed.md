---
title: "Terraform max_surge_fixed"
published: true
tags: Terraform
---

## google_compute_region_instance_group_manager

The Google Compute Engine Regional Instance Group Manager API creates and
manages pools of homogeneous Compute Engine virtual machine instances from a
common instance template.

- `update_policy` - (Optional) The update policy for this managed instance
  group.
  - `max_surge_fixed` - (Optional), The maximum number of instances that can be created above the specified targetSize during the update process. Conflicts with `max_surge_percent`. It has to be either 0 or at least equal to the number of zones. If fixed values are used, at least one of `max_unavailable_fixed` or `max_surge_fixed` must be greater than 0.

## Reference

- [https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_region_instance_group_manager)