class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if tasks==None or len(tasks)==0:
            return 0
        map1={}
        maxFreq=0
        maxCount=0
        #to make a hashmap such that {'A':3,'B':3} as well as get the maxFreq
        for task in tasks:
            cnt=map1.get(task,0)
            maxFreq=max(maxFreq,cnt+1)
            map1[task]=cnt+1
        for key in map1:
            if map1.get(key)==maxFreq:
                maxCount+=1
        partitions=maxFreq-1
        empty=(n-(maxCount-1))*partitions
        pending=len(tasks)-maxFreq*maxCount;
        idle=max(0,empty-pending)
        return idle + len(tasks)
        
#space is O(1) as hashmap can contain upto 26 alphabets..fixed size
#time is O(n) where n is the length of the tasks array
