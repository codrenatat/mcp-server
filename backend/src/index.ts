import { Elysia } from "elysia";
import { html } from "@elysiajs/html";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "python",
  args: ["C:/Users/renis/Documents/PAP/mcp-server/mcp-server/src/server.py"], 
});

// Create MCP client instance
const client = new Client({
  name: "alpha-vantage-client",
  version: "1.0.0",
});

// Connect to the MCP server
await client.connect(transport);

// Call a tool
const result = await client.callTool({
  name: "get_current_price_tool", 
  arguments: {
  symbol: "AAPL",
  },
});

console.log("Result from MCP server:", result);

// Optional: Elysia server just to have a visible frontend
const app = new Elysia()
  .use(html())
  .get("/", () => `<h1>Result: ${JSON.stringify(result)}</h1>`)
  .listen(3000);

console.log("Server running at http://localhost:3000");