import pytest

from src.spending_calculator import get_total


@pytest.fixture
def costs():
    return {'socks': 5, 'shoes': 60, 'sweater': 30}


def test_get_total_basic(costs):
    """Test basic calculation with existing items and tax."""
    assert get_total(costs, ['socks', 'shoes'], 0.09) == 70.85


def test_get_total_missing_item_ignored(costs):
    """Test that items not in costs are ignored."""
    assert get_total(costs, ['socks', 'banana'], 0.09) == 5.45


def test_get_total_empty_items(costs):
    """Test that empty items list returns 0.00."""
    assert get_total(costs, [], 0.09) == 0.00


def test_get_total_all_items_missing(costs):
    """Test that all missing items returns 0.00."""
    assert get_total(costs, ['banana', 'apple'], 0.09) == 0.00


def test_get_total_zero_tax(costs):
    """Test calculation with zero tax."""
    assert get_total(costs, ['socks', 'shoes'], 0.0) == 65.00


def test_get_total_rounding(costs):
    """Test that result is rounded to 2 decimal places."""
    result = get_total(costs, ['socks', 'shoes', 'sweater'], 0.09)
    assert result == round(result, 2)


def test_get_total_invalid_costs_type():
    """Test that TypeError is raised when costs is not a dict."""
    with pytest.raises(TypeError):
        get_total("not a dict", ['socks'], 0.09)


def test_get_total_invalid_items_type(costs):
    """Test that TypeError is raised when items is not a list."""
    with pytest.raises(TypeError):
        get_total(costs, "not a list", 0.09)


def test_get_total_invalid_tax_type(costs):
    """Test that TypeError is raised when tax is not a number."""
    with pytest.raises(TypeError):
        get_total(costs, ['socks'], "0.09")