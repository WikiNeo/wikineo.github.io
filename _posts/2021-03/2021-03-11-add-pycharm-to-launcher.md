---
title: 'Add PyCharm to launcher in Ubuntu'
published: true
tags: Linux
---

Create a launcher in text editor

```
[Desktop Entry]
Version=1.0
Type=Application
Name=PyCharm
Icon=/opt/pycharm-2017.1.1/bin/pycharm.png
Exec="/opt/pycharm-2017.1.1/bin/pycharm.sh" %f
Comment=The Drive to Develop
Categories=Development;IDE;
Terminal=false
StartupWMClass=jetbrains-pycharm
```

Save it to

```
/home/yourname/.local/share/applications/appname.desktop

OR

/usr/share/applications/appname.desktop
```

## Reference

- [How can I set up PyCharm to launch from the Launcher?](https://askubuntu.com/questions/391439/how-can-i-set-up-pycharm-to-launch-from-the-launcher/909246#909246)