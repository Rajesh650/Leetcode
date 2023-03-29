class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if x==0:
            return 0
        elif n ==0:
            return 1 
        elif (x==0 )and  (n==0):
            return 1
        else :
            return pow(x,n)
        