import asyncio
import pytest
import json
import os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import uvicorn
import websockets
from threading import Thread

import services.whisper_stream_ws.app as stream_app


async def start_server(app, port):
    config = uvicorn.Config(app, host="127.0.0.1", port=port, log_level="warning")
    server = uvicorn.Server(config)
    thread = Thread(target=server.run, daemon=True)
    thread.start()
    # wait for startup
    while not server.started:
        await asyncio.sleep(0.05)
    return server, thread


async def stop_server(server, thread):
    server.should_exit = True
    thread.join()


@pytest.mark.asyncio
async def test_whisper_stream_ws_end_to_end(monkeypatch):
    class DummyStreamer:
        def transcribe_chunks(self, chunks, sample_rate=16000):
            for _ in chunks:
                yield "hi"

    monkeypatch.setattr(stream_app, "streamer", DummyStreamer())
    server, thread = await start_server(stream_app.app, 5051)
    try:
        uri = "ws://127.0.0.1:5051/stream"
        async with websockets.connect(uri) as ws:
            await ws.send(b"aa")
            msg = await ws.recv()
            assert json.loads(msg)["transcription"] == "hi"
    finally:
        await stop_server(server, thread)
