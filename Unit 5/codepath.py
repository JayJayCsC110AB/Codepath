""" Problem 2: Top Artists
Given the head of a linked list playlist, return a dictionary that maps each artist in the list to its frequency.

Evaluate the time complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.


class SongNode:
    def __init__(self, song, artist, next=None)
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    pass
Example Usage:

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

get_artist_frequency(playlist)
Example Output:

{ "SZA": 2, "Jimin" : 1, "Sabrina Carpenter": 1}
"""

"""
Understand:
I-  The linked list is the input of the song and artist
O- Dictionary stored into linked list
C - Time complexity and Space complexity
E - return what if linkedlist is empty


Plan:
connect the linkedlist to eachother
initalize dictionary
then we can loop through the linkedlist
dictionary[] = dictionary.get(num, 0)+1

return the dictionary

Implement:
"""
class SongNode:
    def __init__(self, song, artist, next=None):
        self.song = song
        self.artist = artist
        self.next = next

# For testing
def print_linked_list(node):
    current = node
    while current:
        print((current.song, current.artist), end=" -> " if current.next else "")
        current = current.next
    print()


def get_artist_frequency(playlist):
    artist_frequency = {}
    current = playlist
    while current:
        if current.artist in artist_frequency:
            artist_frequency[current.artist] += 1
        else:
            artist_frequency[current.artist] = 1
        current = current.next
    return artist_frequency

playlist = SongNode("Saturn", "SZA", 
                SongNode("Who", "Jimin", 
                        SongNode("Espresso", "Sabrina Carpenter", 
                                SongNode("Snooze", "SZA"))))

output = get_artist_frequency(playlist)

print(output)