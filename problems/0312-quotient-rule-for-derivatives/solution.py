import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g_x = 0 #v
    for i in range(len(g_coeffs)-1,-1,-1):
        g_x += g_coeffs[i]*x**abs(i-(len(g_coeffs)-1))
    print(f'g_x: {g_x}')

    g_xp = 0 #vp
    for i in range(len(g_coeffs)-2,-1,-1):
        g_xp += (abs(i-(len(g_coeffs)-1))*g_coeffs[i])*x**(abs(i-(len(g_coeffs)-1))-1)
    print(f'g_xp: {g_xp}')

    h_x = 0 #u
    for i in range(len(h_coeffs)-1,-1,-1):
        h_x += h_coeffs[i] * x ** abs(i - (len(h_coeffs) - 1))
    print(f'h_x: {h_x}')

    h_xp = 0 #up
    for i in range(len(h_coeffs)-2,-1,-1):
        h_xp += (abs(i-(len(h_coeffs)-1))*h_coeffs[i])*x**(abs(i-(len(h_coeffs)-1))-1)
    print(f'h_xp: {h_xp}')

    # ((v*up)-(u*vp))/v**2
    quotient = (((h_x*g_xp)-(g_x*h_xp))/h_x**2)

    return quotient