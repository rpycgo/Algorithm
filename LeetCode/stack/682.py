class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        total = 0

        for operation in operations:
            if operation == 'C':
                total -= record.pop()
            elif operation == 'D':
                value = 2*record[-1]

                record.append(value)
                total += value
            elif operation == '+':
                value = record[-1] + record[-2]
                
                record.append(value)
                total += value
            else:
                value = int(operation)
                
                record.append(value)
                total += value
        
        return total
