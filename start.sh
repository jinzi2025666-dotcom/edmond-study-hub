#!/usr/bin/env bash
# Start Edmond Study Hub on a fixed port (default 8787).
# Builds the frontend, then serves the API and the built site with one process.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT"
PORT="${PORT:-8787}"

if ! command -v python3 >/dev/null 2>&1; then
  echo "python3 is required" >&2
  exit 1
fi
if ! command -v npm >/dev/null 2>&1; then
  echo "npm / Node.js is required" >&2
  exit 1
fi

if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip >/dev/null
pip install -r requirements.txt

if [ ! -f "data/curriculum/content.json" ]; then
  python data/curriculum/build_content.py
fi

(
  cd frontend
  if [ ! -d node_modules ]; then
    npm install
  fi
  npm run build
)

echo
echo "Edmond Study Hub is starting at http://127.0.0.1:${PORT}"
echo "Open that address in a browser on this cloud computer."
echo
exec python -m uvicorn backend.main:app --host 0.0.0.0 --port "$PORT"
