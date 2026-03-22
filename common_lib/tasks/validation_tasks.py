from common_lib.exceptions import ValidationError


def validate_not_empty(value: dict | None) -> dict:
    if not value:
        raise ValidationError("value is empty")
    return {
        "status": "valid",
        "value": value,
    }
