// news-image-20261122 — entry runner.
// Copies entry.png into $MAKEFUN_OUTPUT_DIR, byte for byte.
// Paths resolve relative to this file (import.meta.url); stdlib only,
// no network, no clock, no randomness. The copy is deterministic:
// the same entry.png always lands in the output dir unchanged.
// (entry.png itself is drawn by gen_image.py: a 1024x1024 front page
//  summing up Sunday 22 November 2026 in 35 dated stories, 7 regions.)
import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR;
if (!outDir) {
  throw new Error("MAKEFUN_OUTPUT_DIR is not set");
}
mkdirSync(outDir, { recursive: true });
const src = join(here, "entry.png");
const dest = join(outDir, "entry.png");
copyFileSync(src, dest);
console.log("entry.png -> " + dest + " (" + statSync(dest).size + " bytes)");
