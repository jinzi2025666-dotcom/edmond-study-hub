// Offline single-file build: `npm run build:offline`
// Produces ../offline/edmond-study-hub.html that works from file:// with no server.
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { viteSingleFile } from "vite-plugin-singlefile";
import { fileURLToPath } from "node:url";
import path from "node:path";

const here = path.dirname(fileURLToPath(import.meta.url));

// KaTeX ships woff2 + woff + ttf for every face; Chrome only needs woff2.
const katexWoff2Only = {
  name: "katex-woff2-only",
  enforce: "pre",
  transform(code, id) {
    if (!id.includes("katex") || !id.endsWith(".css")) return null;
    return code
      .replace(/,\s*url\([^)]+\.woff\)\s*format\(["']woff["']\)/g, "")
      .replace(/,\s*url\([^)]+\.ttf\)\s*format\(["']truetype["']\)/g, "");
  },
};

// Drop the Google Fonts links; offline uses system Noto Sans CJK for Chinese.
const stripRemoteFonts = {
  name: "strip-remote-fonts",
  transformIndexHtml(html) {
    return html.replace(/\s*<link[^>]+fonts\.(googleapis|gstatic)\.com[^>]*>/g, "");
  },
};

export default defineConfig({
  mode: "offline",
  plugins: [katexWoff2Only, react(), stripRemoteFonts, viteSingleFile()],
  define: {
    "import.meta.env.VITE_OFFLINE": JSON.stringify(true),
  },
  resolve: {
    alias: [
      // Every `./api` / `../api` import becomes the localStorage data layer.
      { find: /^\.{1,2}\/api$/, replacement: path.resolve(here, "src/offline/store.js") },
    ],
  },
  build: {
    outDir: path.resolve(here, "../offline/build"),
    emptyOutDir: true,
    assetsInlineLimit: 100_000_000,
    cssCodeSplit: false,
    chunkSizeWarningLimit: 10_000,
  },
});
