---
title: 'BitTorrent tracker'
published: true
tags: Network
---

A BitTorrent tracker is a special type of server that assists in the
communication between peers using the BitTorrent protocol.

In peer-to-peer file sharing, a software client on an end-user PC requests a
file, and portions of the requested file residing on peer machines are sent to
the client, and then reassembled into a full copy of the requested file. The
"tracker" server keeps track of where file copies reside on peer machines,
which ones are available at time of the client request, and helps coordinate
efficient transmission and reassembly of the copied file. Clients that have
already begun downloading a file communicate with the tracker periodically to
negotiate faster file transfer with new peers, and provide network performance
statistics; however, after the initial peer-to-peer file download is started,
peer-to-peer communication can continue without the connection to a tracker.

Since the creation of the distributed hash table (DHT) method for
"trackerless" torrents, BitTorrent trackers have largely become
redundant; however, they are still often included with
torrents to improve the speed of peer discovery.

## Reference

- [https://en.wikipedia.org/wiki/BitTorrent_tracker](https://en.wikipedia.org/wiki/BitTorrent_tracker)