---
title: 'python-pyqt5 error upgrading'
published: true
tags: ArchLinux
---

## Error Log

```shell
error: failed to commit transaction (conflicting files)
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtBluetooth.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtCore.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtDBus.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtDesigner.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtGui.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtHelp.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtLocation.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtMultimedia.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtMultimediaWidgets.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtNetwork.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtNfc.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtOpenGL.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtPositioning.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtPrintSupport.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtQml.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtQuick.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtQuick3D.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtQuickWidgets.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtRemoteObjects.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtSensors.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtSerialPort.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtSql.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtSvg.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtTest.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtTextToSpeech.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtWebChannel.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtWebSockets.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtWidgets.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtX11Extras.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtXml.pyi exists in filesystem
python-pyqt5: /usr/lib/python3.10/site-packages/PyQt5/QtXmlPatterns.pyi exists in filesystem
Errors occurred, no packages were upgraded.
```

## Solution

Overwrite the `.pyi` files with `pacman`

```shell
 sudo pacman -S --overwrite "*.pyi" python-pyqt5  
```

## Reference

- [https://bbs.archlinux.org/viewtopic.php?id=243795](https://bbs.archlinux.org/viewtopic.php?id=243795)