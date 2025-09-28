class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.arr = []

    def push(self, value):
        if self.isFull():
            print("Stack đầy, không thể push!")
            return
        self.arr.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack rỗng, không thể pop!")
            return None
        return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0

    def isFull(self):
        return len(self.arr) == self.capacity

    # Hàm count
    def count(self):
        return len(self.arr)


# Test
if __name__ == "__main__":
    st = Stack(5)
    st.push(1)
    st.push(2)
    st.push(3)
    print("Số phần tử hiện tại trong stack:", st.count())
    st.pop()
    print("Sau khi pop, số phần tử:", st.count())
