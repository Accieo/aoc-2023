from typing import Union, Literal

def parse_input():
    with open("input/day09.txt", "r") as file:
        data = file.read().strip().splitlines()
        data = list(map(lambda x: x.split(" "), data))
        history = list()
        for entry in data:
            history.append(list(map(int, entry)))

    return history

def divided_differences(x_values: Union[list, range], y_values: list[int]) -> list[float]:
    """
    Given a sequence of data points (x0, y0) ... (xn, yn)
    This method calculates the coefficients of the interpolation polynomial of these points in the Newton form.
    Read more: https://en.wikipedia.org/wiki/Divided_differences
    """
    n = len(x_values)
    coefficients = list(map(float, y_values))

    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coefficients[i] = (coefficients[i] - coefficients[i - 1]) / (x_values[i] - x_values[i - j])

    return coefficients

def newton_interpolation(x_values: Union[list, range], coefficients: list[float], nth: int):
    """
    Polynomial interpolation is the interpolation of a given bivariate data set by the polynomial of lowest
    possible degree that passes through the points of the dataset.
    Read more: https://en.wikipedia.org/wiki/Newton_polynomial
    """
    result = coefficients[-1]
    n = len(x_values)

    for i in range(n - 2, -1, -1):
        result = result * (nth - x_values[i]) + coefficients[i]

    return result

def solve(part: Literal[1, 2] = 1) -> int:
    history = parse_input()

    values = list()
    for entry in history:
        length_history = len(entry) + 1
        x_values = range(1, length_history)

        coefficients = divided_differences(x_values=x_values, y_values=entry)

        if part == 1:
            interpolated_value = newton_interpolation(x_values=x_values, coefficients=coefficients, nth=length_history)
        else:
            interpolated_value = newton_interpolation(x_values=x_values, coefficients=coefficients, nth=0)
        values.append(interpolated_value)

    sum_of_interpolated = int(sum(values))

    return sum_of_interpolated

def part_one():
    return solve(part=1)

def part_two():
    return solve(part=2)

if __name__ == "__main__":
    print(part_one())
    print(part_two())
