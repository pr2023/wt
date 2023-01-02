A = [1,2,3]
B = [5,3,2]
 
dis = 0
 
for i in range(len(A)):
    dis += abs(A[i] - B[i])
 
print("First Array is: ", A)
print("Second Array is: ", B)
print("Manhattan Distance is: ", dis)
