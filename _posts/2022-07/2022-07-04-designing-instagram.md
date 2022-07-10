---
title: 'Designing Instagram'
published: false
tags: SystemDesign
---

## 1. What is Instagram?

Instagram is a social networking service that enables its users to upload and
share their photos and videos with other users. 

## 2. Requirements and Goals of the System

### Functional Requirements

1. Users should be able to upload/download/view photos.
2. Users can perform searches based on photo/video titles.
3. Users can follow other users.
4. The system should generate and display a user's News Feed consisting of top
   photos from all the people the user follows.

### Non-functional Requirements

1. Our service needs to be highly available.
2. The acceptable latency of the system is 200ms for News Feed generation.
3. Consistency can take a hit (in the interest of availability) if a user
   doesn't see a photo for a while; it should be fine
4. The system should be highly reliable; any uploaded photo or video should
   never be lost

## 3. Some Design COnsiderations

The system would be read-heavy, so we will focus on building a system that can
retrieve photo quickly.

1. Practically, users can upload as many phots as they like; therefore,
   efficient management of storage should be a crucial factor in designing
   this system.
2. Low latency is expected while viewing photos.
3. Data should be 100% reliable. If a user uploads a photo, the system will
   guarantee that it will never be lost.

## 4. 