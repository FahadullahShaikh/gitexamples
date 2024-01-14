print("Hello world");
list_one=['a','b','c','d','e'];
list_one.add('f')
print(list_one)

for lis in list_one:
   print(lis)

dict_one = {
            'a': ['python', 'C'],
            'b': ['Java', 'PhP']
            }
print(dict_one)

for k,v in dict_one.items():
    print(f"{k}'s age is {v}")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': 'c',
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for k,v in favorite_languages.items():
    print(f"{k}'s favorite-languages are {v}")