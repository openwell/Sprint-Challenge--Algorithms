#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) Quadratic/Polynomial: O(n^3)


b) Quadratic/Polynomial: O(n^2)


c) Linear

## Exercise II

n = total stories of building (ex: 25 stories) f = highest floor from which eggs are not broken when dropped

Goal: Determine the value of f in a way that breaks the least number of eggs (in least amount of attempts)

Psuedocode:

declare highest floor of building ( n )
go to highest floor of building, so that current floor equals highest floor ( c = n )
from current floor, determine middle floor ( m = c/2 ) 4. from new current floor, drop 1 egg ( new_c = m ) 5. if egg breaks, go back to step 3 6. if egg does not break, add 1 to new current floor ( new_c + 1 ) 7. if egg does not break, go back to step 6 8. if egg breaks, then the highest floor from which eggs are not broken when dropped is the new current floor ( return f = new_c ) END
