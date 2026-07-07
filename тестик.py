words = ["apple", "banana", "kiwi", "cherry", "pear", "grape", "melon"]
#sort_words = sorted(len(word) for word in words), revers=True)
# sort_words = [(sorted(len(word) for word in words), revers=True)] !!!!!!!
sample = sorted(words, key=len, reverse=True)
groups = [sorted(word for word in words if len(word) == sam) for sam in sample]
print(groups)