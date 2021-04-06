def swapFL(lists):
    #temp = lists[0]
    #lists[0] = lists[3]
    #lists[3] = temp
    lists[0], lists[-1] = lists[-1], lists[0]

ingredients = ['flour', 'sugar', 'butter', 'apples']
swapFL(ingredients)
print(ingredients)