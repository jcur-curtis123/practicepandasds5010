from timer import Timer
import random
import numpy as np



def make_list(n=10000000, k=1000):
    """
    returns a list of n random numbers (each between 1 and k) 
    """
    return [random.randint(1,k) for _ in range(n)]

def square_list(li):
    """
    Expects a list of ints
    returns a new list of all items in li, squared
    """
    x = []
    for i in range(len(li)):
        x.append(li[i] ** 2)
    return x

def make_np_arr_from_list(li):
    return np.array(li)

def square_np_arr(np_arr):
    return np_arr ** 2

    
def make_np_arr_directly(n=10000000, k=1000):
    # make a 1 dimensional arr that contains random numbers between 1 and k
    return np.random.randint(1, k+1, n) 

'''
refactored main() to support the time.py 

computes time for the following functions
'''
def main():
    rand_list = make_list()
    rand_np_arr = make_np_arr_from_list(rand_list)
    squared = square_list(rand_list)
    # squared = square_list(rand_np_arr)
    print(squared[:10])
    
    '''
    return the time to build the python list of size n (1,000,000)
    '''

    print("Timing make_list():")
    with Timer():
        rand_list = make_list()

    '''
    time to square the rand_list 

    print first 10 elements in squared list
    '''
    print("Timing square_list():")
    with Timer():
        squared_list = square_list(rand_list)
        print(squared_list[:10])

    '''
    time to convert list to numpy array and square using vectorization
    '''    
    print("Timing make_np_arr_from_list:")
    with Timer():
        rand_np_arr = make_np_arr_from_list(rand_list)
        squared_np = square_np_arr(rand_np_arr)
        print(squared_np[:10])

    '''
    time to execute squared random integers directy with numpy
    '''    

    print("Timing make_np_arr_directly(): ")
    with Timer():
        rand_np_direct = make_np_arr_directly()
        squared_np_direct = square_np_arr(rand_np_direct)
        print(squared_np_direct[:10])

if __name__ == "__main__":
    main()