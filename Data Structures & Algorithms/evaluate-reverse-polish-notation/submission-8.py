class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # traverse the list using for loop
            #if curr is a digit store number:first and second
            # else go through if statements and apply correct operation.
                # move result to first number to get ready for second number
        numbers = []
        for token in tokens:
            if token.isdigit():
                numbers.append(int(token))
            elif token[0]=="-" and token[1:].isdigit():
                numbers.append(-int(token[1:]))
                #print(token)
            elif token == "+":
                #print(numbers.pop()+numbers.pop())
                numbers.append(numbers.pop()+numbers.pop())
            elif token == "-":
                second_num = numbers.pop()
                first_num = numbers.pop()
                numbers.append(first_num-second_num)
            elif token == "*":
                numbers.append(numbers.pop()*numbers.pop())
            elif token == "/":
                second_num = numbers.pop()
                first_num = numbers.pop()
                numbers.append(int(first_num/second_num))
                '''
                if  (first_num < 0 and second_num > 0) or (first_num > 0 and second_num <0) :
                    #print(abs(first_num)//abs(second_num))
                    what = abs(first_num)//abs(second_num)
                    numbers.append(-what)
                else:
                    numbers.append(first_num//second_num)
                '''
                
            #print(numbers)
        return numbers.pop()
        