---
title: "set -o pipefail"
published: true
tags: Shell
---

The `set -o pipefail` command is used in Bash scripts and interactive shells to change the behavior of pipelines.

## What does it do?

When `pipefail` is enabled, a pipeline will return the exit status of the **rightmost** command that fails (i.e., exits with a non-zero status), rather than the exit status of the last command in the pipeline.

## Default Behavior (Without set -o pipefail):

By default, a pipeline in Bash only returns the exit status of the last command.

```shell
#!/bin/bash
false | true
echo $? # Output: 0 (Success, because 'true' is the last command)
```

## With set -o pipefail:

When `pipefail` is set, the exit status of the pipeline is the first non-zero exit code in the pipeline (if any).

```shell
#!/bin/bash
set -o pipefail
false | true
echo $? # Output: 1 (Failure, because 'false' failed)
```

## Why is this useful?

- Helps catch errors in pipelines that might otherwise go unnoticed.
- Improves script robustness by ensuring failures propagate.
- Useful in CI/CD pipelines or automation scripts where silent failures can be problematic.

## Example Use Case:

```shell
set -o errexit # Exit script on any command failure
set -o pipefail # Ensure pipeline failures are not ignored

cat nonexistent.txt | grep "hello"

# Without pipefail, the script might continue even if `cat` fails.
```
