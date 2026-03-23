import pytest
from pathlib import Path

SAMPLE_XML = """\
<?xml version="1.0" encoding="UTF-8" ?>
<root>
   <name>pancakes</name>
   <ingredients>
      <item>flour</item>
      <quantity>2</quantity>
      <unit>cups</unit>
   </ingredients>
   <ingredients>
      <item>milk</item>
      <quantity>1.5</quantity>
      <unit>cups</unit>
   </ingredients>
   <ingredients>
      <item>eggs</item>
      <quantity>3</quantity>
      <unit></unit>
   </ingredients>
   <preparations>Mix all ingredients</preparations>
   <preparations>Cook on griddle</preparations>
</root>
"""

SAMPLE_YAML = """\
---
name: salad
ingredients:
- item: lettuce
  quantity: 0.5
  unit: pound
- item: olive oil
  quantity: 2
  unit: fl. oz.
- item: tomato
  quantity: 3
  comment: diced
preparations:
- Chop vegetables
- Toss with dressing
"""

SAMPLE_JSON = """\
{
  "name": "soup",
  "ingredients": [
    {"item": "water", "quantity": 1, "unit": "gallon"},
    {"item": "salt", "quantity": 2, "unit": "tsp"}
  ],
  "preparations": ["Boil water", "Add salt"]
}
"""


@pytest.fixture
def sample_dir(tmp_path: Path) -> Path:
    """Create a temp directory with one file of each supported format."""
    (tmp_path / "pancakes.xml").write_text(SAMPLE_XML)
    (tmp_path / "salad.yaml").write_text(SAMPLE_YAML)
    (tmp_path / "soup.json").write_text(SAMPLE_JSON)
    return tmp_path
