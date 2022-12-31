# largest range

# O(n) time | O(n) space
def largest_range(array):
    d = {}
    best_range = [[], float('inf'), float('-inf')]
    for num in array:
        d[num] = True
    

    for num in array:
        r = [[num], num, num]

        c = 1

        while d.get(num + c, False):
            d[num + c] = False
            r[0].append(num + c)
            r[1] = min(r[1], num + c)
            r[2] = max(r[2], num + c)
            c += 1
        
        c = 1

        while d.get(num - c, False):
            d[num - c] = False
            r[0].append(num - c)
            r[1] = min(r[1], num - c)
            r[2] = max(r[2], num - c)
            c += 1
        
        if d.get(num, False):
            d[num] = False
            best_range = r if len(r[0]) > len(best_range[0]) else best_range
    
    return [best_range[1], best_range[2]]
