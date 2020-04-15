


#1)
def my_max(*args):
    """
    The function accepts undefined number of optional non-keyword 
    arguments type of integer and returns maximum value of their.
       If at least one of the function parameters isn't an integer
       function returns 'Error'.
    
    Arguments
    ---------
    optional:
        *args (undifined number of integers) : 'int'
        
    Returns
    -------
        'int'
            maximum element of function parametrs.
            
    """
    if len(args)==0:
        return 'no numbers given'
    
    max_num = args[0]
    
    for i in range(len(args)):
        if not isinstance(args[i],int):
            return 'Error! type of function parametrs should be integer'
        if args[i] > max_num:
            max_num = args[i]
            
    return max_num



#2)
def unique_values(list_of_any_values:list):
    """
    The function separates unique values of list
    
    Arguments
    ---------
    positional:
        list_of_any_values : 'list'
        
    Returns
    -------
        'list'
            list of unique values
            
    """
    new_list=[]
    duplicates={}
    
    for item in list_of_any_values:
        duplicates[item]=list_of_any_values.count(item)
    
    for item in duplicates:
        if duplicates[item]==1:
            new_list.append(item)
    
    return new_list
        

#3)
def fibonacci_number(n:int):
    """
    The function calculate Fibonacci number.
    
    Arguments
    ---------
    positional:
        n : 'int'
            number of sequence Fibonacci
            
    Returns
    -------
        'int'
            n-th fibonacci number
            
    If function parametr isn't integer or it
    small or equal to zero function returns -1

    """
    if (not isinstance(n,int)) or (n<=0) : return -1
    if n==1 : return 0
    if n==2 : return 1
    x,y=0,1
    for i in range(2,n):
        x,y=y,x+y
    return y    
    

#4)
def my_func(n:int):
    if n<10: return n+10
    return n-10 
    
l1=[1,2,3,4,5,10,11,12,13,14,15]
new_list=list(map(my_func,l1))




    
    
    
    
    
    
    
    
    






