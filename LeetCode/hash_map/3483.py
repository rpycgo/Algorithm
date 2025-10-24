class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digits = [str(digit) for digit in digits]
        numbers = set()

        n_digits = len(digits)
        for i in range(n_digits-2):
            for j in range(i+1, n_digits-1):
                for k in range(j+1, n_digits):
                    number = ''.join([digits[i], digits[j], digits[k]])
                    if not number.startswith('0') and int(number)%2 == 0:
                        numbers.add(number)

                    reversed_number = number[::-1]
                    if not reversed_number.startswith('0') and int(reversed_number)%2 == 0:
                        numbers.add(reversed_number)

                    count = 0
                    while count < 2:
                        number = number[-1] + number[:2]
                        if number not in numbers and not number.startswith('0') and int(number)%2 == 0:
                            numbers.add(number)
                        
                        reversed_number = number[::-1]
                        if not reversed_number.startswith('0') and int(reversed_number)%2 == 0:
                            numbers.add(reversed_number)
        
                        count += 1

        answer = len(numbers)

        return answer
