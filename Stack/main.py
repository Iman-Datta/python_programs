import sys

# Function to initialize an empty List as stack
def create():
    return []

def push(stack, element):
    stack.append(element)
    print('Item {} inserted successfully'.format(element))

def display(stack):
    print('Current stack: ',stack)

def peek(stack):
    return stack[-1]            # Negative Indexing in List

if __name__ == "__main__":
   stack = create()
   while True:
        print('\n------ Choose an operation: --------')
        print('1. Push an element inside Stack: ')
        print('2. Pop an element from Stack: ')
        print('3. Top/ Peek an element from Stack: ')
        print('4. Display Stack: ')
        print('5. Exit: ')

        choice = int(input('Enter your choice (1-5): '))

        if choice == 1:
            element = int(input('Enter  number to be pushed: '))
            push(stack, element)
        elif choice == 3:
            top = peek(stack)
            print('Last element: ',top)
        elif choice == 4:
            display(stack)
        else:
            sys.exit(1)