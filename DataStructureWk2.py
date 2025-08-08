thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
print(thisdict["year"])
print(type(thisdict))

numbers = {1, 2, 3, 4, 5}
print('Initial set:', numbers)
numbers.add(76)
print('Set after adding 76:', numbers)
print('Updated set:', numbers)

ShoeBrands = {'Nike', 'Addidas', 'Puma', 'Reebok'}
for brand in ShoeBrands:
    print(brand)
    print(type(brand))
    length = len(brand)
    print('Length of', brand, 'is', length)
    total_elements = len(ShoeBrands)
    print('Total elements in ShoeBrands set:', total_elements)

message = ''' Here are some popular shoe brands:
- Nike
- Adidas
- Puma
- Reebok
'''
print(message)

str1 = "I think am running mad"
str2 = "How did you come up with that idea!"
str3 = "I am not sure about that"
str4 = "dI think am running mad"
str5 = "I am not sure about that"
print(str1 == str4)
print(str1 == str2)
print(str1 == str5)
print(str3 == str5)
print(str3.upper())

name = 'Stephen Mutisya'
occupation = 'Software Engineer'

result = name + ' is a ' + occupation
print(result)

greet = 'Hamjamboni'
for letter in greet:
    print(letter)

    name = 'Stephen Mutisya'
    country = 'Kenya'
    print(f'{name} is from {country}')

    Input = ("20 40 30 10")
    total = sum(map(int, Input.split()))
    print(total)

    d1 = {"Fruit":["Mango","Banana"], "Flower":["Rose", "Lotus"]}
d2 = {('India, USA'):'Countries', ('New Delhi', 'New York'):'Capitals'}
print (d1)
print (d2)
