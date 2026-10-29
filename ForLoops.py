# range
# 0 = variant (more like starting point)
# 1 = count += 1 (add up) ==> count =+ 2
# 100 = the limit

print("What phrase do you want to see in reverse?" )
phrase = input() # Hello ==>

print("the phrase is ", end='')

for pos in range(len(phrase) -1, -1, -2):
    print(phrase[pos], end='')
