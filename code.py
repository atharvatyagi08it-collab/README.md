import re

class CreditCardValidator:
    def __init__(self, card_number):
        # Remove any spaces or dashes from input
        self.card_number = re.sub(r'\D', '', str(card_number))

    def luhn_check(self):
        """
        Performs the Luhn Algorithm (Mod 10 Check) to validate the card number.
        """
        if not self.card_number.isdigit():
            return False
        
        # Convert string to list of integers
        digits = [int(d) for d in self.card_number]
        
        # 1. Reverse the list of digits
        digits = digits[::-1]
        
        # 2. Double every second digit
        for i in range(1, len(digits), 2):
            digits[i] *= 2
            # 3. If doubled number is > 9, subtract 9 (sum of digits)
            if digits[i] > 9:
                digits[i] -= 9
                
        # 4. Sum all the digits
        total_sum = sum(digits)
        
        # 5. If sum is divisible by 10, it is valid
        return total_sum % 10 == 0

    def get_card_type(self):
        """
        Identifies the card network based on IIN ranges (Prefixes) and Length.
        """
        num = self.card_number
        length = len(num)

        # VISA: Starts with 4, length 13 or 16
        if re.match(r"^4[0-9]{12}(?:[0-9]{3})?$", num):
            return "Visa"

        # MASTERCARD: Starts with 51-55 or 2221-2720, length 16
        # (Includes new 2-series BIN ranges)
        if re.match(r"^(5[1-5][0-9]{14}|2(22[1-9][0-9]{12}|2[3-9][0-9]{13}|[3-6][0-9]{14}|7[0-1][0-9]{13}|720[0-9]{12}))$", num):
            return "Mastercard"

        # AMERICAN EXPRESS: Starts with 34 or 37, length 15
        if re.match(r"^3[47][0-9]{13}$", num):
            return "American Express"

        # DISCOVER: Starts with 6011 or 65, length 16
        if re.match(r"^6(?:011|5[0-9]{2})[0-9]{12}$", num):
            return "Discover"

        return "Unknown Card Type"

    def validate(self):
        """
        Main function to run checks and print report.
        """
        print(f"\n--- Analyzing Card: {self.card_number} ---")
        
        # Check 1: Is the math valid?
        is_valid = self.luhn_check()
        
        if is_valid:
            # Check 2: Who issued the card?
            card_type = self.get_card_type()
            print(f" Status: VALID")
            print(f"Network: {card_type}")
        else:
            print(f" Status: INVALID (Luhn Check Failed)")


# --- Main Execution ---
if __name__ == "__main__":
    print("Enter a credit card number (spaces/dashes are okay):")
    user_input = input("> ")
    
    validator = CreditCardValidator(user_input)
    validator.validate()
