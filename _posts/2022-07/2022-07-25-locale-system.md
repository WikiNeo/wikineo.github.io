---
title: 'Locale System'
published: true
tags: Linux
---

## What are locales?

A locale is a set of information that most programs use for determining
country and language specific settings. The locales and their data are part of
the system library and can be found at /usr/share/i18n/locales/ on most
systems. A locale name is generally named `ab_CD` where `ab` is the two (or three)
letter language code (as specified in ISO-639) and `CD` is the two letter
country code (as specified in ISO-3166). Variants like @euro or @latin are
often appended to locale names, e.g. de_DE@euro or nan_TW@latin.

## Environment variables for locales

- `LANG`
  - Defines all locale settings at once, while allowing further individual customization via the LC_* settings below.
- `LC_COLLATE`
  - Define alphabetical ordering of strings. This affects e.g. output of sorted directory listings.
- `LC_CTYPE`
  - Define the character-handling properties for the system. This determines which characters are seen as alphabetic, numeric, and so on. This also determines the character set used, if applicable.
- `LC_MESSAGES`
  - Programs' localizations stored in /usr/share/locale/ for applications that use a message-based localization scheme (the majority of GNU programs).
- `LC_MONETARY`
  - Defines currency units and formatting of currency-type numeric values.
- `LC_NUMERIC`
  - Defines formatting of numeric values which aren't monetary. Affects things such as thousand separator and decimal separator.
- `LC_TIME`
  - Defines formatting of dates and times.
- `LC_PAPER`
  - Defines default paper size.
- `LC_ALL`
  - Overrides all other settings.

## Reference

- [https://wiki.gentoo.org/wiki/Localization/Guide#Locale_system](https://wiki.gentoo.org/wiki/Localization/Guide#Locale_system)