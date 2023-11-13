import unittest
from math_quiz import random_generator, rand_math_operation, calculate_output


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        for i in range(10):
            choices=['+', '-', '*']
            rand_choise=rand_math_operation()
            self.assertIn(rand_choise,choices)
             

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),(6,4,'-','6 - 4',2)]
               # ''' TODO add more test cases here '''
            #]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                 problem,out=calculate_output(num1,num2,operator)
                 self.assertEqual(out,expected_answer)
                 self.assertTrue(problem==expected_problem)

if __name__ == "__main__":
    unittest.main()
