
f = open("mynumbers.txt", "r")
content = f.read()

numbers = [float(num) for num in content.split()]

even = []
odd = []
for i in numbers:
    if i%2 ==0:
        even.append(i)
    else:
        odd.append(i)
        
temp_total = 0
for i in even:
    temp_total += i
even_average = round(temp_total/len(even), 2)
temp_total = 0
for i in odd:
    temp_total += i
odd_average = round(temp_total/len(odd), 2)

#assumed mean average

print("EVEN:",even_average)
print("Odd:",odd_average)
    