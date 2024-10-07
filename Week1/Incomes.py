f = open("pay.txt", "r")
content = f.read()

data = [val for val in content.split()]
print(data)

Emma = 0
Sofia = 0
Olivia = 0

for i in range(0,int(len(data)/3)):
    print(data[i])
    x=i*3
    if data[x] == "Emma":
        Emma += (int(data[x+1]) * int(data[x+2]))
    elif data[x] == "Sofia":
        Sofia += (int(data[x+1]) * int(data[x+2]))
    else:
        Olivia += (int(data[x+1]) * int(data[x+2]))
        
print("Emma: £", Emma)
print("Sofia: £", Sofia)
print("Olivia: £", Olivia)
    
    