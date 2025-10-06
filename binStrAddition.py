class Solution:
    def binaryAdd(self, a:str,b:str) -> str:
        return bin(int(a,2)+int(b,2))[2:]
print(Solution().binaryAdd("10","1"))