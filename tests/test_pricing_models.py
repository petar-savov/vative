import math
import pytest
from vative.pricing_models.black_scholes import black_scholes


@pytest.mark.parametrize(
    "S, K, T, r, sigma, option_type, expected_price",
    [
        (100, 100, 1, 0.05, 0.2, "call", 10.450583572185565),
        (100, 100, 1, 0.05, 0.2, "put", 5.573526022256971),
    ],
)
def test_black_scholes(S, K, T, r, sigma, option_type, expected_price):
    calculated_price = black_scholes(S, K, T, r, sigma, option_type)
    assert math.isclose(calculated_price, expected_price, rel_tol=1e-9)
