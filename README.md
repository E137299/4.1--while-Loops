# 4.1-Loops

Here’s a Python programming assignment that incorporates the required functions using `while` loops:

---

**Assignment: Mastering `while` Loops**

**Objective:**  
In this assignment, you will write functions that use `while` loops to solve various problems. Each function will focus on a different task and incorporate looping logic. Follow the instructions for each function carefully.

### Instructions:
1. **Guessing Game Function**  
   Write a function `guess_question(question, answer)` that takes in a question (string) and an answer (string). Inside the function, the user is prompted to guess the answer to the question until they get it right. The function should return the number of guesses the user made.

   #### Example:
    Function call:
    ```python
    guess_count = guess_question("What is the capital of France?", "Paris")
    print(f'The number of guesses: {guess_count}')
    ```
    Output:
    ```
    What is the capital of France? London
    What is the capital of France? Berlin
    What is the capital of France? Paris
    The number of guesses: 3
    ```

<br></br>
---
2. **Countdown Function**  
   Write a function `count_down_by_10(num)` that takes in a number and counts down from that number by 10 until it reaches 0 or less. After the countdown is complete, the function should print "Done!".
   
   #### Example:
   Function call:
   ```python
   count_down_by_10(50)
    ```
    Output:
    ```python
    50
    40
    30
    20
    10
    0
    Done!
    ```
<br></br>
---
3. **Sum of Values Function**  
   Write a function `sum_to_n(n)` that takes in a number `n` and returns the sum of all values from 1 to `n`.

   #### Example
   Function call:
   ```python
    num = 5
    total = sum_to_n(num)
    print(f"Sum of integers from one to {num}: {total}")
    ```
    Output:
    ```
    Sum of integers from 1 to 5: 15
    ```
<br></br>
---
4. **Even Numbers String Function**  
   Write a function `even_numbers(a, b)` that takes in two values `a` and `b` and returns a string of the even numbers between the two values (inclusive).
   #### Example
   Function call:
   ```python
    min = 3
    max = 10
    evens = even_numbers(min, max)
    print(f"Even numbers between {min} and {max}: {evens}")
    ```
    Output:
    ```
    Even numbers from 3 to 10: 4 6 8 10
    ```
<br></br>
---
5. **Prime Number Function**  
   Write a function `is_prime(n)` that takes in a number `n` and returns `True` if the number is prime, `False` otherwise. A prime number is an integer greater than 1 that has no positive divisors other than 1 and itself. In other words, it cannot be divided evenly by any number other than 1 and the number itself.
   #### Example
   Function call:
   ```python
    num1 = 7
    result1 = is_prime(num1)
    print(f"{num1} is prime: {result1}")

    num2 = 10
    result2 = is_prime(num2)
    print(f"{num2} is prime: {result2}")
    ```
    Output:
    ```
    7 is even: True
    10 is even: False
    ```
<br></br>
---
6. **Number Names Function**  
   Write a function `number_to_names(num)` that takes in a multi-digit number and returns a string with the names of the digits (e.g., `123` -> "one two three").

    **Hint:**  
    To separate the digits of a multi-digit number, you can use the modulus (`%`) and integer division (`//`) operations. The modulus operation (`num % 10`) will give you the last digit of the number, while the integer division (`num // 10`) will remove the last digit. You can use these operations in a loop to extract each digit from right to left.

    For example, if the number is `123`:
    - `123 % 10` will give `3`.
    - `123 // 10` will give `12` (removing the last digit).
    - Repeat this process to extract each digit one by one.
    #### Example
    Function call:
    ```python
    names = number_to_names(123)
    print(names)
    ```
    Output:
    ```
    one two three
    ```


<br></br>
---
7. **Number Guessing Game Function**  
   Write a function `guess_number(target)` that takes in a number `target` and prompts the user to guess the number. The function should return the count of even and odd guesses the user made before correctly guessing the number.
    #### Example
    Function Call:
    ```python
    even_count, odd_count = guess_number(5)
    print("\nEven guesses:", positive_count)
    print("Odd guesses:", negative_count)
    ```
    Output:
    ```
    Guess the number: -3
    Guess the number: 4
    Guess the number: 5

    Even guesses: 1
    Odd guesses: 2
    ```









