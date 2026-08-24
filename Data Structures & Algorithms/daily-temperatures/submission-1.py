class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given temperatures = a list-> output results a list 
        # eg result[i] == 3: it's 3 days of consistent cooling after day i
        # brute force:
            # for every day i go through temperatures and check when the temperature finally increases
        # for days:
            # inc day tracker incs if base_temp > temp[i]
            # how to set base_temp
                # set base_temp= initial temp
            # else: while day_tracker > 0: append results with day_tracker and decr
                # update base_temp to current temp
        res = [0]*len(temperatures)
        stack = []
        for i,t in enumerate(temperatures): # ind i , temperature[i]
            while stack and t > stack[-1][0]:
                stackT,stackInd =stack.pop()
                res[stackInd] = i- stackInd
            stack.append((t,i))
        return res