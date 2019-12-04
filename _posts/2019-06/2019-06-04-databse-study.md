---
title:  "Database Study"
published: true
categories: tech
---

#### Books

##### Database System Concepts

- Book worth reading

#### Notes

##### Problems with keeping organizational information in a file-processing system

- **Data redundancy and inconsistency.** Same information may be duplicated in several files. Various copies
of the same data may no longer agree.

- **Difficulty in accessing data.** The conventional file-processing environment do not allow needed data to
be retrieved in a convenient and efficient manner.

- **Integrity problems.** The data values stored in the database must satisfy certain types of consistency
constraints. Some value may never fall below zero.

- **Atomicity problem.** Some operation must be atomic - it must happen in its entirety or not at all.

- **Concurrent-access anomalies.** Multiple clients update data at the same time.

- **Security problem.** Not every user of the database system should be able to access all the data.
