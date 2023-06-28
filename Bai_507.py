class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        c = 0
        if(num > 33550336) :
            return False
        for i in range(1, int (num/2 + 1)):
            if num % i == 0 :
                c = c + i
        if num == c:
            return True
        return False

        
