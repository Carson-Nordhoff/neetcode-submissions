class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
          
        num = 0

        for i in range(len(digits)):
            num += digits[i] * 10**(len(digits)-i-1)

        num += 1

        print(f'num: {num}')

        ans = []

        count = 1
        while num > 0:
            remainder = num % 10**count
            num -= remainder
            ans.append(remainder // 10**(count-1))
            count += 1 
            print(f'Remainder: {remainder}. Num: {num}. Answer: {ans}')

        return ans[::-1]