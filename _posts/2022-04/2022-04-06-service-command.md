---
title: 'Service Command'
published: true
tags: Linux
---

The `service` command is a wrapper script that allows system administrators to
start, stop, and check the status of services without worrying too much about
the actual init system being used. Prior to systemd's introduction, it was a
wrapper for `/etc/init.d` scripts and Upstart's `initctl` command, and now it is a
wrapper for these two and `systemctl` as well.

## It checks for Upstart:

```bash
# Operate against system upstart, not session
unset UPSTART_SESSION
if [ -r "/etc/init/${SERVICE}.conf" ] && which initctl >/dev/null \
   && initctl version 2>/dev/null | grep -q upstart \
   && initctl status ${SERVICE} 2>/dev/null 1>/dev/null
then
   # Upstart configuration exists for this job and we're running on upstart
```

## If that doesn't work, it looks for systemd:

```bash
if [ -d /run/systemd/system ]; then
   is_systemd=1
fi

...

# When this machine is running systemd, standard service calls are turned into
# systemctl calls.
if [ -n "$is_systemd" ]
then
```

## And if that fails as well, it falls back to System V /etc/init.d scripts:

```bash
run_via_sysvinit() {
   # Otherwise, use the traditional sysvinit
   if [ -x "${SERVICEDIR}/${SERVICE}" ]; then
      exec env -i LANG="$LANG" LANGUAGE="$LANGUAGE" LC_CTYPE="$LC_CTYPE" LC_NUMERIC="$LC_NUMERIC" LC_TIME="$LC_TIME" LC_COLLATE="$LC_COLLATE" LC_MONETARY="$LC_MONETARY" LC_MESSAGES="$LC_MESSAGES" LC_PAPER="$LC_PAPER" LC_NAME="$LC_NAME" LC_ADDRESS="$LC_ADDRESS" LC_TELEPHONE="$LC_TELEPHONE" LC_MEASUREMENT="$LC_MEASUREMENT" LC_IDENTIFICATION="$LC_IDENTIFICATION" LC_ALL="$LC_ALL" PATH="$PATH" TERM="$TERM" "$SERVICEDIR/$SERVICE" ${ACTION} ${OPTIONS}
   else
      echo "${SERVICE}: unrecognized service" >&2
      exit 1
   fi
}

...
run_via_sysvinit
```

Since the `service` command is a fairly simple wrapper, it only supports a limited subset of actions compared to what the actual init system might provide.

For portability over various versions of Ubuntu, users can reliably use the
`service` command to start, stop, restart or examine the status of a service.
For more complex tasks, however, the actual command being used, be that
`initctl` or `systemctl` or the `/etc/init.d` script might have to be used directly.

Further, being a wrapper, the `service` script in some cases also does more than
the direct equivalent command might do. For example:


- It always executes `/etc/init.d` scripts in a clean environment. (Note the long `env` command invocation in the `run_via_sysvinit` function above.)
- It maps `restart` on Upstart systems to a combination of `stop/start`, since a plain `initctl restart` will error out if the service isn't running already.
- It stops sockets when stopping systemd services which have associated sockets:

```bash
case "${ACTION}" in
  restart|status)
     exec systemctl $sctl_args ${ACTION} ${UNIT}
  ;;
  start|stop)
     # Follow the principle of least surprise for SysV people:
     # When running "service foo stop" and foo happens to be a service that
     # has one or more .socket files, we also stop the .socket units.
     # Users who need more control will use systemctl directly.
```

Upstart services were enabled directly in the service configuration file (or
disabled via overrides), and System V scripts were enabled or disabled with
the `update-rc.d` command (which managed symlinks in the `/etc/rc*` directories),
so the `service` command was never involved in enabling or disabling services on
boot.

## Reference

- [https://askubuntu.com/questions/903354/difference-between-systemctl-and-service-commands](https://askubuntu.com/questions/903354/difference-between-systemctl-and-service-commands)