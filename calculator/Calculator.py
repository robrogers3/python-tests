from stacks import Stack
import re

class Calculator():
    def __init__(self):
        self.operators = Stack()
        self.operands  = Stack()
        self.operatorsMap = {'/': 2, '*': 2, '-': 1, '+': 1, '(': 0, ')': 0}

    def evaluate(self, expression):
        if expression is None or len(expression) == 0:
            return 0

        expression = expression.split(' ')

        for ch in expression:
            if self.isOperand(ch):
                self.operands.push(int(ch))
            elif ch == '(':
                self.operators.push(ch)
            elif ch == ')':
                while self.operators.peek() != '(':
                    self.process()

                self.operators.pop()

            elif self.isOperator(ch):
                while not self.operators.empty() and self.precedence(self.operators.peek()) >= self.precedence(ch):
                    self.process()

                self.operators.push(ch)

        while not self.operators.empty():
            self.process()

        return self.operands.pop()

    def process(self):
        map = {'+': self.add, '-': self.sub, '*': self.multi, '/': self.divide}
        right = self.operands.pop()
        left = self.operands.pop()
        operator = self.operators.pop()
        func = map[operator]
        r = func(left, right)
        self.operands.push(r)

    def isOperand(self,char):
        return re.match(r'^\d+$', char) is not None

    def isOperator(self, char):
        return char in self.operatorsMap

    def precedence(self, operator):
        if operator not in self.operatorsMap:
            raise Exception(f"unknown operateor {operator}")

        return self.operatorsMap[operator]

    def add(self, left, right):
        return left + right

    def sub(self, left, right):
        return left - right

    def divide(self, left, right):
        return left / right

    def multi(self, left, right):
        return left * right
