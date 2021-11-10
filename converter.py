num = input('Please enter the value: ')
unit = input('In which unit do you want it to be converted from:  ')
trgetUnit = input('In which unit do you want it convert: ')

if unit == "cm" and trgetUnit == "m":
    ans = float(num)/100
    print(ans)
elif unit == "mm" and trgetUnit == "cm":
    ans = float(num)/10
    print(ans)
elif unit == "m" and trgetUnit == "cm":
    ans = float(num)*100
    print(ans)
elif unit == "cm" and trgetUnit == "mm":
    ans = float(num)*10
    print(ans)
elif unit == "mm" and trgetUnit == "m":
    ans = float(num)/1000
    print(ans)
elif unit == "m" and trgetUnit == "mm":
    ans = float(num)*1000
    print(ans)
elif unit == "km" and trgetUnit == "m":
    ans = float(num)*1000
    print(ans)
elif unit == "m" and trgetUnit == "km":
    ans = float(num)/1000
    print(ans)
elif unit == "mm" and trgetUnit == "km":
    ans = float(num)/1000000
    print(ans)
elif unit == "ft" and trgetUnit == "cm":
    ans = float(num)*30.48
    print(ans)
elif unit == "ft" and trgetUnit == "mm":
    ans = float(num)*304.8
    print(ans)
elif unit == "ft" and trgetUnit == "inch":
    ans = float(num)*12
    print(ans)
elif unit == "inch" and trgetUnit == "cm":
    ans = float(num)*2.54
elif unit == "inch" and trgetUnit == "mm":
    ans = float(num)*25.4