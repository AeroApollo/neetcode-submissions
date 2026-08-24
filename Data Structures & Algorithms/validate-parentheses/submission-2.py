class Solution:
    def isValid(self, s: str) -> bool:
        # we can keep a running list of valid parenthesis 
        # we need a means to track the brackets in order
            # we can track the open brackets in a list and pop them when they are closed

            # if a char c belongs in a open bracket, then we store it
            # if a char c belongs in a closed bracket, we need to check if list has an eq open bracket ELSE return False
            # the numbers of bracket types is low so we couldn't if them

            # the list hs anth rem, return False else return true

        bracks = set([   '(',')'  ,    '{','}'  ,   '[',']'   ])
        close_b = set([')','}',']'])
        open_b = set(['(','{','['])
        order = []
        for c in s:
            if c not in bracks:
                continue # skips anything not related
            #anth after this is filtered to be brackets
            if c in open_b:
                order.append(c)
            # anth after this is filtered to be closed backets
            if order == []: return False
            if c == ')':
                if order[-1] != '(': return False
                order.pop()
            elif c == '}':
                if order[-1] != '{': return False
                order.pop()
            elif c == ']':
                if order[-1] != '[': return False
                order.pop()
        if len(order) > 0: return False #some brackets were not closed
        return True

