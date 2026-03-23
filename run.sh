#!/usr/bin/env bash
set -e

IMAGE_NAME="recipe-normalizer"
INPUT_DIR="${1:-./recipes}"
OUTPUT_FILE="${2:-output.json}"

docker build -t "$IMAGE_NAME" .

docker run --rm \
  -v "$(cd "$INPUT_DIR" && pwd)":/data/input \
  -v "$(pwd)":/data/output \
  "$IMAGE_NAME" /data/input -o "/data/output/$OUTPUT_FILE"

echo "Done — output written to $OUTPUT_FILE"
