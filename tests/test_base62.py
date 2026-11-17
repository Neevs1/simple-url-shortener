import pytest
from app.services import base62 as base62

def test_encode():
    # Test encoding of 0
    assert base62.encode_postgres_bigint(0) == '0'

    # Test encoding of a small number
    assert base62.encode_postgres_bigint(1) == '1'
    assert base62.encode_postgres_bigint(61) == 'Z'

    # Test encoding of a larger number
    assert base62.encode_postgres_bigint(62) == '10'
    assert base62.encode_postgres_bigint(3843) == 'ZZ'
    assert base62.encode_postgres_bigint(238327) == 'ZZZ'

    # Test encoding of a very large number
    assert base62.encode_postgres_bigint(1234567890123456789) == '1tckI1NfUnH'

    # Test that negative numbers raise ValueError
    with pytest.raises(ValueError):
        base62.encode_postgres_bigint(-1)

    # Test that non-integer values raise TypeError
    with pytest.raises(TypeError):
        base62.encode_postgres_bigint("not an integer") 