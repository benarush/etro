from flask import Blueprint, request, jsonify
from pydantic import ValidationError

from const import LETTER_RULES
from validation import ValidateRequest

api = Blueprint("api", __name__)


def validate_word(word: str) -> dict:
    for i in range(len(word) - 1):
        current, next_letter = word[i], word[i + 1]

        if current not in LETTER_RULES:
            return {"valid": False, "reason": f"'{current}' is not a recognized letter"}

        if next_letter not in LETTER_RULES[current]["followers"]:
            return {"valid": False, "reason": f"'{next_letter}' cannot follow '{current}'"}

    last = word[-1]
    if last not in LETTER_RULES:
        return {"valid": False, "reason": f"'{last}' is not a recognized letter"}

    if not LETTER_RULES[last]["can_be_final"]:
        return {"valid": False, "reason": f"'{last}' cannot be the final letter"}

    return {"valid": True}


@api.route("/validate", methods=["POST"])
def validate():
    try:
        body = ValidateRequest(**request.get_json())
    except ValidationError as e:
        return jsonify({"error": e.errors()}), 400

    result = validate_word(body.word)
    return jsonify({"word": body.word, **result})
