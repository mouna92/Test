from scipy.spatial import distance
import numpy

coords =[(2810125  , 1002710),(4023834  , 4748684),(1312573 , 8418602), (4038083 , 9103890),(8637793  , 2528606),(988534 , 8667395),(8899296 , 9013490)]

array=distance.cdist(coords, coords, 'euclidean') # cdist Computes distance between each pair of the two collections of inputs.

print(array)
print("place" ,numpy.argmax(array))


