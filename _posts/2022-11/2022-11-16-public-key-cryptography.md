---
title: 'Public-Key Cryptography'
published: true
tags: Network
---

**Public-key cryptography**, or **asymmetric cryptography**, is the field of
cryptographic systems that use pairs of related keys. Each key pair consists
of a public key and a corresponding private key.[1][2] Key pairs are generated
with cryptographic algorithms based on mathematical problems termed one-way
functions. Security of **public-key** cryptography depends on keeping the **private
key secret**; the public key can be openly distributed without compromising
security.[3]

In a **public-key encryption** system, anyone with a public key can encrypt a
message, yielding a **ciphertext**, but only those who know the corresponding
private key can decrypt the ciphertext to obtain the original message.[4]

For example, a journalist can publish the public key of an encryption key pair
on a web site so that sources can send secret messages to the news
organization in ciphertext. Only the journalist who knows the corresponding
private key can decrypt the ciphertexts to obtain the sources' messages—an
eavesdropper reading email on its way to the journalist can't decrypt the
ciphertexts. However, public-key encryption doesn't conceal metadata like what
computer a source used to send a message, when they sent it, or how long it
is. Public-key encryption on its own also doesn't tell the recipient anything
about who sent a message—it just conceals the content of a message in a
ciphertext that can only be decrypted with the private key.

In a digital signature system, a sender can use a private key together with a
message to create a **signature**. Anyone with the corresponding public key can
verify whether the signature matches the message, but a forger who doesn't
know the private key can't find any message/signature pair that will pass
verification with the public key.[5][6]

For example, a software publisher can create a signature key pair and include
the public key in software installed on computers. Later, the publisher can
distribute an update to the software signed using the private key, and any
computer receiving an update can confirm it is genuine by verifying the
signature using the public key. As long as the software publisher keeps the
private key secret, even if a forger can distribute malicious updates to
computers, they can't convince the computers that any malicious updates are
genuine.

Public key algorithms are fundamental security primitives in modern
cryptosystems, including applications and protocols which offer assurance of
the confidentiality, authenticity and non-repudiability of electronic
communications and data storage. They underpin numerous Internet standards,
such as Transport Layer Security (TLS), SSH, S/MIME and PGP. Some public key
algorithms provide key distribution and secrecy (e.g., Diffie–Hellman key
exchange), some provide digital signatures (e.g., Digital Signature
Algorithm), and some provide both (e.g., RSA). Compared to symmetric
encryption, asymmetric encryption is rather slower than good symmetric
encryption, too slow for many purposes.[7] Today's cryptosystems (such as TLS,
Secure Shell) use both symmetric encryption and asymmetric encryption, often
by using asymmetric encryption to securely exchange a secret key which is then
used for symmetric encryption.

## Reference

- [https://en.wikipedia.org/wiki/Public-key_cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)