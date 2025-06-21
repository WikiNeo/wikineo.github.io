---
title: "Third Normal Form (3NF)"
published: true
tags: Database
---

**Third Normal Form (3NF)** is a database normalization standard used to reduce redundancy and ensure data integrity. A table is in **3NF** if:

1. It is in **Second Normal Form (2NF)**, and
2. **All non-prime attributes are non-transitively dependent on the primary key**.

### Terms

- **Non-prime attribute**: An attribute that is **not** part of any candidate key.
- **Transitive dependency**: A situation where attribute A depends on B, and B depends on C, so A depends on C indirectly.

---

### Example

#### Not in 3NF

| StudentID | Name  | Department | DepartmentHead |
| --------- | ----- | ---------- | -------------- |
| 1         | Alice | CS         | Dr. Smith      |
| 2         | Bob   | EE         | Dr. Jones      |

Here:

- `StudentID → Department`
- `Department → DepartmentHead`

So, `StudentID → DepartmentHead` is a **transitive dependency** via `Department`.

---

#### In 3NF

Split into two tables:

**Students**

| StudentID | Name  | Department |
| --------- | ----- | ---------- |
| 1         | Alice | CS         |
| 2         | Bob   | EE         |

**Departments**

| Department | DepartmentHead |
| ---------- | -------------- |
| CS         | Dr. Smith      |
| EE         | Dr. Jones      |

Now, all non-prime attributes depend directly on the primary key, not transitively.

---
