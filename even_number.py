nums = [12,345,2,6,7896]
sum = 0
for num in nums:
    if len(str(num)) % 2 == 0:
        sum = sum + 1
print(sum)
