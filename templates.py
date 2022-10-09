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

# rotate matrix right

R = len(box)
C = len(box[0])

rot_box = [[''] * R for _ in range(C)]

for i in range(R):
    for j in range(C):
        rot_box[j][i] = box[i][j]
        
for i in range(len(rot_box)):
    rot_box[i] = rot_box[i][::-1]

# intersect between two times
l1, r1 = slots1[i]
l2, r2 = slots2[j]

intersect_start = max(l1, l2)
intersect_end   = max(r1, r2)

duration = intersect_end - intersect_start

# reverse linked list
prev, cur = None, head
while cur:
    tmp = cur.next
    cur.next = prev
    prev = cur
    cur = tmp

# Trie

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class TrieNode():
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]

        cur.end = True

    def search(self, word):
        cur = self.root

        for ch in word:
            if ch not in cur.children:
                return False
            cur = cur.children[ch]

        return cur.end



