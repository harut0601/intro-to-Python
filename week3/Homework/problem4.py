market = {"dairy": ["yogurt", "cheese"], "fruits": ["banana", "apple", "orange", "lemon", "apple", "banana", "banana"]}
print(market)
market['candies'] = ["mars", "kinder", "twix"]
print(market)

fruits_new = market.get("fruits")
fruits_new.sort()
print(fruits_new)


for index in fruits_new:
    if index in fruits_new:
        fruits_new.remove(index)

print(fruits_new)

