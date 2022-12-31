class Stack:
    
    # O(n) time
    # O(n) space
    
    def __init__(self, numOfStacks):
        self.list = []
        self.pointers = [-1]*numOfStacks
        self.notNumber = {}


    def pop(self, stack_number):
        # pop like normal
        self.pointers[stack_number] -= 1
        # check if -2 or equal to another stacks's pointer
        if self.pointers[stack_number] == -2:
            raise MemoryError("Stack Underflow Error")
        
        for pointer in self.pointers:
            if self.pointers.index == stack_number:
                pass
            if pointer == self.pointers[stack_number] and pointer != -1:
                raise MemoryError("Stack Underflow Error")
        
        return self.list[self.pointers[stack_number]]


    def push(self, item, stack_number):
        
        # not first element in stack n
        if self.pointers[stack_number] != -1:
            # add element into list at point of stack's pointer
            self.list = self.list[:self.pointers[stack_number]+1] + [item] + self.list[self.pointers[stack_number]+1:]
    
            # increment all pointers of stacks that are this stack or are after this stack
            for num in self.notNumber[stack_number]:
                self.pointers[num] += 1
        
        # first element in stack n
        else:
            # append item to list
            self.list.append(item)
            self.largestPointer = self.pointers.index(max(self.pointers))
            # pointer of stack will be end of list
            self.pointers[stack_number] = len(self.list) - 1
            
            # set the values of notNumber
            temp = []
            for i in range(len(self.pointers)):
                try:
                    self.notNumber[i]
                except KeyError:
                    temp.append(i)
            self.notNumber[stack_number] = temp
            
    def peek(self, stack_number):
        return self.list[self.pointers[stack_number]]
            
    def getList(self):
        return self.list
                
        
threeWayStack = Stack(3)

# [(s2) 1,2,3, (s0) 1,2,5, (s1) 1,2,3,4]

threeWayStack.push(1,2)
threeWayStack.push(1,0)
threeWayStack.push(1,1)
threeWayStack.push(2,2)
threeWayStack.push(2,1)
threeWayStack.push(2,0)
threeWayStack.push(3,1)
threeWayStack.push(4,1)
threeWayStack.push(3,2)
threeWayStack.push(5,0)

l = threeWayStack.getList()
print(l)
print(threeWayStack.peek(0),threeWayStack.peek(1),threeWayStack.peek(2))
        
secondStack = Stack(3)
secondStack.pop(1)

