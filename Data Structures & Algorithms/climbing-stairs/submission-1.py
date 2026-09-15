class Solution:
    def climbStairs(self, n: int) -> int:
        #brute force way is to find all the combos of 1 and 2 that fit in n
        # but this is repititive in taht you keep iterating through 1:n
        # figure out odd or even
        # we can figure out how many two are needed by doing (n-1)/2 and n/2
        # then we can replace each two with one

        one = 1
        two = 1
        for i in range(n-1):
            tmp = one
            one = one + two
            two = tmp
        return one
