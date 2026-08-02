import string

ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase


def encode_postgres_bigint(value: int) -> str:
    """Encode a Postgres BIGINT value as a Base62 string."""
    if not isinstance(value, int):
        raise TypeError("value must be an integer")
    if value < 0:
        raise ValueError("value must be non-negative")
    if value == 0:
        return ALPHABET[0]

    encoded_chars = []
    while value:
        value, remainder = divmod(value, len(ALPHABET))
        encoded_chars.append(ALPHABET[remainder])

    return "".join(reversed(encoded_chars))

