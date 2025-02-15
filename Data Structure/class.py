class Stack:
    def __init__(self, pOne: int, pTwo: str, pThree: bool):
        self.mark = pOne
        self.name = pTwo
        self.status = pThree
        
    def show(self):
        print(f'Name: {self.name}, Mark: {self.mark}, Qualified: {self.status}')

if __name__ == "__main__":
    ref_stack: Stack = Stack(99, 'Iman', True)
    ref_stack.show()
    print(f'Data is {ref_stack}')



# class Stack:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)  # Dynamically set attributes from kwargs

#     def show(self):
#         print(', '.join(f'{key}: {value}' for key, value in self.__dict__.items()))

# if __name__ == "__main__":
#     ref_stack1 = Stack(mark=99, name='Iman', status=True)
#     ref_stack1.show()

#     ref_stack2 = Stack(mark=85, name='Alex')  # No status provided
#     ref_stack2.show()

#     ref_stack3 = Stack(name="John")  # Only one attribute
#     ref_stack3.show()
