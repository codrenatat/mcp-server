import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

// Transport
const transport = new StdioClientTransport({
  command: "python",
  args: ["../mcp-server/src/server.py"],
});

// Cliente
const client = new Client({
  name: "alpha-vantage-client",
  version: "1.0.0",
});

// Conexión inmediata al importar
await client.connect(transport);

console.log("✅ MCP client connected");

export const mcpClient = client;


