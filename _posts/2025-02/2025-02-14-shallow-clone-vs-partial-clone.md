---
title: "Shallow Clone vs. Partial Clone"
published: true
tags: Git
---

## Shallow Clone

- **Definition**: A shallow clone only fetches a limited history of commits.
- **Use Case**: When you don’t need the entire commit history of a repository. Useful for saving time and disk space.
- How to Create:
  ```shell
  git clone --depth <depth> <repo-url>
  ```
  - `--depth 1`: Only fetch the latest commit.
  - Shallow clones can significantly reduce the size of the clone, but they might not support certain operations like checking out older commits or rebasing.
- Example:
  ```shell
  git clone --depth 1 https://github.com/example/repo.git
  ```
  - This fetches only the latest commit for each branch.

## Partial Clone

- **Definition**: A partial clone skips fetching large objects (e.g., binaries) until they are actually needed.
- **Use Case**: When the repository contains large files or many objects you don’t need right away (e.g., in monorepos or projects with large media assets). Saves disk space while allowing you to work with the repo.
- **How to Create**:
  ```shell
  git clone --filter=<filter> <repo-url>
  ```
  - Common filters:
    - `--filter=blob:none`: Skips all blobs (file contents) and only downloads them when accessed.
- Example:
  ```shell
  git clone --filter=blob:none https://github.com/example/repo.git
  ```
  - This fetches only the repository structure and metadata, downloading file content on demand.

## Key Differences

| Aspect           | Shallow Clone                      | Partial Clone                         |
| ---------------- | ---------------------------------- | ------------------------------------- |
| Focus            | Limited commit history             | Skipping large blobs                  |
| Speed            | Faster for small history clones    | Faster for repos with large objects   |
| Dis Space        | Save space by reducing hisotry     | Save space by delaying blob downloads |
| Operations Limit | Some opraions may not be supported | All operations are supported          |
