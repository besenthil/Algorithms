class LuhnDigitChecker(object):
    def __init__(self,number):
        self.number = abs(number)

    def is_valid_number(self):
        def sum_2_digit_to_1_digit(number):
            # works only for 2 digits less than or equal to 18
            return int(number%10) + int(number/10)

        even_digits = list(str(self.number))[-2::-2]
        even_digits.reverse()
        even_digits = list(map(lambda y: int(y)*2, even_digits))
        even_digits = list(map(sum_2_digit_to_1_digit, even_digits))

        odd_digits = list(str(self.number))[-1::-2]
        odd_digits.reverse()
        odd_digits = list(map(int,odd_digits))

        checksum = sum(even_digits+odd_digits)
        return checksum % 10 == 0