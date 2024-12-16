"""
fractions.py 

Quick sample to summarise the fractions exploration from the CSER MOOC.

- ninths
- sevenths
"""

def displayFractions( denominator):
    """ Display fractions for a given denominator """
    for numerator in range( 1, 11):
        print( f" {numerator} / {denominator} = {numerator / denominator} ")


print("------- Ninths")
displayFractions( 9)

print("------- Sevenths")
displayFractions(7)