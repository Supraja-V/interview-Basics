
def one(c,x):
    return c+int(x)
def two(c,x):
    return c-int(x)
def three(c,x):
    return c*int(x)
def four(c,x):
    return c/int(x)

    
if __name__ == "__main__":
    a = input()
    l = list(a)
    n = ['1','2','3','4','5','6','7','8','9']
    operand = []
    operator = []
    print(l)
    for i in l:
        if i not in n:
            operator.append(i)
        else:
            operand.append(i)
    switcher = {
        '+': one,
        '-': two,
        '*': three,
        '/': four
    }
    
    c = int(operand[0])
    for i in range(1,len(operand)):
        
        func = switcher.get(operator[i-1])
        c = func(c,operand[i])
    print(c)
    
            
            
    