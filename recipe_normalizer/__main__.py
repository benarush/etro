import argparse
import logging
import sys
from pathlib import Path

from recipe_normalizer.normalizer import process_directory, write_output


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Normalize cooking recipes to a consistent JSON format with metric units.",
    )
    parser.add_argument("input_dir", type=Path, help="Directory containing recipe files")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("output.json"), help="Output JSON file path (default: output.json)"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    if not args.input_dir.is_dir():
        logging.error("Input path is not a directory: %s", args.input_dir)
        sys.exit(1)

    recipes = process_directory(args.input_dir)

    if not recipes:
        logging.warning("No recipes found in %s", args.input_dir)

    write_output(recipes, args.output)


if __name__ == "__main__":
    main()
