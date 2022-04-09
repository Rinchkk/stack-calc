class Stack:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        try:
            assert self.is_empty()
            return self.items.pop()
        except AssertionError:
            print("Error: stack is empty")

    def peek(self):
        try:
            assert self.is_empty()
            return self.items[-1]
        except AssertionError:
            print("Error: stack is empty")

def main():
    arr = list(map(str, input().split())) #Я не смогла нагуглить как считать в питоне элементы, записанные в одной строке, но имеющие разный тип данных
    stack = Stack()
    CONST_STR = "+-*/"
    CONST_S1 = '+'
    CONST_S2 = '-'
    CONST_S3 = '*'
    for item in arr:
        if CONST_STR.find(item) == -1:
            stack.push(int(item))
        else:
            val1 = int(stack.pop())
            val2 = int(stack.pop())
            if item == CONST_S1:
                stack.push(val2 + val1)
            elif item == CONST_S2:
                stack.push(val2 - val1)
            elif item == CONST_S3:
                stack.push(val2 * val1)
            else:
                stack.push(val2 // val1)

    print(stack.peek())

if __name__ == '__main__':
    main()
