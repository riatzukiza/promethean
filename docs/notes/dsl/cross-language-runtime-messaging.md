To orchestrate multiple runtimes, start with JSON message passing between Sibilant's meta layer and Python, Node.js, or Rust processes. The design evolves toward shared buffers and metadata registration for typed data. Macros like `send-json` and `receive-json` handle serialization while future phases move to memory-mapped buffers and dispatch maps.

Related notes: [sibilant-meta-namespace-dispatch](sibilant-meta-namespace-dispatch.md), [polyglot-repl-interface](polyglot-repl-interface.md) [unique/index](../../unique/index.md)

#tags: #runtime #interop #json
