sentence="python is a interesting language and python is a easy language"
words=sentence.lower().split()
for word in set(words):
    print(f"{word}: {words.count(word)}")
