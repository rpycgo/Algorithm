class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_code_map = {
            chr(i): morse_code
            for i, morse_code
            in zip(range(97, 123), morse_codes)
        }

        count = defaultdict(int)
        for word in words:
            decoded_morse_code = []
            for char in word:
                decoded_morse_code.append(morse_code_map.get(char))
            decoded_morse_code = ''.join(decoded_morse_code)

            count[decoded_morse_code] += 1

        return len(count)
