numbers=[1,10,5,16,4,9,11,8,9]
letters=['a','f','g','s','h','c']

print(min(numbers))
print(max(numbers))

print(min(letters))
print(max(letters))

print(numbers[0:3])
print(numbers[4:])

print(letters[3:])

val=numbers[4]=100

print(numbers)

numbers.append(49)
print(numbers)

numbers.append('22')#liste sonuna ekler
print(numbers)

numbers.insert(2,21)
print(numbers)

numbers.insert(-1,99)#verilen index numarasindan hemen onceki indexe ekler.
print(numbers)

numbers.pop()# en sondaki elemanı siler
print(numbers)

numbers.pop(0)
print(numbers)

numbers.remove(21)#aranan elemani bulup siler
print(numbers)

numbers.sort()
print(numbers)#siralama yapar

letters.sort()
print(letters)


numbers.reverse()
print(numbers)#tersten yazdirir

letters.reverse()
print(letters)

print(len(letters))
print(len(numbers))

print(numbers.count(9))

print(letters.count('a'))

numbers.clear()
print(numbers)#hepsini siler.