
def get_total(costs: dict[str, float], items: list[str], tax: float) -> float:
    """
    Calculate the total cost of items plus tax, ignoring non-existent items.

    :param costs: A dictionary where keys are item names and values are their costs.
    :type costs: dict[str, float]
    :param items: A list of item names to be purchased.
    :type items: list[str]
    :param tax: The tax rate to apply (e.g., 0.09 for 9%).
    :type tax: float

    :return: The total cost rounded to two decimal places. 
    :rtype: float

    :raises TypeError: If 'costs' is not of type dict.
    :raises TypeError: If 'items' is not of type list.
    :raises TypeError: If 'tax' is not a number (int or float).
    """
    if not isinstance(costs, dict):
        raise TypeError("costs must be a dictionary")
    if not isinstance(items, list):
        raise TypeError("items must be a list")
    if not isinstance(tax, (int, float)):
        raise TypeError("tax must be a number")

    total_base = 0.0

    for item in items:
        if item in costs:
            total_base += costs[item]


    total_con_impuesto = total_base * (1 + tax)

    return round(total_con_impuesto, 2)