
def push(input_list, elem):
    input_list.append(elem)
    return

def stack_pop(input_list):
    if len(input_list) < 1:
        return 
    elem = input_list.pop()
    return elem

def is_empty(input_list):
    return len(input_list) == 0


def peek(input_list):
    if len(input_list) < 1:
        return 
    return input_list[-1]

s="prasad"

stack=[]

for i in s:
    push(stack,i)
  
reversed_str=""
while not is_empty(stack):
    reversed_str+=stack_pop(stack)
print(reversed_str)
    
