# from pretty_print import *
from pretty_print import (
    simple_print as sp,
    pro_print as pp
    
)


def calculate_cube(x):
    """
    The function calculate cube of integer.
    
    Argumnets
    ---------
    positional:
        x : 'int'
        
    Returns
    -------
        'int'
            The cube of received integer
    
    If type of parametr function isn't 'int' the function returns -1
        
    """
    if isinstance(x,int):
        return x**3
    return -1

def calculate_square(x):
    """
    The function calculate square of integer.
    
    Arguments
    ---------
    positional:
        x : 'int'
        
    Returns
    -------
        'int'
            The square of received integer
    
    If type of parametr function isn't 'int' the function returns -1
    """
    if isinstance(x,int):
        return x**2
    return -1

def main():
    square_of_two=calculate_square(2)
    sp(square_of_two)
    
    cube_of_four=calculate_cube(4)
    pp(cube_of_four)
    
    """
    or simply
        pp(calculate_cube(4))
        sp(calculate_square(2))
    """

if __name__ == "__main__":
    
    main()





