import queue

"""
You are organizing a festival and want to manage the queue of requests to perform.
Each request has a priority. Use a queue to process the performance requests in the order they arrive but ensure that requests 
with higher priorities are processed before those with lower priorities. Return the order in which performances are processed.

def process_performance_requests(requests):
    pass
Example Usage:

print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
Example Output:

['Music', 'Dance', 'Drama']
['Concert', 'Stand-up Comedy', 'Poetry', 'Magic Show']
['Keynote Speech', 'Panel Discussion', 'Film Screening', 'Workshop', 'Art Exhibition']
"""
"""
Understand: We are using a queue-  with the queue we are putting greatest to least tuples 
into a array
    implement: we might use a dictionary
    input:
    output:
    
"""
def process_performance_requests(requests):
    queue = []

    for key, value in requests:
        queue.append((key,value))
    
    result = []
        
    while queue:
        highest = max(queue)
        result.append(highest[1])
        queue.remove(highest)
    return result


print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))
