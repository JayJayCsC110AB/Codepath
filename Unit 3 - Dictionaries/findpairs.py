"""
Given an array of integers popularity_scores representing the popularity scores of songs in a music festival playlist, return the number of popular song pairs.

A pair (i, j) is called popular if the songs have the same popularity score and i < j.

Hint: number of pairs = (n x n-1)/2

4
6
0"""


def num_popular_pairs(popularity_scores):
    scores = {}
    pairs = 0
    for values in popularity_scores:
        scores[values] = scores.get(values, 0) +1

    for values in scores:  
        pairs += (scores[values] * (scores[values]-1))//2
    return pairs
            


popularity_scores1 = [1, 2, 3, 1, 1, 3]
popularity_scores2 = [1, 1, 1, 1]
popularity_scores3 = [1, 2, 3]

print(num_popular_pairs(popularity_scores1))
print(num_popular_pairs(popularity_scores2))
print(num_popular_pairs(popularity_scores3)) 

