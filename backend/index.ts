import { Elysia } from "elysia";
import { html } from "@elysiajs/html";

const app = new Elysia()
    .use(html())
    .get("/", () => '<h1>Hello World<h1>')
    .listen(3000);

console.log("Server on http://localhost:", app.server?.port)