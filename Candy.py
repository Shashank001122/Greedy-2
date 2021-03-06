class Solution:
    def candy(self, ratings: List[int]) -> int:
        if ratings==None or len(ratings)==0:
            return 0
        candies=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],1+candies[i+1])
        sum1=0
        for i in candies:
            sum1+=i
        
        return sum1
#Time complexity is O(n)
#Space is O(n)
                
        
