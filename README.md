# Recipe Normalizer

A command-line application that normalizes cooking recipes from various input formats (XML, YAML, JSON) to a consistent JSON file with metric units.

## Usage

```bash
python -m recipe_normalizer <input_dir> [-o output.json] [-v]
```

**Arguments:**
- `input_dir` — directory containing recipe files (.xml, .yaml, .yml, .json)
- `-o / --output` — output JSON file path (default: `output.json`)
- `-v / --verbose` — enable verbose logging

**Example:**

```bash
python -m recipe_normalizer ./recipes -o normalized.json
```

## Docker

```bash
docker build -t recipe-normalizer .
docker run -v $(pwd)/recipes:/data recipe-normalizer /data -o /data/output.json
```

## Tests

```bash
pip install -r requirements.txt
pytest
```

## Architecture

```
recipe_normalizer/
├── __main__.py       # CLI entry point (argparse)
├── models.py         # Ingredient & Recipe dataclasses
├── converter.py      # Imperial → metric conversion
├── normalizer.py     # Orchestration: read dir, parse, convert, write JSON
└── parsers/
    ├── base.py       # Abstract base parser (ABC)
    ├── xml_parser.py
    ├── yaml_parser.py
    └── json_parser.py
```

New input formats can be added by creating a parser class inheriting from `RecipeParser` and registering its file extension in `parsers/__init__.py`.

## Unit Conversion Table

| Imperial            | Metric | Factor    |
|---------------------|--------|-----------|
| pound / lb          | gr     | 453.592   |
| ounce / oz          | gr     | 28.3495   |
| gallon              | liter  | 3.785     |
| cup / cups          | gr     | 240       |
| fl. oz.             | ml     | 29.5735   |
| tablespoon / tbsp   | ml     | 14.787    |
| teaspoon / tsp      | ml     | 4.929     |
| quart               | liter  | 0.946     |
| pint                | ml     | 473.176   |

## Assumptions

- Each input file contains exactly one recipe.
- Quantities are always numeric (int or float).
- Empty or missing `unit` means the ingredient is unitless (count-based); no conversion is applied and the `unit` key is omitted from output.
- Units already in metric (ml, g, liter) are kept as-is.
- `preparations` is a list of strings.
- Quantities are rounded to 2 decimal places; whole numbers are output as integers.
- Cups are converted to grams using a factor of 240 (approximation treating 1 cup ≈ 240 ml ≈ 240 g).
- Unsupported file extensions in the input directory are skipped with a warning.
