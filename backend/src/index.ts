import { Elysia } from "elysia";
import { cors } from "@elysiajs/cors";
import { database } from "./database";
import conversations from "./routes/conversations";
import messages from "./routes/messages";
import { mcpClient } from "./mcpClient"; // cliente MCP externo

const app = new Elysia()
  .use(cors())
  .use(database)
  .decorate("mcpClient", mcpClient) 
  .use(conversations)
  .use(messages)
  .listen(3000);

console.log(`Server running at http://localhost:3000`);

