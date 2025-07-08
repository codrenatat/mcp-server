import { Elysia, t } from "elysia";

const messages = {}; // { conversationId: [ {id, role, content} ] }

const messagesRoute = new Elysia({ prefix: "/messages" })
  .get("/:conversationId", ({ params }) => messages[params.conversationId] || [])
  .post("/", async ({ body }) => {
    const { conversationId, role, content } = body;

    if (!messages[conversationId]) messages[conversationId] = [];
    messages[conversationId].push({ id: Date.now().toString(), role, content });

    if (role === "user") {
      // Llama MCP para respuesta (ej: get_current_price_tool)
      const result = await client.callTool({
        name: "get_current_price_tool",
        arguments: { symbol: content },
      });

      const assistantMsg = {
        id: (Date.now() + 1).toString(),
        role: "assistant",
        content: result || "Error en MCP",
      };

      messages[conversationId].push(assistantMsg);

      return assistantMsg;
    }

    return { id: Date.now().toString(), role, content };
  });

export default messagesRoute;
