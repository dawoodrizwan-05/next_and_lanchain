from langchain.tools import tool
from sympy import *
import numpy as np


@tool
def Matrix_Det(given_list:list) -> list:
    """calculate matrix\'s determinent"""
    Inverse_mat=None
    print("in matrix det")
    #convert the string to python code
    
    Generated_matrix=Matrix(given_list)

    determinent = Generated_matrix.det()
    if(determinent!=0):
        return 0
    return determinent


@tool
def Matrix_Adj(given_list:list) -> list:
    """calculate Adjoint  of a matrix"""
    Adj_mat=None
    print("in matrix adj")
    #convert the string to python code
    
    Generated_matrix=Matrix(given_list)

    adjoint = Generated_matrix.adjugate()
    return adjoint


@tool
def Inverse_Of_Matrix(given_list:list) -> list:
    """calculatethe inverse of a matrix"""
    
    print("in matrix inv")

  
    Generated_matrix=Matrix(given_list)
    try:
        inverse = Generated_matrix.inv()
        return np.array(inverse,dtype='float64')
    except:
        return f"""determinent is zero """
    

@tool
def Matrix_Product(given_list: list) -> dict:
    """calculate the product of two matrices"""
    print("in matrix product")
    #exract the matrices from the given list seperated by semi colon
    lists_str = given_list

    # Use eval() on each part to convert them into actual lists
    list1 = lists_str[0]
    list2 = lists_str[1]
    #convert the string to sympy matrix
    Mat_1 = Matrix(list1)
    Mat_2 = Matrix(list2)
    #multiply the matrices
    Product = Mat_1*Mat_2
    #return the product
    return {f"Product of matrices {Mat_1} and {Mat_2}":Product}


@tool
def is_Polynomial(expression)-> int:
    """Detemine Whether a given expression in one variable is Polynomial or not"""
    x=symbols('x')
    try:
        poly_expr=Poly(expression,x)
        return True
    except:
        return False
    

@tool
def isRationalExpression(Num,Den)->int:
    """To confirm whther an algebraic expression is rational or not"""
    numerator=sympify(Num)
    denominator=sympify(Den)
    x,y,z=symbols('x y z')
    if(denominator!=0):
        try:
            num=Poly(numerator,x)
            den=Poly(denominator,x)
            print(den)
            return True
        except:
            return False
    else:
        return False
    

@tool
def ReducedToLowestForm(num,den)->int:
    """ To simplify expression by reducing it to lowest form"""
    Num=sympify(num)
    Den=sympify(den)

    HCF=gcd(Num,Den)
    new_num=factor(div(Num,HCF))[0]
    new_den=factor(div(Den,HCF))[0]
    return new_num/new_den


@tool
def SubstituteInExpression(expression,**kwargs)->int:
    """to evaluate expression by substituting values in it"""
    exp=sympify(expression)
    substitutions = {symbols(key): value for key, value in kwargs.items()}
    print(substitutions)
    
    return exp.subs(substitutions) 
#making list of all availbale tools
tools = [Matrix_Adj, ReducedToLowestForm, isRationalExpression, SubstituteInExpression, is_Polynomial, Matrix_Det, Inverse_Of_Matrix, Matrix_Product]
