---
title: 'SQL vs. NoSQL'
published: true
tags: SystemDesign
---

Relational databases are structured and have a predefined schemas like phone
books that store phone numbers and addresses. Non-relational databases are
unstructured, distributed, and have a dynamic schema like file folders that
hold everything from a person's address and phone number to their Facebook
'likes' and online shopping preferences.

## SQL

Relational databases store data in rows and columns. Each row contains all the
information about one entity and each column contains all the separate data
points.

## NoSQL

- Key-Value Stores:
  - Data is stored in an array of key-value paris. The 'key' ia an attribute
    name which is linked to a 'value'. Well-known key-value stores include
    Redis, Dynamo.
- Document Databases:
  - Data is stored in documents and these documents are grouped together in
    collections. Each document can have an entirely different structure.
    MongoDB.
- Wide-Column Databases:
  - Instead of 'tables', in columnar databases we have column families, which
    are containers for rows. Unlike relational databases, we don't need to
    know all the columns upfront and each row doesn't have to have the same
    number of columns. Columnar databases are best suited for analyzing large
    datasets - Cassandra and HBase
- Graph Database
  - These databases are used to store data whose relations are best
    represented in a graph. Data is saved in graph structures with nodes
    (entities) , properties (information about the entities), and lines
    (connections between the entities). Neo4j and InfiniteGraph.

## High Level Differences between SQL and NoSQL

- Storage
  - SQL stores data in tables where each row represents an entity and each
    column represents a data point about that entity
  - NoSQL database have different data storage models. The main ones are
    key-value, document, graph, and columnar.
- Schema
  - In SQL, each record conforms to a fixed schema, meaning the columns must
    be decided and chose before data entry and each row must have data for
    each column.
  - In NoSQL, schemas are dynamic. Columns can be added on the fly and each
    'row' (or equivalent) doesn't have to contain for each 'column'
- Querying
  - SQL data bases use SQL. In a NoSQL database, queries are focused on a
    collection of documents. Sometimes it is also called UnQL (Unstructured
    Query Language)
- Scalability
  - SQL databases are vertically scalable.
  - NoSQL databases are horizontally scalable
- Reliability or ACID Compliancy (Atomicity, Consistency, Isolation,
  Durability)
  - The vast majority of relational databases are ACID compliant.
  - Most of the NoSQL solutions sacrifice ACID compliance for performance and scalability.

## SQL vs. NoSQL - Which one to use?

### Reasons to use SQL database

1. We need to enure ACID compliance.
2. Your data is structured and unchanging.

### Reasons to use NoSQL database

1. Storing large volumes of data that often have little to no structure.
2. Making the most of cloud computing and storage.
3. Rapid development.