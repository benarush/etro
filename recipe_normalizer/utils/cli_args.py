import argparse
from pathlib import Path

from pydantic import BaseModel, field_validator


class CLIArgs(BaseModel):
    input_dir: Path
    output: Path = Path("output.json")
    verbose: bool = False

    @field_validator("input_dir")
    @classmethod
    def input_dir_must_exist(cls, v: Path) -> Path:
        if not v.is_dir():
            raise ValueError(f"Input path is not a directory: {v}")
        return v


def parse_args() -> CLIArgs:
    parser = argparse.ArgumentParser(
        description="Normalize cooking recipes to a consistent JSON format with metric units.",
    )
    parser.add_argument("input_dir", type=Path, help="Directory containing recipe files")
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("output.json"), help="Output JSON file path (default: output.json)"
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose logging")

    args = parser.parse_args()
    return CLIArgs(input_dir=args.input_dir, output=args.output, verbose=args.verbose)
