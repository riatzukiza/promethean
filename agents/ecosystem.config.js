const path = require('path');
// Right now duck hosts all  the services, but as we move on this will become less and less true.
// Most of these services could be shared between agents.
// We are in the boot strap phase, I moved this code from another repo.
// we're just getting it running to match pairity for now.

// we have a mongodb instance running seperately from this file that the services depend on.
// we'll figure out what to do about that in the future.

// an instruction to future users?
// a container?

// I moved this out of containers because I was using the NPU for some of these services.
// and docker is just not the place to run that.
// either way, you use docker, you use a mongo db instance
// someone needs to download a program as a dependency.

module.exports = {
    apps: [
        {
            name: "tts",
            cwd: ".",
            script: "../services/tts/run.sh",
            interpreter:"bash",
            "exec_mode": "fork",
            watch: ["../services/tts"],
            instances: 1,
            autorestart: true,
            env: {

                PYTHONPATH: path.resolve(__dirname),
                PYTHONUNBUFFERED: "1",
                FLASK_APP: "app.py",
                FLASK_ENV: "production",
            },
            restart_delay: 10000,
            kill_timeout: 10000 

        },
        {
            name: "stt",
            cwd: "../services/stt",
            script: "../services/stt/run.sh",
            interpreter: "bash",
            exec_mode: "fork",
            watch: ["../services/stt"],
            instances: 1,
            autorestart: true,
            out_file: "../logs/stt-out.log",
            error_file: "../logs/stt-err.log",
            merge_logs: true,
            env: {
                PYTHONUNBUFFERED: "1",
                PYTHONPATH: path.resolve(__dirname),
            },

            restart_delay: 10000,
            kill_timeout: 10000 // wait 5s before SIGKILL
        },
        {
            name: "discord_indexer",
            cwd: ".",
            script: "python",
            args: "-m pipenv run python -m main",

            "exec_mode": "fork",
            watch: ["../services/discord_indexer"],
            instances: 1,
            autorestart: true,
            env: {
                PYTHONPATH: path.resolve(__dirname),
                PYTHONUTF8: "1",
                PYTHONUNBUFFERED: "1",
            },

            restart_delay: 10000,
            kill_timeout: 10000
        },
        {
            "name": "discord_speaker_js",
            "watch": ["../services/discord_speaker_js/src"],
            "cwd": ".",
            "script": "src/index.ts",
            "interpreter": "node",
            "node_args": ["--loader", "ts-node/esm"],
            "autorestart": true,
            "env_file": ".env",

            restart_delay: 10000,
            kill_timeout: 10000 // wait 5s before SIGKILL

        },
        {
            "name": "embedder",
            "watch": ["../services/embedder/src"],
            "cwd": ".",
            "interpreter": "node",
            "script": "./src/index.ts",
            // "script":"./services/embedder/src/index.ts",
            "node_args": ["--loader", "ts-node/esm"],
            "autorestart": true,
            "env_file": ".env"

        },
        {
            // should each agent hold their own chroma?
            // will there be a single core chroma?
            // or will it be a mix of the two?
            // some "core" data we know is just used by all agents
            // and some data is specific to the agent?
            // for now, we'll just run chroma in each agent
            "name": "chromadb",
            "script": "python",
            "args": "-m pipenv run chroma run --path ./chroma_data",
        }

    ]
};
