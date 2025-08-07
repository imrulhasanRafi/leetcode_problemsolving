class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"        
        n, m = len(num1), len(num2)
        result = [0] * (n + m)

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = i + j + 1

                sum_ = mul + result[p2]
                result[p2] = sum_ % 10
                result[p1] += sum_ // 10

        result_str = ''.join(map(str, result)).lstrip('0')
        return result_str or "0"