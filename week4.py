def qan_tic():
    tic = "QAN.AX"
    print(tic)

res = qan_tic()
print(res)

def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

print(qan_tic)



def qan_tic():
    tic = "QAN.AX"
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()

def qan_tic():
    print(tic)
    return tic

tic = "WES.AX"
print(tic)
qan_tic()



test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]

def is_even_num(lis):
    evennum = []
    for n in lis:
        if n % 2 == 0:
            evennum.append(n)
    return evennum
print(is_even_num(test_list))


lst = [2,3,10,14,20,21,25,13,15]
new_list = [x**2 for x in lst if x**2>150]
print(f'the new list with value of square greater than 150 is {new_list}')


numbers = [0,1,1,2,5,6,8,2,4,6,8]
result = list({i for i in numbers if i % 2==0})
result.sort()
print(result)






