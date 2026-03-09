class Stack:
    def __init__(self):
        """Инициализация пустого стека."""
        self.items = []

    def is_empty(self):
        """Проверка стека на пустоту. Возвращает True или False."""
        return len(self.items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека. Метод ничего не возвращает."""
        self.items.append(item)

    def pop(self):
        """Удаляет верхний элемент стека и возвращает его. Если стек пуст, выбрасывает исключение."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Возвращает верхний элемент стека, но не удаляет его. Если стек пуст, выбрасывает исключение."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self.items)

s = Stack()
print(s.is_empty())  # True
s.push(1)
s.push(2)
s.push(3)
print(s.peek())  # 3
print(s.pop())  # 3
print(s.size())  # 2
print(s.is_empty())  # False