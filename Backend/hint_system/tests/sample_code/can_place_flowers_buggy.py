# Intentional errors: 
# 1. Missing edge case handling
# 2. Incorrect adjacent check
def canPlaceFlowers(flowerbed, n):
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
    return n <= 0