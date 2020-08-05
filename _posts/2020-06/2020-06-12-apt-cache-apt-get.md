---
title: "apt-cache & apt-get"
published: true
tags: Ubuntu
---

## List all available packages

```bash
apt-cache pkgnames

esseract-ocr-epo
pipenightdreams
mumudvb
tbb-examples
libsvm-java
libmrpt-hmtslam0.9
libboost-timer1.50-dev
kcm-touchpad
g++-4.5-multilib
...
```

## Find out package name and description of software

```bash
apt-cache search vstfpd

vsftpd - lightweight, efficient FTP server written for security
ccze - A robust, modular log coloriser
ftpd - File Transfer Protocol (FTP) server
yasat - simple stupid audit tool
```

## Check package information

```bash
apt-cache show netcat

Package: netcat
Priority: optional
Section: universe/net
Installed-Size: 30
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Ruben Molina <rmolina@udea.edu.co>
Architecture: all
Version: 1.10-40
Depends: netcat-traditional (>= 1.10-39)
Filename: pool/universe/n/netcat/netcat_1.10-40_all.deb
Size: 3340
MD5sum: 37c303f02b260481fa4fc9fb8b2c1004
SHA1: 0371a3950d6967480985aa014fbb6fb898bcea3a
SHA256: eeecb4c93f03f455d2c3f57b0a1e83b54dbeced0918ae563784e86a37bcc16c9
Description-en: TCP/IP swiss army knife -- transitional package
 This is a "dummy" package that depends on lenny's default version of
 netcat, to ease upgrades. It may be safely removed.
Description-md5: 1353f8c1d079348417c2180319bdde09
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Origin: Ubuntu
```

## Check dependencies for specific packages

```bash
apt-cache showpkg vsftpd

Package: vsftpd
Versions: 
2.3.5-3ubuntu1 (/var/lib/apt/lists/in.archive.ubuntu.com_ubuntu_dists_quantal_main_binary-i386_Packages)
 Description Language: 
                 File: /var/lib/apt/lists/in.archive.ubuntu.com_ubuntu_dists_quantal_main_binary-i386_Packages
                  MD5: 81386f72ac91a5ea48f8db0b023f3f9b
 Description Language: en
                 File: /var/lib/apt/lists/in.archive.ubuntu.com_ubuntu_dists_quantal_main_i18n_Translation-en
                  MD5: 81386f72ac91a5ea48f8db0b023f3f9b

Reverse Depends: 
  ubumirror,vsftpd
  harden-servers,vsftpd
Dependencies: 
2.3.5-3ubuntu1 - debconf (18 0.5) debconf-2.0 (0 (null)) upstart-job (0 (null)) libc6 (2 2.15) libcap2 (2 2.10) libpam0g (2 0.99.7.1) libssl1.0.0 (2 1.0.0) libwrap0 (2 7.6-4~) adduser (0 (null)) libpam-modules (0 (null)) netbase (0 (null)) logrotate (0 (null)) ftp-server (0 (null)) ftp-server (0 (null)) 
Provides: 
2.3.5-3ubuntu1 - ftp-server 
Reverse Provides:
```

## Check statistics of cache

```bash
apt-cache stats

Total package names: 51868 (1,037 k)
Total package structures: 51868 (2,490 k)
  Normal packages: 39505
  Pure virtual packages: 602
  Single virtual packages: 3819
  Mixed virtual packages: 1052
  Missing: 6890
Total distinct versions: 43015 (2,753 k)
Total distinct descriptions: 81048 (1,945 k)
Total dependencies: 252299 (7,064 k)
Total ver/file relations: 45567 (729 k)
Total Desc/File relations: 81048 (1,297 k)
Total Provides mappings: 8228 (165 k)
Total globbed strings: 286 (3,518 )
Total dependency version space: 1,145 k
Total slack space: 62.6 k
Total space accounted for: 13.3 M
```

## Update system package

```bash
sudo apt-get update

[sudo] password for tecmint: 
Ign http://security.ubuntu.com quantal-security InRelease                      
Get:1 http://security.ubuntu.com quantal-security Release.gpg [933 B]          
Get:2 http://security.ubuntu.com quantal-security Release [49.6 kB]            
Ign http://in.archive.ubuntu.com quantal InRelease                             
Ign http://in.archive.ubuntu.com quantal-updates InRelease                     
Get:3 http://repo.varnish-cache.org precise InRelease [13.7 kB]                
Ign http://in.archive.ubuntu.com quantal-backports InRelease                   
Hit http://in.archive.ubuntu.com quantal Release.gpg                           
Get:4 http://security.ubuntu.com quantal-security/main Sources [34.8 kB]       
Get:5 http://in.archive.ubuntu.com quantal-updates Release.gpg [933 B]         
...
```

## Upgrade software packages

```bash
sudo apt-get upgrade

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages have been kept back:
  linux-headers-generic linux-image-generic wine1.5 wine1.5-i386
The following packages will be upgraded:
  activity-log-manager-common activity-log-manager-control-center adium-theme-ubuntu alacarte
  alsa-base app-install-data-partner appmenu-gtk appmenu-gtk3 apport apport-gtk apt
  apt-transport-https apt-utils aptdaemon aptdaemon-data at-spi2-core bamfdaemon base-files bind9-host
   ...
```

## Install or upgrade sepcific packages

```bash
sudo apt-get install netcat

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following extra packages will be installed:
  netcat-traditional
The following NEW packages will be installed:
  netcat netcat-traditional
0 upgraded, 2 newly installed, 0 to remove and 328 not upgraded.
Need to get 67.1 kB of archives.
After this operation, 186 kB of additional disk space will be used.
Do you want to continue [Y/n]? y
Get:1 http://in.archive.ubuntu.com/ubuntu/ quantal/universe netcat-traditional i386 1.10-40 [63.8 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu/ quantal/universe netcat all 1.10-40 [3,340 B]
Fetched 67.1 kB in 1s (37.5 kB/s)
Selecting previously unselected package netcat-traditional.
(Reading database ... 216118 files and directories currently installed.)
Unpacking netcat-traditional (from .../netcat-traditional_1.10-40_i386.deb) ...
Selecting previously unselected package netcat.
Unpacking netcat (from .../netcat_1.10-40_all.deb) ...
Processing triggers for man-db ...
Setting up netcat-traditional (1.10-40) ...
Setting up netcat (1.10-40) ...
```

## Install multiple packages

```bash
sudo apt-get install nethogs goaccess

Reading package lists... Done
Building dependency tree       
Reading state information... Done
goaccess is already the newest version.
nethogs is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 328 not upgraded.
```

## Install several packages using wildcard

```bash
sudo apt-get install '*name*'
```

## Install packages without upgrading

```bash
sudo apt-get install packageName --no-upgrade

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Skipping vsftpd, it is already installed and upgrade is not set.
0 upgraded, 0 newly installed, 0 to remove and 328 not upgraded.
```

## Upgrade only specific packages

```bash
sudo apt-get install packgeName --only-upgrade

Reading package lists... Done
Building dependency tree       
Reading state information... Done
vsftpd is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 328 not upgraded.
```

## Install specific package version

```bash
sudo apt-get install vsftpd=2.3.5-3ubuntu1

Reading package lists... Done
Building dependency tree       
Reading state information... Done
vsftpd is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 328 not upgraded.
```

## Remove packages without configuration

```bash
sudo apt-get remove vsftpd

[sudo] password for tecmint: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  vsftpd
0 upgraded, 0 newly installed, 1 to remove and 328 not upgraded.
After this operation, 364 kB disk space will be freed.
Do you want to continue [Y/n]? y
(Reading database ... 216156 files and directories currently installed.)
Removing vsftpd ...
vsftpd stop/waiting
Processing triggers for ureadahead ...
Processing triggers for man-db ...
```

## Completely remove packages

```bash
sudo apt-get purge vsftpd

Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  vsftpd*
0 upgraded, 0 newly installed, 1 to remove and 328 not upgraded.
After this operation, 0 B of additional disk space will be used.
Do you want to continue [Y/n]? y
(Reading database ... 216107 files and directories currently installed.)
Removing vsftpd ...
Purging configuration files for vsftpd ...
Processing triggers for ureadahead ...
```

## Clean up disk space

```bash
sudo apt-get clean
```

## Download only source code of package

```bash
sudo apt-get --download-only source vsftpd

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Need to get 220 kB of source archives.
Get:1 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (dsc) [1,883 B]
Get:2 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (tar) [188 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (diff) [30.5 kB]
Fetched 220 kB in 4s (49.1 kB/s)
Download complete and in download only mode
```

## Download and unpack a package

```bash
sudo apt-get source vsftpd

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Need to get 220 kB of source archives.
Get:1 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (dsc) [1,883 B]
Get:2 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (tar) [188 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu/ quantal/main vsftpd 2.3.5-3ubuntu1 (diff) [30.5 kB]
Fetched 220 kB in 1s (112 kB/s)  
gpgv: Signature made Thursday 24 May 2012 02:35:09 AM IST using RSA key ID 2C48EE4E
gpgv: Can't check signature: public key not found
dpkg-source: warning: failed to verify signature on ./vsftpd_2.3.5-3ubuntu1.dsc
dpkg-source: info: extracting vsftpd in vsftpd-2.3.5
dpkg-source: info: unpacking vsftpd_2.3.5.orig.tar.gz
dpkg-source: info: unpacking vsftpd_2.3.5-3ubuntu1.debian.tar.gz
dpkg-source: info: applying 01-builddefs.patch
dpkg-source: info: applying 02-config.patch
dpkg-source: info: applying 03-db-doc.patch
dpkg-source: info: applying 04-link-local.patch
dpkg-source: info: applying 05-whitespaces.patch
dpkg-source: info: applying 06-greedy.patch
dpkg-source: info: applying 07-utf8.patch
dpkg-source: info: applying 08-manpage.patch
dpkg-source: info: applying 09-s390.patch
dpkg-source: info: applying 10-remote-dos.patch
dpkg-source: info: applying 11-alpha.patch
dpkg-source: info: applying 09-disable-anonymous.patch
dpkg-source: info: applying 12-ubuntu-use-snakeoil-ssl.patch
```

## Download, unpack and compile a package

```bash
sudo apt-get --complie source goaccess

[sudo] password for tecmint: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Need to get 130 kB of source archives.
Get:1 http://in.archive.ubuntu.com/ubuntu/ quantal/universe goaccess 1:0.5-1 (dsc) [1,120 B]
Get:2 http://in.archive.ubuntu.com/ubuntu/ quantal/universe goaccess 1:0.5-1 (tar) [127 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu/ quantal/universe goaccess 1:0.5-1 (diff) [2,075 B]
Fetched 130 kB in 1s (68.0 kB/s)
gpgv: Signature made Tuesday 26 June 2012 09:38:24 AM IST using DSA key ID A9FD4821
gpgv: Can't check signature: public key not found
dpkg-source: warning: failed to verify signature on ./goaccess_0.5-1.dsc
dpkg-source: info: extracting goaccess in goaccess-0.5
dpkg-source: info: unpacking goaccess_0.5.orig.tar.gz
dpkg-source: info: unpacking goaccess_0.5-1.debian.tar.gz
dpkg-buildpackage: source package goaccess
dpkg-buildpackage: source version 1:0.5-1
dpkg-buildpackage: source changed by Chris Taylor <ctaylor@debian.org>
dpkg-buildpackage: host architecture i386
 dpkg-source --before-build goaccess-0.5
dpkg-checkbuilddeps: Unmet build dependencies: debhelper (>= 9) autotools-dev libncurses5-dev libglib2.0-dev libgeoip-dev autoconf
dpkg-buildpackage: warning: build dependencies/conflicts unsatisfied; aborting
dpkg-buildpackage: warning: (Use -d flag to override.)
...
```

## Download a package without installing

```bash
sudo apt-get download nethogs

Get:1 Downloading nethogs 0.8.0-1 [27.1 kB]
Fetched 27.1 kB in 3s (7,506 B/s)
```

## Check change log of a package

```bash
sudo apt-get changelog csftpd

vsftpd (2.3.5-3ubuntu1) quantal; urgency=low

  * Merge from Debian testing (LP: #1003644).  Remaining changes:
    + debian/vsftpd.upstart: migrate vsftpd to upstart.
    + Add apport hook (LP: #513978):
      - debian/vsftpd.apport: Added.
      - debian/control: Build-depends on dh-apport.
      - debian/rules: Add --with apport.
    + Add debian/watch file.
    + debian/patches/09-disable-anonymous.patch: Disable anonymous login
      by default. (LP: #528860)
  * debian/patches/12-ubuntu-us-snakeoil-ssl.patch: Use snakeoil SSL
    certificates and key.

 -- Andres Rodriguez <andreserl@ubuntu.com>  Wed, 23 May 2012 16:59:36 -0400
...
``

## Check broken dependencies

```bash
sudo apt-get check

[sudo] password for tecmint: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
```

## Search and build dependencies

```bash
sudo apt-get build-dep netcat

The following NEW packages will be installed:
  debhelper dh-apparmor html2text po-debconf quilt
0 upgraded, 5 newly installed, 0 to remove and 328 not upgraded.
Need to get 1,219 kB of archives.
After this operation, 2,592 kB of additional disk space will be used.
Do you want to continue [Y/n]? y
Get:1 http://in.archive.ubuntu.com/ubuntu/ quantal/main html2text i386 1.3.2a-15build1 [91.4 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu/ quantal/main po-debconf all 1.0.16+nmu2ubuntu1 [210 kB]
Get:3 http://in.archive.ubuntu.com/ubuntu/ quantal/main dh-apparmor all 2.8.0-0ubuntu5 [9,846 B]
Get:4 http://in.archive.ubuntu.com/ubuntu/ quantal/main debhelper all 9.20120608ubuntu1 [623 kB]
Get:5 http://in.archive.ubuntu.com/ubuntu/ quantal/main quilt all 0.60-2 [285 kB]
Fetched 1,219 kB in 4s (285 kB/s)
...
```

## Auto clean apt-get cache

```bash
sudo apt-get autoclean

Reading package lists... Done
Building dependency tree       
Reading state information... Done
```

## Auto remove installed packages

```bash
sudo apt-get autoremove vsftpd

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Package 'vsftpd' is not installed, so not removed
0 upgraded, 0 newly installed, 0 to remove and 328 not upgraded.
```

## References

- [https://www.tecmint.com/useful-basic-commands-of-apt-get-and-apt-cache-for-package-management/](https://www.tecmint.com/useful-basic-commands-of-apt-get-and-apt-cache-for-package-management/)