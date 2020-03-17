class Queue:
    stack1 = []
    stack2 = []

    def push(self, val):
        self.stack1.append(val)

    # 如果 stack2 为空，就把 stack1 里面的数据转移过来，
    # 如果 stack2 不为空，直接 pop stack2 最上面的值，其实就是最先
    # 进入 stack1 的那个值(FIFO)，直到 stack2 再次为空，再把 stack1 里面
    # 的数据转移过来
    def pop(self) -> int:
        if len(self.stack2) == 0:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())
            
        return self.stack2.pop()

    def isEmpty(self) -> bool:
        return len(self.stack1) == 0 and len(self.stack2) == 0