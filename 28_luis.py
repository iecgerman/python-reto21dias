def my_map(list, func):
  return [func(i) for i in list]

result0 = my_map([1, 2, 3, 4], lambda num: num * 2)
print(result0)
print('\n')
# Output: [2, 4, 6, 8]

result1 = my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"])
print(result1)
print('\n')
# Output: ["michi", "firulais"]