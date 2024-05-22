from abc import ABC, abstractmethod

#1 strategy Interface
class Strategy(ABC):
    @abstractmethod
    def do_operation(self, num1, num2):
        pass

#2 conrete classes

class OperationAdd(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2
    
class OperationSub(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2
    
class OperationDev(Strategy):
    def do_operation(self, num1, num2):
        return num1 / num2
    
class OperationMul(Strategy):
    def do_operation(self, num1, num2):
        return num1 * num2
    
    
class Context:
    def __init__(self, strategy :Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy : Strategy):
        self._strategy = strategy
    
    def excute_strategy(self,num1,num2):
        return self._strategy.do_operation(num1,num2)
    
# Usage

context = Context(OperationAdd())
print(context.excute_strategy(10,5)) # 15

context.set_strategy(OperationMul())
print(context.excute_strategy(10,5)) # 50

context.set_strategy(OperationSub())
print(context.excute_strategy(10,5)) # 5

