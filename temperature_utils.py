from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> tuple[str, float]:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """

    return round(float((fahrenheit_temp - 32) * (5 / 9)), 2)


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    return round(float((celsius_temp * 1.8) + 32), 2)  # remove pass statement and implement me


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    new_list = []
    for t in temperatures:
        if input_unit_of_measurement == 'f':
            new_list.append((t, convert_to_celsius(t)))
        elif input_unit_of_measurement == 'c':
            new_list.append((t, convert_to_fahrenheit(t)))
        else:
            return tuple(new_list)

    return tuple(new_list)
