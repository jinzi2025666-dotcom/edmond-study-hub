// Copy the single-file build to offline/edmond-study-hub.html and sanity-check it.
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const outDir = path.resolve(here, "../../offline");
const built = path.join(outDir, "build", "index.html");
const target = path.join(outDir, "edmond-study-hub.html");

const html = fs.readFileSync(built, "utf8");
const external = [...html.matchAll(/<(script|link)[^>]+(src|href)="(https?:)?\/\/[^"]+"/g)].map((m) => m[0]);
if (external.length) {
  console.warn("Warning: external references remain:", external);
}
fs.writeFileSync(target, html);
fs.rmSync(path.join(outDir, "build"), { recursive: true, force: true });
console.log(`Offline file: ${target} (${(fs.statSync(target).size / 1024 / 1024).toFixed(2)} MB)`);
