from collections import deque

# deque digunakan untu dapat menghpus dari kiri ke kanan
listItem = deque([1, 2, 3, 4, 5])

# hapus dari kiri ke kanan
listItem.popleft()
print(listItem)