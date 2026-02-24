class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        #special cases
        if ((len(flowerbed) == 1) and (flowerbed[0] == 0)):
            flowerbed[0] = 1
            count+=1
        if count >= n:
            return True
        if ((flowerbed[0] == 0) and (flowerbed[1] == 0)):
            flowerbed[0] = 1
            count+=1
        if ((flowerbed[len(flowerbed)-1] == 0) and (flowerbed[len(flowerbed)-2] == 0)):
            flowerbed[len(flowerbed)-1] = 1
            count+=1
        if count >= n:
            return True
        for i in range(1, len(flowerbed) - 1):
            #print("count: " + str(i))
            #print("pre val: " + str(flowerbed[i-1]))
            #print("cur val: " + str(flowerbed[i]))
            #print("next val: " + str(flowerbed[i+1]))
            if ((flowerbed[i-1] == 0) and (flowerbed[i+1] == 0) and (flowerbed[i] != 1)):
                flowerbed[i] = 1
                count+=1
            if count >= n:
                return True
        return False