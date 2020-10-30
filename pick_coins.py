coins = [4,2,1]
count = 0
for i in range(len(coins)):
    if(coins[i]%2==0):
        count+=int(coins[i]/2)
    else:
        count += int(coins[i] / 2)+1
print(count)
