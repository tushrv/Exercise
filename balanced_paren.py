class Stack(object): # class to define stack data structure
    def __init__(self,limit=10):
        self.stack = []
        self.limit = limit
    def __str__(self): # return whole stack
        return ' '.join(self.stack)
    def push(self,data): # push data into stack
        if len(self.stack) >= self.limit:
            print('Stack OverFlow !!')
        else:
            self.stack.append(data)
    def pop(self): # pop data out of stack
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack.pop()
    def peek(self): # return the top most element of the stack
        if len(self.stack) <= 0:
            return -1
        else:
            return self.stack[len(self.stack)-1]
    def isEmpty(self):
        return self.stack==[]
    def size(self): # returns size of the stack
        return len(self.stack)

def parse_paren(parenthesis):
    balanced = 1 # 1-> Balanced
    index = 0 
    myStack = Stack(len(parenthesis))
    while (index<len(parenthesis)) and (balanced==1):
        check = parenthesis[index]
        if check == '(':
            myStack.push(check)
            # print(check)
        else:
            if myStack.isEmpty():
                balanced = 0
            else:
                s = myStack.pop()
        index+=1
    if balanced==1 and myStack.isEmpty():
        # print('Balanced')
        return True
    else:
        # print('Not Balanced')
        return False
    
if __name__ == '__main__':
    print(parse_paren('(()(()))')) #True
    print(parse_paren('(()))')) # False
             


