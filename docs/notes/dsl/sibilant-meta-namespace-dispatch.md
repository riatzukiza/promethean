Sibilant's macros can be organized by namespace to avoid runtime `if` checks. By defining `python.macros.*` or `js.macros.*`, the compiler resolves macro implementations at compile time. This yields faster dispatch and clear separation of per-target logic while keeping Sibilant's semantics intact.

Related notes: [sibilant-cross-target-macros](sibilant-cross-target-macros.md), [template-based-compilation](template-based-compilation.md) [unique/index](../../unique/index.md)

#tags: #sibilant #macros #namespaces
