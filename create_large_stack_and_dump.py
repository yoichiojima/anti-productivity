from random import randint

def create_large_stack_and_dump():
    # create large stack
    stack = []
    for i in range(100000000000):
        stack.append(randint(1, 10000000000))
    # dump
    stack = None
    
    
if __name__ == "__main__":
    create_large_stack_and_dump()
