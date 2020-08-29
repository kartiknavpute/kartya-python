
#//written by Annonymous
def i_letter():
    a = [0 ,12 ,12  ,1 ,1 ,1 ,1 ,12 ,12 ,0]

    for i in a:
        if i == 1:
           print(i * '           * *')
        else:
           print(i * ' *')
    print('',end ='')

def l_letter():
    b = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 12, 12]
    for j in b:
        if j == 1:
            print(j * '* * *')
        else:
            print(j * '* ')


def o_letter():
    matrix = [
        [0, 0, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 2, 2, 1, 1, ],
        [0, 1, 1, 2, 2, 1, 1],
        [0, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1]

    ]
    for a in matrix:
        for row in a:
            if (row == 1):
                print(row * '* *', end=' ')

            elif (row == 0):
                print(row * '  ')
            elif (row == 2):
                print(row * '  ', end='')
            else:
                break


def v_letter():
    a = [
        [0 ,0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ],
        [0 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,2 ],
        [0 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,1 ],
        [0 ,2 ,2 ,2 ,1 ,2 ,2 ,1 ,2 ],
        [0 ,2 ,2 ,2 ,2 ,1 ,1 ,2 ,2 ,2 ],
        [0 ,2 ,2, 2, 2, 1,1 ,2 ,2 , 2],

    ]
    for b in a :
        for c in b:
            if (c==0):
                print(' ')
            elif(c==1):
                print(c * '* *',end = ' ')
            elif(c==2):
                print(c * ' ',end = '')


def e_letter():
    matrix = [
        [0,0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [0, 1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
        [0 ,1 ,1],
        [0 ,1 ,1],
        [0, 1, 1, 1, 1 ,1 ,1 ,1 ,1],
        [0, 1, 1, 1, 1 ,1 ,1 ,1 ,1],
        [0 ,1 ,1],
        [0 ,1 ,1],
        [0, 1, 1, 1, 1 ,1 ,1 ,1 ,1],
        [0, 1, 1, 1, 1 ,1 ,1 ,1 ,1],
    ]
    for a in matrix:
        for b in a:
            if (b ==0):
                print(' ')
            else:
                print('**' * b,end = ' ')


def y_letter():
    a = [
            [0,0 ,0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ],
            [0 ,2 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ,2 ],
            [0 ,2 ,2 ,1 ,2 ,2 ,2 ,2 ,1 ],
            [0 ,2 ,2 ,2 ,1 ,2 ,2 ,1 ,2 ],
            [0 ,2 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ],
            [0 , 2, 2, 2, 1, 1, 1, 2, 2],
            [0 ,2 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ],
            [0 ,2 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ],
        ]
    for b in a :
        for c in b:
            if (c==0):
                print(' ')
            elif(c==1):
                print(c * '* *',end = ' ')
            elif(c==2):
                print(c * ' ',end = '')


def u_letter():
    a = [
        [0 ,0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ],
        [0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1  ],
        [0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ],
        [0 ,1 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,2 ,1 ],
        [0 ,1 , 2, 2, 2, 2, 2, 2, 2, 2 , 1],
        [0 ,1 , 2, 2, 2, 2, 2, 2, 2, 2 , 1],
        [0 ,2 ,2 ,1 ,1 ,1 ,1 ,2, 2],
        [0 ,2 ,2 ,1 ,1 ,1 ,1 ,2, 2],

    ]
    for b in a :
        for c in b:
            if (c==0):
                print(' ')
            elif(c==1):
                print(c * '* *',end = ' ')
            elif(c==2):
                print(c * ' ',end = '')



# output is here....
i_letter(),l_letter(),o_letter(),v_letter(),e_letter(),y_letter(),o_letter(),u_letter()
# These are stupid things.....
