


#1)
def arithmetic_mean(a:int,b:int,c:int):
    """
    The function calculates the arithmetic mean of 3 values.
    
    Arguments
    ---------
    positional:
        a : 'int'
        b : 'int'
        c : 'int'
        
    Returns
    -------
        'float'
            The arithmetic mean of 3 numbers.
    
    If at least one of the function parametrs isn't an integer, then function returns -1   
    
    """ 
    if (not isinstance(a,int)) or (not isinstance(b,int))  or (not isinstance(c,int)):
        return -1
    
    return (a+b+c)/3



#2)
def count_of_evens(list_integers:list):
    """
    The function calculates count of even numbers in list.
    
    Arguments
    ---------
    positional:
        list of integers : 'list'
        
    Returns
    -------
        'int'
            count of even numbers.
            
    """
    list_evens=[item for item in list_integers if item%2==0]
    
    return len(list_evens) 
        


#3)
def is_corresponds_rules(password:str):
    """
    The function checks if the given ​password ​corresponds to the password rules.
    
    Arguments
    ---------
    positional:
        password : 'string'
        
    Returns
    -------
        'bool'
        
            (1) 'True'  : If  1)the length of the password least 10
                                             and 
                              2)the password have a at least 2 numbers
            (2) 'False' : In all other cases
            
    If type of function parametr isn't string, then function returns 'Error'

    """
    if not isinstance(password,str):
        return "Error: Function parametr should be string!"
    is_corresponds=False
    if (len(password)>=10):
        digits='0','1','2','3','4','5','6','7','8','9'
        count=0
        for item in digits:
            if (item in password):
                count+=1
        if count>=2:
            is_corresponds=True
            
    return is_corresponds
                
        

#4)
def print_name_greeting(name:str,greeting:str="Welcom to our company!"):
    """
    The function prints the received arguments․
    
    Arguments
    ---------
    positional:
        name : 'string'
    optional:
        greeting : 'string' --> default greeting=="Welcom to our company!" 
        
    Returns
    -------
        no return values
        
    """
    print(name,greeting)
    


#5)
def function5(name:str,*args:int):
    """
    Arguments
    ---------
    positional:
        name  : 'string'
    optional:
        *args (undefined number of non-keyword integers) : 'int'
        
    Returns
    -------
        no return values
        
    If function don't get a optional arguments, then the function prints
    the 'name' positional argument else prints arithmetic mean of optional arguments    
    """
    if len(args)==0:
        print("No grades availble for %s" %name)
    else:
        print("%s, your average grade is: ​%.2f" %(name, sum(args)/len(args)))



#6)
def function6(user:str,**kwargs):
    """
    Arguments
    ---------
    positional:
        user : 'string'
    optional:
        **kwargs (undefined number of keyword arguments) : any type
        
    Returns
    -------
        no return values
        
    If 'user' don't equale 'admin' the function prints  'access denied to the user'
    else prints optional values's  name and value
    """
    if user!="admin":
        print("access denied to the user %s" %user)
    else:
        for key in kwargs:
            print(key,":",kwargs[key])



























