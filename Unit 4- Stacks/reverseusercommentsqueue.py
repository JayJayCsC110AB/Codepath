def revese_comments_queue(comments):
    stack = []
    item = ""
    for i in comments:
      stack.append(i)

    reversed_item = []

    while stack:
        reversed_item.append(stack.pop())
    return reversed_item
      
print(revese_comments_queue(["Great post!", "love it", "thanks for sharing"]))