from collections import deque
m,n=map(int,input().split())
words = list(map(int,input().split()))
memory_set=set()
memory_queue=deque()
count=0
for word in words:
    if word not in memory_set:
        count+=1
        if len(memory_set)>=m:
            removed_word=memory_queue.popleft()
            memory_set.remove(removed_word)
        memory_queue.append(word)
        memory_set.add(word)
print(count)
