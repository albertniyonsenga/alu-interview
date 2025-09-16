#!/usr/bin/python3
"""Calculates the fewest number of operations needed
to result in exactly n (H) characters in the file"""

def minOperations(n):
    """Return the minimum number of operations for n"""
    oper = 0
    div = 2
    
    if n < 2:
        return 0
    
    while n > 1:
        while n % div == 0:
            oper += div
            n //= div
        div += 1
    return oper
