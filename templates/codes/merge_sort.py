
def merge_sort(array):
    ## base case 1: 
    if len(array) == 1:
        return array
    
    ## base case 2:
    if len(array) == 2:
        minv = min(array[0], array[1])
        maxv = max(array[0], array[1])
        return [minv, maxv]
    n = len(array)
    mid = (n  - 1) // 2
    array1 =  merge_sort(array[:mid+1])
    array2 = merge_sort(array[mid+1:])

    sorted_array = combine(array1, array2)
    return sorted_array

def combine(array1, array2):
    """
    combine array1 and array2 in sorted order.
    both array1 and array2 are in sorted order 
    """
    array = [0 for _ in range(len(array1) + len(array2))]
    i = j = k = 0
    while i < len(array1) and j < len(array2):
        if array1[i] <= array2[j]:
            array[k] = array1[i]
            i += 1
        else:
            array[k] = array2[j]
            j += 1
        k += 1
    
    while i < len(array1):
        array[k] = array1[i]
        i += 1
        k += 1
    while j < len(array2):
        array[k] = array2[j]
        j += 1
        k += 1
    
    return array
        
array = [-74,48,-20,2,10,-84,-5,-9,11,-24,-91,2,-71,64,63,80,28,-30,-58,-11,-44,\
    -87,-22,54,-74,-10,-55,-28,-46,29,10,50,-72,34,26,25,8,51,13,30,35,-8,50,65,\
        -6,16,-2,21,-78,35,-13,14,23,-3,26,-90,86,25,-56,91,-13,92,-25,37,57,-20,\
            -69,98,95,45,47,29,86,-28,73,-44,-46,65,-84,-96,-24,-12,72,-68,93,57,\
                92,52,-45,-2,85,-63,56,55,12,-85,77,-39]
rst = merge_sort(array)
expected = [-96,-91,-90,-87,-85,-84,-84,-78,-74,-74,-72,-71,-69,-68,-63,-58,\
    -56,-55,-46,-46,-45,-44,-44,-39,-30,-28,-28,-25,-24,-24,-22,-20,-20,-13,\
        -13,-12,-11,-10,-9,-8,-6,-5,-3,-2,-2,2,2,8,10,10,11,12,13,14,16,21,\
            23,25,25,26,26,28,29,29,30,34,35,35,37,45,47,48,50,50,51,52,54,\
                55,56,57,57,63,64,65,65,72,73,77,80,85,86,86,91,92,92,93,95,98]
assert rst == expected