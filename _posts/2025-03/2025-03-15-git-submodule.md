---
title: "Git Submodule"
published: true
tags: Git
---

A **Git submodule** is a way to include one Git repository inside another. This is useful when you want to manage dependencies or separate concerns in a modular fashion.

## 🔹 Why Use Submodules?

- To include external libraries or dependencies without merging their history into your main project.
- To keep separate repositories but still work with them as part of a larger project.
- To track a specific commit of an external project instead of the latest changes.

## 🔹 Basic Commands

### 1️⃣ Adding a Submodule

```sh
git submodule add <repository-url> <path>
```

This adds a submodule and records its exact commit in your project.

### 2️⃣ Cloning a Repository with Submodules

By default, `git clone` does **not** pull submodules. To clone a repo **with** submodules, use:

```sh
git clone --recursive <repository-url>
```

If you forgot `--recursive`, initialize submodules manually:

```sh
git submodule update --init --recursive
```

### 3️⃣ Updating a Submodule

To update the submodule to the latest commit from its repository:

```sh
cd <submodule-path>
git pull origin main  # Update the submodule to the latest commit
cd ..
git add <submodule-path>
git commit -m "Updated submodule"
```

### 4️⃣ Removing a Submodule

```sh
git submodule deinit -f <path>
git rm -f <path>
rm -rf .git/modules/<path>
```

This removes all traces of the submodule from your repo.

---

Let me know if you need more details! 🚀
