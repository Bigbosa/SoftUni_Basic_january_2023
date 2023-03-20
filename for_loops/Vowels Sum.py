text = input()
sum = 0

for ch in range(0,len(text)):
     if text[ch] == "a":
         sum += 1
     if text[ch] == "e":
         sum +=2
     if text[ch] == "i":
         sum += 3
     if text[ch] == "o":
         sum += 4
     if text[ch] == "u":
         sum += 5
print(sum)