A=[]
for v in range(8):
    A.append(int(input('Enter a Number :')))

print(A)

def selectionSort(A):
    n = len(A)
    for j in range(0,n-1):
        smallest = j
        for i in range(j+1,n):
            if A[j] < A[smallest]:
                smallest = i
            A[j],A[smallest] = A[smallest], A[j]

selectionSort(A)
print('Sorted Array :', A)
