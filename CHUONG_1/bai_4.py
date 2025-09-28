class Stack:
    def __init__(self, capacity):
        self.capacity = capacity   # Sức chứa tối đa
        self.stack = []            # Dùng list để chứa phần tử

    # Thêm phần tử vào ngăn xếp
    def push(self, item):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm!")
        else:
            self.stack.append(item)

    # Lấy phần tử ra khỏi ngăn xếp
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy!")
            return None
        else:
            return self.stack.pop()

    # Kiểm tra rỗng
    def isEmpty(self):
        return len(self.stack) == 0

    # Kiểm tra đầy
    def isFull(self):
        return len(self.stack) == self.capacity

    # Đếm số phần tử
    def count(self):
        return len(self.stack)

    # In ngăn xếp
    def print(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng!")
        else:
            print("Các phần tử trong ngăn xếp:", self.stack)


# --- Test ---
s = Stack(5)
s.push(10)
s.push(20)
s.push(30)
s.print()            # In ra [10, 20, 30]
print("Pop:", s.pop())  
s.print()
print("Số phần tử:", s.count())