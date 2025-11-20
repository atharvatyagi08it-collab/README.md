1. PROBLEM STATEMENT- : Credit Card Validator Program
# Goal-The primary goal is to develop a Python program that can validate a given sequence of digits to determine if it is a potentially valid credit card number based on industry-standard rules, most notably the Luhn Algorithm
#. Input-The program must accept a single input:
Credit Card Number: A sequence of digits provided as a string (which may optionally contain spaces or hyphens, which must be sanitized).
# Processing and Validation Criteria
The program must implement and check the following three core criteria in order:
A. Input Sanitization
Remove all non-digit characters (e.g., spaces, hyphens) from the input string to ensure only a pure sequence of digits is processed.
B. Length Validation
Check if the sanitized number's length is valid for common card types. Acceptable lengths are typically 13, 15, 16, or 19 digits. Any number falling outside these lengths should be immediately marked as invalid.
C. Luhn Algorithm Check
The core of the validation. The program must apply the Luhn Algorithm (Mod 10 formula) to the number.
Starting from the rightmost digit (the check digit) and moving left, double the value of every second digit.
If the result of doubling is greater than 9, subtract 9 from the result.
Sum all the digits in the resulting sequence.
If the total sum modulo 10 is equal to 0, the number passes the Luhn check.
2. SCOPE OF THE PROJECT-The project is limited to functions necessary for validating the numerical integrity and brand identification of a credit card number.
Input Handling & Sanitization: The program must accept input and cleanse it by stripping all non-digit characters (spaces, hyphens, etc.) before processing.
Length Check: The program must verify that the sanitized input string falls within a standard range of credit card lengths (e.g., 13, 15, 16, 19 digits).
Luhn Algorithm Implementation: The program must correctly implement and execute the Luhn Algorithm (Mod 10 formula) to check the number's mathematical validity.
Card Brand Identification: The program must identify the card brand (e.g., Visa, Mastercard, Amex) based on the number's prefix (starting digits).
Clear Output Reporting: The program must output a definitive status (VALID or INVALID) along with the identified brand or a specific reason for failure.
Technology Constraint: The program must be implemented strictly using Python and its built-in features, without external libraries.
3. TARGET USERS - #🧑‍💻 Python Developers / Engineers
These users are actively working on or integrating with systems that handle credit card information.
Goal: To test their own code's logic, ensure accurate implementation of the Luhn Algorithm, and verify prefix and length rules during the development phase of a larger system (like an e-commerce checkout or billing module).
Need: A straightforward, command-line tool that provides immediate feedback on a card number's structural validity without the complexity of a full payment gateway integration.
# Quality Assurance (QA) Testers
These users are responsible for ensuring the reliability of financial applications.
Goal: To generate or test both valid and invalid card numbers according to known rules to rigorously test the input fields and validation logic of other applications.
Need: A tool to quickly confirm if a test number they are using should pass or fail the Luhn check before they use it to test a payment form.
4. HIGH LEVEL FEATURES- The high-level features of the Credit Card Validator Program are the essential capabilities that fulfill the core requirements of the problem statement. They represent the main tasks the program performs to successfully validate a card number.
Here are the key high-level features:
#🧼 Input Sanitization Engine
This feature handles the preliminary cleanup of the user's input before any validation logic is applied.
Function: Automatically strips all non-digit characters (spaces, hyphens, dashes, parentheses, etc.) from the input string.
Purpose: Ensures that the core validation logic, which relies purely on a sequence of digits, does not fail due to formatting issues or user input errors.
Output: A clean, contiguous string of digits ready for mathematical and structural checks.
#📏 Structural Integrity Validation
This feature performs the initial structural checks based on the expected format of credit card numbers.Length Check: Verifies that the sanitized number has an industry-standard length (e.g., 13, 15, 16, or 19 digits).
Prefix Check (Brand Identification): Examines the starting digits to categorize the number as a specific card brand (Visa, Mastercard, Amex, etc.). This is necessary even if the card passes the Luhn check, as most cards must adhere to brand-specific lengths and prefixes.
#🔢 Luhn Algorithm Processor (Core Validation)
This is the central, mathematical feature that determines the theoretical validity of the number's sequence.
Function: Implements the Mod 10 or Luhn Algorithm logic, which involves doubling every second digit (from right to left), summing the resulting digits, and checking if the total sum is divisible by 10.
Purpose: Provides a high degree of confidence that the number is not a randomly generated sequence and adheres to the internal mathematical structure of real card numbers.
