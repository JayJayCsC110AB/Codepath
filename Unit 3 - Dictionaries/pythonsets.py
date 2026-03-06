
def best_set(votes):
    freq = {}

    # Count votes
    for artist in votes.values():
        freq[artist] = freq.get(artist, 0) + 1
        # gets artist stores the amount its been seen sze been seen 3 times
    #use what we have to make a function that finds if its >
    max_artist = "none"
    count = 0
    for artist in freq:
        if freq[artist] >= count:
            count = freq[artist]
            max_artist = artist
    return max_artist
    """ 
    output: SZA
    Ethel Cain
    Note: SZA and Ethel Cain would both be acceptable answers for the second example
    """

    pass

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))

