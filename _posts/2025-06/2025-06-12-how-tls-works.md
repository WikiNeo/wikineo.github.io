---
title: "How TLS works"
published: true
tags: Network
---

TLS (Transport Layer Security) is a cryptographic protocol that provides **secure communication** over a computer network. It is widely used in HTTPS, email, messaging, and other protocols. Here's a detailed breakdown of how TLS works, from the moment a connection is initiated to the end of the secure session.

---

## 🔐 Goals of TLS

TLS provides four main properties:

1. **Confidentiality** – Data is encrypted to prevent eavesdropping.
2. **Integrity** – Ensures data is not modified in transit.
3. **Authentication** – Confirms the identity of one or both parties.
4. **Forward Secrecy** (optional) – Ensures past sessions remain secure even if long-term keys are compromised.

---

## 🧾 TLS in Action: The Handshake

### Step 1: **Client Hello**

The client (e.g., browser) initiates a secure connection by sending a "ClientHello" message that includes:

- Supported **TLS versions**
- Supported **cipher suites**
- A **random number** (used later for key generation)
- **Extensions**, including the server name (SNI)

### Step 2: **Server Hello**

The server responds with:

- The **chosen TLS version**
- The selected **cipher suite**
- Its own **random number**
- Its **digital certificate** (usually X.509, contains public key and identity info)
- Optionally, **key exchange parameters**

> The digital certificate is signed by a **Certificate Authority (CA)** that the client trusts.

### Step 3: **Authentication and Key Exchange**

Now the client must verify the server's identity:

- The client checks the certificate’s validity (expiry, domain match, CA signature)
- If valid, the client proceeds to **key exchange**

The exact method depends on the chosen **key exchange algorithm**:

- In **RSA-based TLS**, the client generates a "pre-master secret", encrypts it with the server's public key (from the certificate), and sends it to the server.
- In **Diffie-Hellman or ECDHE** (modern, preferred), both sides agree on a shared secret using ephemeral keys (provides forward secrecy).

### Step 4: **Session Key Generation**

Both sides now derive the **session key** from:

- The **pre-master secret** (or Diffie-Hellman result)
- The **client and server random numbers**

This key is used for **symmetric encryption**, because it’s much faster than public-key cryptography.

### Step 5: **Finished Messages**

- Both client and server send a "Finished" message encrypted using the derived session key.
- These messages confirm that future communications are encrypted and that the handshake succeeded.

---

## 🔒 Secure Data Transfer

Now that both sides share a session key:

- All data is encrypted using a **symmetric cipher** (e.g., AES)
- A **MAC (Message Authentication Code)** or **AEAD (Authenticated Encryption with Associated Data)** ensures data integrity

---

## 📤 Closing the Connection

When either side wants to close:

- They send a "close_notify" alert
- Both sides discard the session key

---

## 🧠 Summary Diagram

```
Client                         Server
  |----- ClientHello -------->|
  |                           |
  |<------ ServerHello -------|
  |<----- Certificate --------|
  |                           |
  |--- (Key Exchange) ------->|
  |                           |
  |--- Finished (encrypted)-->|
  |<-- Finished (encrypted) --|
  |                           |
  |<==== Secure Data ========>|
  |                           |
  |------ close_notify ------>|
```

---

## ✅ TLS Versions

- **TLS 1.0 / 1.1**: Obsolete, insecure
- **TLS 1.2**: Widely used, secure with modern settings
- **TLS 1.3**: Simplified, faster, more secure (no RSA key exchange, removes obsolete features)

---

## 📘 Real World Example (HTTPS)

1. You type `https://example.com`
2. Your browser starts a TLS handshake
3. Verifies the server’s certificate
4. Negotiates a secure connection
5. Then HTTP data is transmitted securely on top of TLS

---
