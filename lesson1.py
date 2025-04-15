import unittest

# Функция, которую ты тестируешь
def perform_operation(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):
    def test_operation_add(self):
        result = perform_operation(1, 2)
        self.assertEqual(result, 3, msg="Result of 1 + 5 does not equal 3")

if __name__ == "__main__":
    unittest.main()
