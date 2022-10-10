"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    strItems = []
    for item in items:
        strItems.append(str(item))

    frequencies = {item: strItems.count(item) for item in strItems}

    return frequencies
