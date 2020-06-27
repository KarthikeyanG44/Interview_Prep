import numpy as np

def euclidean(l1,l2):
        diff_vector = l1 - l2
        norm_val = np.linalg.norm(diff_vector,ord=2)
        return norm_val
### Problem 1 - Lloyd Clustering ####
# p1 = np.array([5.1,3.5])
# p2 = np.array([4.9,3])
# p3 = np.array([7.3,2.3])
# p4 = np.array([6.7,2.5])
# p5 = np.array([7.2,2.1])
# p6 = np.array([4.5,3.4])


##### Problem 2 - kNN Algorithm ####
p1 = np.array([4.5,1.3])
p2 = np.array([4.7,1.6])
p3 = np.array([3.3,1])
p4 = np.array([4.6,3.1])
p5 = np.array([5,3.6])
p6 = np.array([5.4,3.9])
test_pt = np.array([4.5,1.7])
distances = []
data = [p1,p2,p3,p4,p5,p6]

for idx,point in enumerate(data):
    dist = euclidean(test_pt,point)
    distances.append((dist,idx+1))

distances.sort(key = lambda variable: variable[0])
