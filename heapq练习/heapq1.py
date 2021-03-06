from heapq import *

def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h,value)
    return [heappop(h) for _ in range(len(h))]

if __name__=="__main__":
    print(heapsort([1,3,5,9,2]))
    a = [2,5,4,6,7,8,10,3,1]
    heapify(a)
    print(heappop(a))
    print(a)
    b = nlargest(len(a),a)
    print(type(
        b))