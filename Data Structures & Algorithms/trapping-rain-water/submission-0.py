class Solution:
    def trap(self, height: List[int]) -> int:
        
        #area: however many open squares are within all two bars is the area
        # height of area is determined by min height of bar pairs
        # ideally there is a way to count all open squares
        # need a way to identify the bar pairs

        #1st way 
        # id all bar pairs
        # count the open squares for each bar pair

        # if height[i] > height[i+1] and height[j-1] < height[j]

        # i think it's easier to start from front only so like
        # i = 0 and j = i+1
        # bc it isolates the bar pairs one at a time instead of having multiple in between

        # so bar pairs ones at a time isolates the area we need to calc

        # we can find a bar pair with area if:
        # 1) if height[i] and height[j] > 0 # indicates that there is a bar
        # 2) there is space between the bar pair: if j-i > 1 #indicates bar #pair
        # 2) OR there is height difference height[i] != height[j]

        # im thinking two pointer while loop for above
        # the current flaw with this approach is we don't know if the open squares is truly contained or not. we will always need to find the next higher bar.
        # we need total_area = 0 and run_op_sqs = 0
        
        # next we need to find all the legal open squars between the bars
        # we can have a k with while loop: k=[i+1] but < j
        # OR for loop through for k in range(i+1,j)
        # need min height between two bars: min_h = min(height[i],height[j])
        # if height[k] <= min_h: run_op_sqs += min_h-height[k]

        # NEW APPROACH
        # two pointers with while i < j: i = 0 j = len(heights)-1
        # we need to find all the legal open squars between the bars
        # we can have a k with while loop: k=[i+1] but < j
        # OR for loop through for k in range(i+1,j)
        # need min height between two bars: min_h = min(height[i],height[j])
        # if height[k] <= min_h: total += min_h-height[k] if min_h-height[k] > 0
        # height we can guarantee for sure that the open squares of the bar heights are include
        # the intuition is that as we go more to the center, we end up collecting the upward sq
        # BUT we need to make sure we don't double count some squares
        # we need to add back the squares counted for the old min so we can add an old min trac
        # inc higher or lower height? we only want to keep our highest height to maximize 
        # so inc lower
        # if height[i] < height[j]: i += 1 else j-=1 
        # here we need two loops and O(1) space

        i = 0; j = len(height)-1
        total = 0
        old_min = 0
        while i < j:
            if height[i] > old_min and height[j] > old_min: #means that there is a bar that matters
                min_h = min(height[i],height[j])
                for k in range(i+1,j):
                    if height[k] < min_h:

                        total += min_h-height[k] #ideally this line only includes curr_contribution
                        if height[k] < old_min:
                            total -= old_min-height[k]
                old_min = min_h
                #print(total)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return total
