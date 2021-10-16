def reverse_list(list_1):
    '''
    This function reverses the elements of a list. 
    It takes a list as parameter.
    
    example:
      INPUT                         OUTPUT
    [4,5,6]                          [6,5,4]
    ["Red","Blue","Pink"]           ["Pink","Blue", "Red"]

    '''
    output=[]
    for i in range(len(list_1)):
        b=i+1
        a=list_1[-b] 
        output.append(a)
    print(output)
    return(output)
    
    

reverse_list([1,2,3,4,5])
reverse_list(['Apple','ball','cat','dog'])
