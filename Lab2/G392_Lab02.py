# Part 1, multiply list items together
part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 2048, 4096]
ans1 = 1
for i in part1:
    ans1 *= i
print ("All numbers multiplied togther are: ", ans1)


# Part 2, add list items together
part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]
ans2 = 0
for i in part2:
    ans2 += i
print ("All numbers added togther are: ", ans2)

# Part 3, add together even numbers
part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]
ans3 = 0
x = 0
y = -1 
while x < len(part3) - 1:
    y += 1
    x+=1
    if part3[y]%2 == 0:
        ans3 += part3[y]
print(" All even numbers added together are: ", ans3)
