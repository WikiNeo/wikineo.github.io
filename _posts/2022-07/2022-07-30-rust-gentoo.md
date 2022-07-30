---
title: '[Gentoo] Can not attach stdlib sources automatically without rustup'
published: true
tags: Gentoo
---

The `dev-lang/rust` Gentoo package has an `rls` use-flag (standing for Rust
Language Server), which has a side-effect of installing Rust sources to
`/usr/lib/rustlib/src`:

```shell
equery files dev-lang/rust | grep lib.rs

/usr/lib/rustlib/src/rust/src/libcore/lib.rs
/usr/lib/rustlib/src/rust/src/libstd/lib.rs
```

The solution is therefore to enable the `rls` use-flag and then point Intellij
IDEA to `/usr/lib/rustlib/src/rust/src`:


## Reference

- [https://stackoverflow.com/questions/57807583/in-intellij-idea-on-gentoo-how-do-i-attach-the-rust-stdlib-sources-since-gentoo](https://stackoverflow.com/questions/57807583/in-intellij-idea-on-gentoo-how-do-i-attach-the-rust-stdlib-sources-since-gentoo)