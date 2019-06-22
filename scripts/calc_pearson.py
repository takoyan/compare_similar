import numpy as np

def upper_side(vec1, vec2):
    vec1=np.array(vec1)
    vec1=vec1-np.average(vec1)
    vec2=np.array(vec2)
    vec2=vec2-np.average(vec2)
    return np.dot(vec1, vec2.reshape(len(vec2), 1))[0]
    
def under_side(vec1, vec2):
    vec1=np.array(vec1)
    vec1=vec1-np.average(vec1)
    vec_x=np.dot(vec1, vec1.reshape(len(vec1), 1))[0]
    vec_x=np.sqrt(vec_x)
    vec2=np.array(vec2)
    vec2=vec2-np.average(vec2)
    vec_y=np.dot(vec2, vec2.reshape(len(vec2), 1))[0]
    vec_y=np.sqrt(vec_y)
    return vec_x*vec_y


def Calc_pearson(vec1, vec2):
    #print(upper_side(vec1, vec2)/under_side(vec1, vec2))
    return(upper_side(vec1, vec2)/under_side(vec1, vec2))
