import collections

deque_colors = collections.deque(["Red","Green","White"])
print(deque_colors)

print("\nAdding to the left: ")
deque_colors.appendleft("Blue")
print(deque_colors)

print("\nAdding to the right: ")
deque_colors.append("Orange")
print(deque_colors)

print("\nRemoving from the right: ")
deque_colors.pop()
print(deque_colors)

print("\nRemoving from the left: ")
deque_colors.popleft()
print(deque_colors)

print("\nReversing the deque: ")
deque_colors.reverse()
print(deque_colors)
