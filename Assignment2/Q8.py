seq = ['soup', 'dog', 'salad', 'cat', 'great']

filtered_words = list(filter(lambda word: word.startswith('s'), seq))

print(filtered_words)  # Output: ['soup', 'salad']
