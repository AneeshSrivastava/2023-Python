# Source: https://youtu.be/KxgBB3-Z7wc

def argument_function(*args: str):
    print('Following args are passed in function call:')
    print(args)
    print('type of args: ', type(args))
# argument_function('argument_1', 'argument_2','argument_3')


def argument_function_with_normal_args(name:str ,*args: str):
    if name == 'Aneesh':
        greeting: str= 'Hola! '
    else:
        greeting: str= 'Bonjour! '
    
    for arg in args:
        print(greeting, arg)

argument_function_with_normal_args('Guru', 'how are you?','hope you are well')
