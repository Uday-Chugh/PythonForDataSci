d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}

# Access "hello" using keys and indexing
word = d['k1'][3]['tricky'][3]['target'][3]

# Print the result
print(word)
