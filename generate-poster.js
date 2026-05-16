import OpenAI from "openai";
import { readFileSync, writeFileSync } from "fs";
import { fileURLToPath } from "url";
import { dirname, resolve } from "path";

const __dir = dirname(fileURLToPath(import.meta.url));
const envVars = Object.fromEntries(
  readFileSync(resolve(__dir, ".env"), "utf8")
    .split("\n")
    .filter((l) => l.includes("="))
    .map((l) => l.split("=").map((s) => s.trim()))
);

const openai = new OpenAI({ apiKey: envVars.OPENAI_API_KEY });

async function generatePoster() {
  console.log("Generating CB-013 poster via gpt-image-1...");

  const image = await openai.images.generate({
    model: "gpt-image-1",
    prompt: `Professional education poster for a Malaysian AI tech company called IGEN VERITAS.
Topic: AI Chatbot for Business — how it works.
Style: Clean, modern, dark navy background (#0b0b14), purple and blue gradient accents (#7b67d1 to #488fe3).
Include: icons representing chat, automation, 24/7 availability.
Text: English. Bold headline at top, 3 key benefit bullet points, IGEN VERITAS branding at bottom.
No stock photo elements, vector/flat design style.`,
    n: 1,
    size: "1024x1024",
  });

  const b64 = image.data[0].b64_json;
  const outPath = resolve(__dir, "social-media/CB-013_poster_test.png");
  writeFileSync(outPath, Buffer.from(b64, "base64"));
  console.log("\nPoster saved to: social-media/CB-013_poster_test.png");
  console.log("Open it in VS Code or your file explorer to view it.");
}

generatePoster().catch((err) => {
  console.error("Error:", err.message);
  process.exit(1);
});
