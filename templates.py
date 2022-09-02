# binary search

left, right = 0, n
while left < right:
    mid = left + (right - left) // 2
    if condition(mid):
        right = mid
    else:
        left = mid + 1
return left

# monotonic stack for previous/next lesser/greater values
    # increasing finds previous/next lesser
    # decreasing finds previous/next greater

n = len(arr)
stack = []
next_lesser = [n] * n 
prev_lesser = [0] * n

for i in range(n):
    while stack and arr[stack[-1]] [>= / <=] arr[i]:
        next_lesser[stack.pop()] = i

    prev_lesser[i] = -1 if len(stack) == 0 else stack[-1]
    stack.append(i)

# bfs
q = collections.deque()
q.append(root)

while q:
    for _ in range(len(q)):
        cur = q.popleft()

        if cur.left:
            q.append(cur.left)
        if cur.right:
            q.append(cur.right)

