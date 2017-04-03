# comprehensions - для сбора нового массива из старого

words = ['mama', 'papa']
new_words = [w.upper() for w in words]
print (new_words)

# про фильтры

b = [1, 2, 3, 4]
new_b = [i**2 for i in b if i<10 and i % 2 == 0]
print (new_b)

# внутри одного comprehension не больше двух логических выражений (for, if) - иначе слишком длинно

# Dict Comprehensions - вместо массивов словари

d = {'cat':'meow', 'dog':'woof', 'cow':'moo', 'cock':'cock-a-doodle-doo'}
sounds = {d[key]: key for key in d}
print (sounds)

# плоский массив - массив, состоящий из простых элементов (а не из др массивов)

BIG = [b, new_b, words]
flat = [item for arr in BIG for item in arr]
print (flat)

# форматирование строк
s = 'Everything is connected'
print (s.upper())
print (s.lower())
print (s.capitalize()) 
print (s.title())

template = 'Hello, {}!'
name = input("What's your name? ")
print (template.format(name))

print ('Hello, {} {}!'.format('Dirk', 'Gently'))

arr = [12, 25, 42, 84]
template = 'Age: {:>10}' # > - сдвиг того, что в скобках, на 10 символов направо
for i in arr:
    print (template.format(i))
    
print ('{:+^10}'.format('text'))

pi = 3.141592653589
print("Pi rounded up: {:.2f}".format(pi))
    
print('{:.6}'.format('iamnotastrawberry'))

#pyformat.info

