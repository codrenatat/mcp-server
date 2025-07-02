import path from "path";
import { Elysia } from "elysia";
import { html } from "@elysiajs/html";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

const transport = new StdioClientTransport({
  command: "python",
  args: ["../../mcp-server/src/server.py"],
  env: {
    ...process.env,
    PYTHONPATH: path.resolve(__dirname, "../../mcp-server"),
  },
});

const client = new Client({
  name: "alpha-vantage-client",
  version: "1.0.0",
});

let resultText = "";

try {
  await client.connect(transport);

  const result = await client.callTool({
    name: "get_current_price_tool",
    arguments: { symbol: "AAPL" },
  });

  console.log("✅ Result from MCP server:", result);
  resultText = `Result: ${JSON.stringify(result)}`;
} catch (error) {
  console.error("❌ Error connecting to MCP server:", error);
  resultText = `Error connecting to MCP server: ${error.message || error}`;
}

new Elysia()
  .use(html())
  .get("/", () => `<h1>${resultText}</h1>`)
  .listen(3000);

console.log("🌐 Server running at http://localhost:3000");
