import random

def random_number(start: int, end: int):
    return random.randint(start, end)


for i in range(0, 10):
    print(random_number(0, 100))

    
for i in range(0, 10):
    print(random_number(101, 1000))

for i in range(0, 10):
    print(random_number(1001, 9999))