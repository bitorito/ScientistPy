import numpy as np

a =np.array( [[[0, 1, 1],

                [0, 0, 0],
                [1, 1, 1]],

                [[0, 1, 1],
                [0, 0, 0],
                [1, 1, 1]],

                [[0, 1, 1],
                [0, 0, 0],
                [1, 1, 1]]]
                )

print (a)
print( a.shape)

c=np.matmul(a,a)
print(c)


