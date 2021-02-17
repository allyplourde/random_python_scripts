
##################################################
## Merge strings

##################################################
## Author: Allison Plourde
##################################################


def merge_lists(org, add, rmv):
    """ Merges two lists, removes specified items, and orders

    Keyword arguments:
    org -- original list
    add -- list of items to be added
    rmv -- list of items to be removed
    
    Output:
    res -- sorted tuple of resulting list
    """
    
    # add lists
    res_add = org + add

    # remove duplicates
    res_deduped = [] 
    [res_deduped.append(x) for x in res_add if x not in res_deduped]

    # remove specified
    res_cleaned = []
    [res_cleaned.append(x) for x in res_deduped if x not in rmv]

    # order items
    # reverse alphabetize
    res_cleaned.sort(key=lambda a: a, reverse=True)
    # sort my length
    res_cleaned.sort(key=lambda n: len(n), reverse=True)

    # typecast to immutable object
    res = tuple(res_cleaned)
    
    return res

if __name__=="__main__":

    #inputs
    originalList = ['one', 'two', 'three']
    addList = ['one', 'two', 'five', 'six']
    deleteList = ['two', 'five']   

    result = merge_lists(originalList, addList, deleteList)

    print("The result of the merge is:\n{}".format(result))