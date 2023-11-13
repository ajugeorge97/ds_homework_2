import random


def random_generator(min, max):
    """
    Random Generator 
    Desc: This function generates a Random integer.
    input:
        min: minimum value
        max:max value
    returns:
        random int

    """
    return random.randint(min, max)

def rand_math_operation():
    """
    rand_math_operation
    Desc : Generate a random math operation
    return:
        random choice of list['+', '-', '*']
    """
    return random.choice(['+', '-', '*'])


def calculate_output(value_1, value_2, operation):
    """
    Calculate the result of a mathematical operation between two values.

    Parameters:
        value_1 : The first operand.
        value_2: The second operand.
        operation(str): The mathematical operation to perform. Should be one of '+', '-', or '*'.

    Returns:
        tuple: A tuple containing the mathematical problem as a string and the calculated result.
    """


    problem = f"{value_1} {operation} {value_2}"
    if operation == '+': 
        output = value_1 + value_2
    elif operation == '-': 
        output = value_1 - value_2
    else: 
        output = value_1 * value_2
    return problem, output

def math_quiz():
    """
    Math quiz: 
    An interactive python math quiz game
    
    """
    score = 0
    tries= 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(tries)):
        #variables generation
        value_1 = random_generator(1, 10)
        value_2 = random_generator(1, 5)
        operation = rand_math_operation()
        #output calculation
        problem, output = calculate_output(value_1, value_2, operation)
        print(f"\nQuestion: {problem}")
        try:
            useranswer = input("Your answer: ")
            useranswer = int(useranswer)
        except Exception as e:
            print(e)
            print("Please Check your input")

        if useranswer == output:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {output}.")

    print(f"\nGame over! Your score is: {score}/{tries}")

if __name__ == "__main__":
    math_quiz()
