from functools import reduce
def verify_sum(paths, given_sum):
    return list(filter(lambda path: reduce((lambda a, b: a + b), path) == given_sum, paths))
path1 = [5,4,11,7]
path2 = [5,4,11,2]
path3 = [5,8,4,1]
path4 = [5,8,4,5]
given_sum = 22
print (verify_sum([path1, path2, path3, path4], given_sum))
