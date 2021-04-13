---
title: 'Fix MacOS WIFI slow issue'
published: true
tags: MacOS
---

```shell
/Library/Preferences/SystemConfiguration

Delete

- com.apple.airport.preferences.plist
- com.apple.network.eapolclient.configuration.plist
- com.apple.wifi.message-tracer.plist
- NetworkInterfaces.plist
- preferences.plist

Reboot
```

## Reference

- [https://recoverit.wondershare.com/mac-problems/fix-slow-wifi-mac-sierra-upgrade.html#:~:text=One%20of%20the%20first%20solutions,MacBook%20and%20try%20to%20reconnect.](https://recoverit.wondershare.com/mac-problems/fix-slow-wifi-mac-sierra-upgrade.html#:~:text=One%20of%20the%20first%20solutions,MacBook%20and%20try%20to%20reconnect.)