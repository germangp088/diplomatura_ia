
def calculate_average(numbers):
  """Calculates the average of a list of numbers.

  Args:
    numbers: A list of numbers (integers or floats).  Can be empty.

  Returns:
    The average of the numbers in the list as a float.  Returns 0 if the list is empty.
    Raises TypeError if input is not a list or if the list contains non-numeric values.

  Examples:
    calculate_average([1, 2, 3, 4, 5]) == 3.0
    calculate_average([1.5, 2.5, 3.5]) == 2.5
    calculate_average([]) == 0
    calculate_average([-1, 0, 1]) == 0.0

  Edge Cases:
    - Empty list: Returns 0 to avoid ZeroDivisionError.
    - Non-numeric input in the list: Raises a TypeError.
    - Non-list input: Raises a TypeError.

  """
  if not isinstance(numbers, list):
    raise TypeError("Input must be a list.")
  if not all(isinstance(num, (int, float)) for num in numbers):
    raise TypeError("List must contain only numbers (integers or floats).")
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)


import unittest

def calculate_average(numbers):
  """Calculates the average of a list of numbers.

  Args:
    numbers: A list of numbers (integers or floats).  Can be empty.

  Returns:
    The average of the numbers in the list as a float.  Returns 0 if the list is empty.
    Raises TypeError if input is not a list or if the list contains non-numeric values.

  Examples:
    calculate_average([1, 2, 3, 4, 5]) == 3.0
    calculate_average([1.5, 2.5, 3.5]) == 2.5
    calculate_average([]) == 0
    calculate_average([-1, 0, 1]) == 0.0

  Edge Cases:
    - Empty list: Returns 0 to avoid ZeroDivisionError.
    - Non-numeric input in the list: Raises a TypeError.
    - Non-list input: Raises a TypeError.

  """
  if not isinstance(numbers, list):
    raise TypeError("Input must be a list.")
  if not all(isinstance(num, (int, float)) for num in numbers):
    raise TypeError("List must contain only numbers (integers or floats).")
  if not numbers:
    return 0
  return sum(numbers) / len(numbers)

class TestCalculateAverage(unittest.TestCase):

    def test_basic_functionality(self):
        self.assertEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(calculate_average([1.5, 2.5, 3.5]), 2.5)
        self.assertEqual(calculate_average([-1, 0, 1]), 0.0)

    def test_empty_list(self):
        self.assertEqual(calculate_average([]), 0)

    def test_single_element_list(self):
        self.assertEqual(calculate_average([5]), 5.0)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            calculate_average([1, 2, 'a'])
        with self.assertRaises(TypeError):
            calculate_average([1,2,True])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            calculate_average((1,2,3)) #Tuple input
        with self.assertRaises(TypeError):
            calculate_average("1,2,3") #String input

    def test_mixed_integer_float(self):
        self.assertEqual(calculate_average([1, 2.5, 3]), 2.1666666666666665)


if __name__ == '__main__':
    unittest.main()