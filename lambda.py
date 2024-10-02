# single expression that returns a value
# my vscode does not auto correct it self with the return thing.

squared = lambda num : num * num

print (squared(2))


addtwo = lambda num : num + 2

print (addtwo(12))

sum_total= lambda a,b :a + b
print(sum_total(10, 8))


def funcbuilder(x):
    return lambda num :num + x

addten = funcbuilder(10)
addtwenty =funcbuilder(20)

print (addten(7))
print (addtwenty(7))





numbers = [3,7,12,18,20,21]

squared_nums = map(lambda num: num * num,numbers)

print(list(squared_nums))





odd_nums = filter(lambda num:num % 2 != 0, numbers)

print (list(odd_nums))

# my import didnt shift to the top of my code?????????


from functools import reduce



numbers =[1,2,3,4,5,1]

total = reduce(lambda acc,curr:acc + curr, numbers)

print (total)

print (sum(numbers,10))




names = ['dave','gray','sara','john jacob jinglebells']

char_count = reduce(lambda acc,curr:acc + len(curr), names, 0) # i replaced the = with +.(moral of this is one cannot use = inside a lambda function nowonder ilikua inadisplay allot of error wheen i run the code.(work like a charm))


print (char_count)

#sum is the simpler version:reduce........
