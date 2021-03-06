import random
t = 10**6
max_lr = 10**12

print(t)
for _ in range(t):
    print(random.randint(max_lr // 2, max_lr),
          random.randint(max_lr // 2, max_lr))
