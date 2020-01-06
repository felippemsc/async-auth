from marshmallow import Schema, fields, ValidationError

from auth.constants import MIN_LENGTH_PASS, MAX_LENGTH_PASS


def validate_password(password: str):
    special_sym = "!$@#%&*/?;:|][}{~^"

    if len(password) < MIN_LENGTH_PASS or len(password) > MAX_LENGTH_PASS:
        raise ValidationError("Length must be between 8 and 20.")

    if not any(char.isdigit() for char in password):
        raise ValidationError("Must have at least one numeral.")

    if not any(char.isupper() for char in password):
        raise ValidationError("Must have at least one uppercase letter.")

    if not any(char.islower() for char in password):
        raise ValidationError("Must have at least one lowercase letter.")

    if not any(char in special_sym for char in password):
        raise ValidationError(
            "Must have at least one of the symbols !$@#%&*/?;:|][}{~^"
        )


class UserSchema(Schema):
    id = fields.Integer(dump_only=True)
    key = fields.String(dump_only=True)
    email = fields.Email()
    password = fields.String(load_only=True, validate=validate_password)
    created_at = fields.String(dump_only=True)
    updated_at = fields.String(dump_only=True)
