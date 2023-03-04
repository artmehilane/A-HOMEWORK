def maxArea(height):
    maxV = 0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            laius = j - i
            if height[i] <= height[j]:
                ruumala = height[i] * laius
            else:
                ruumala = height[j] * laius
            if ruumala > maxV:
                maxV = ruumala
    return maxV

test = [1,8,6,2,5,4,8,3,7]
print(maxArea(test))
