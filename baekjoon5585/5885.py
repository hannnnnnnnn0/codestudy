n = int(input())
money = 1000
many = [500, 100, 50, 10, 5, 1]
count = 0
changes = money - n

for i in many:
    count += changes // i
    changes %= i

