def search(s, target):
    #[1,2,3,4,5,6] target = 5
    left, right = 0, len(s)-1
    while left <= right:
        mid = left + (right - left)//2
        if s[mid] == target:
            return mid
        if s[mid] < target:
            left = mid + 1
        else: 
            right = mid - 1
    return -1
print(search([1,2,3,4,5,6], 5))