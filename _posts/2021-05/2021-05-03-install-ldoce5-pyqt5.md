---
title: 'Install LDOCE5 Viewer on Ubuntu'
published: true
tags: Ubuntu
---

```shell
sudo apt-get install git make python pyqt5-dev-tools python3-pyqt5 \
python3-pyqt5.qtwebkit python3-lxml python3-whoosh  qtgstreamer-plugins-qt5

git clone git@github.com:mintwzy/ldoce5viewer-pyqt5.git
make build
sudo make install
```