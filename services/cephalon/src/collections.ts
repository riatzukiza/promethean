import { CollectionManager } from "./collectionManager";

export const discordMessages = await CollectionManager.create<"content", "created_at">("discord_messages", "content", "created_at");
export const thoughts = await CollectionManager.create<"text", "createdAt">("thoughts", "text", "createdAt");
export const transcripts = await CollectionManager.create<"text", "createdAt">("transcripts", "text", "createdAt");
