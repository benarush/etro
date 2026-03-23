import logging
import sys

from pydantic import ValidationError

from recipe_normalizer.normalizer import process_directory, write_output
from recipe_normalizer.utils.cli_args import parse_args


def main() -> None:
    try:
        args = parse_args()
    except ValidationError as e:
        logging.error("%s", e)
        sys.exit(1)

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    recipes = process_directory(args.input_dir)

    if not recipes:
        logging.warning("No recipes found in %s", args.input_dir)

    write_output(recipes, args.output)


if __name__ == "__main__":
    main()
