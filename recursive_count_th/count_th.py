'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurrences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    n=0
    if len(word) < 2:
        return 0

    count = 1 if ((word[n] + word[n+1]) == 'th') else 0
    return count + count_th(word[1:])
    # TBC
    
    # pass
print(count_th('tiiththth'))



