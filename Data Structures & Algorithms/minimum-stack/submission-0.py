class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = [inf, inf] # first shows first_min, second shows second min

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < min_val:
            # assign this to min val and also assign this to other val
            min_val[1] = min_val[0]
            min_val[0] = val

    def pop(self) -> None:
        
        # pop it out,

        # if it is second least element - measn only one remainging.
        if self.stack[-1] == min_val[1]:
            min_val[1] = inf
        
        if self.stack[-1] == min_val[0]:
            min_val[0] = min_val[1]
            min_val[1] = inf

        #if it is not first, second least element
        return self.stack.pop()

        
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val[0]
