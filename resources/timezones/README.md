# Europe/Madrid fallback for Windows

`Europe-Madrid.tzif` is compiled IANA time-zone data (tzdb **2026b**), copied from the environment's installed `/usr/share/zoneinfo/Europe/Madrid`. IANA timezone data is public domain. Upstream: https://www.iana.org/time-zones .

It is used through `ZoneInfo.from_file` only if `ZoneInfo("Europe/Madrid")` is unavailable, as on a standard Windows Python installation without the optional tzdata package. It preserves the actual Madrid daylight-saving rules rather than substituting a fixed UTC offset. The application never disables validation or downloads a replacement during startup.

To update it, use an authentic installed IANA tzdb release, replace the compiled Europe/Madrid file, record its version and SHA-256, and rerun the week/DST tests and the missing-system-zone regression test. The SHA-256 recorded below documents this bundled version; do not change it to bypass an integrity failure.
9a42d7d37ad6dedd2d9b328120f7bf9e852f6850c4af00baff964f659b161cea  resources/timezones/Europe-Madrid.tzif
