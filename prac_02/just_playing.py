
import random
rows = 7
numbers = [i for i in range(20)]
for row in rows:
    print(sorted(random.sample(numbers, 6)))



