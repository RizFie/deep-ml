import numpy as np

def product_rule_derivative(f_coeffs: list, g_coeffs: list) -> list:
    """
    Compute the derivative of the product of two polynomials.
    
    Args:
        f_coeffs: Coefficients of polynomial f, where f_coeffs[i] is the coefficient of x^i
        g_coeffs: Coefficients of polynomial g, where g_coeffs[i] is the coefficient of x^i
    
    Returns:
        Coefficients of (f*g)' as a list of floats rounded to 4 decimal places
    """
    # Your code here
    results = []
    for i in range(len(f_coeffs) + len(g_coeffs)-1):
        results.append(0.0)

    for i in range(len(f_coeffs)):
        for j in range(len(g_coeffs)):
            results[i+j] = results[i+j] + (f_coeffs[i] * g_coeffs[j])
    print(f'results: {results}')

    fg_coeffs = []
    for i in range(len(results)):
        product = round((i*results[i]),4)
        print(f'Product: {product}')
        if product == 0:
            fg_coeffs.append(0.0)
        else:
            fg_coeffs.append(product)
    print(f'fg_coeffs: {fg_coeffs}')

    if len(fg_coeffs) > 1:
        del fg_coeffs[0]
        return fg_coeffs
    else:
        return fg_coeffs
    