
import { Bot } from "./bot.ts";
import * as dotenv from 'dotenv';
dotenv.config({ path: '../../.env' });  // 👈 resolve from wherever you want



const bot = new Bot({
    token:process.env.DISCORD_TOKEN as string,
    applicationId:process.env.DISCORD_CLIENT_USER_ID as string,
    voiceSynthOptions:{
        host:"localhost",
        endpoint:"/voice_synth",
        port:5001
    },
})
bot.start()
