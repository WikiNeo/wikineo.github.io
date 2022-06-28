---
title: 'Design Pastebin'
published: true
tags: SystemDesign
---

## 1. What is Pastebin?

Pastebin like services enable user to store plain text or images over the
network and generate unique URLs to access the uploaded data.

## 2. Requirements and Goals of the System

### Functional Requirements:

1. Users should be able to upload or "paste" their data and get a unique URL
   to access it.
2. Users will only be able to upload text.
3. Data and links will expire after a specific timespan automatically; users
   should also be able to specify expiration time.
4. Users should optionally be able to pick a custom alias for their paste.

### Non-Functional Requirements:

1. The system should be highly reliable, any data uploaded should not be lost.
2. The system should be highly available. This is required because if our
   service is down, users will not be able to access their Pastes.
3. Users should be able to access their Pastes in real-time with minimum latency.
4. Paste links should not be guessable (not predictable).

### Extended Requirements:

1. Analytics
2. Our service should also be accessible through REST APIs by other services.

## 3. Some Design Considerations

- What should be the limit on the amount of text user can paste at a time?
- Should be impose size limits on custom URLs?

## 4. Capacity Estimation and Constraints

- Traffic estimates
- Storage estimates
- Bandwidth estimates
- Memory estimates

## 5. System APIs

```python
addPaste(api_dev_key, paste_data, custom_url=None, user_name=None, paste_name=None, expire_data=None)
getPaste(api_dev_key, api_paste_key)
deletePaste(api_dev_key, api_paste_key)
```

## 6. Database Design

## 7. High Level Design

## 8. Component Design