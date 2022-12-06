def trainingNet(weight,bias,polaInput,typeOutput):

    newWeight=[]
    for i in range(0,len(weight)):
        row=[]
        for j in range(0,len(weight[i])):
            a = weight[i][j] + polaInput[i][j] * typeOutput
            row.append(a)

        newWeight.append(row)

    newBias = bias + typeOutput

    return [
        newWeight,
        newBias
    ]

def bipolarActivation(val):
    if(val < 0):
        return -1

    return 1

def sumFunc(weight,bias,inputVal):
    tambah=0
    for i in range(0,len(weight)):
        for j in range(0,len(weight[i])):
            tambah += weight[i][j] * inputVal[i][j]

    tambah+=bias
    tambah=bipolarActivation(tambah)
    return tambah

    



pola1=[
    [1,1,1],
    [-1,1,-1],
    [-1,1,-1],
]

pola2=[
    [1,-1,1],
    [1,-1,1],
    [1,1,1],
]

weight=[
    [0,0,0],
    [0,0,0],
    [0,0,0],
]
bias=0



train1= trainingNet(weight,0,pola1,1)

train2= trainingNet(train1[0],train1[1],pola2,-1)


# print(train2)


aa = sumFunc(train2[0],train2[1],pola2)

# print(aa)




## Testing 

pola3=[
    [1,1,-1],
    [-1,1,-1],
    [1,1,-1]
]

aa = sumFunc(train2[0],train2[1],pola3)

print(aa)