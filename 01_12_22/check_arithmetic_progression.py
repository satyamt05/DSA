
class Solution: 
    def checkIsAP(self, arr, n): 
        c=0
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(len(arr)-1):
            if (arr[i+1]-arr[i]!=d):
                c=1
        if c==0:        
            return True  
        else:
            return False
      # code here
        