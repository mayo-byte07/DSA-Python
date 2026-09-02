class StockSpanner(object):

    def __init__(self):
        # Stack will store tuples of (price, span)
        self.stack = []

    def next(self, price):
        span = 1
        
        # While stack is not empty and the current price is greater than or equal 
        # to the price at the top of the stack
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
            
        self.stack.append((price, span))
        return span