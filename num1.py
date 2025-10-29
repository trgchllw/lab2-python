def process_words(words):
    lower_words = list(map(lambda x: x.lower(), words))

    filtered_words = list(filter(lambda x: len(x) > 3, lower_words))

    sorted_words = sorted(filtered_words)

    return sorted_words

words = ["Python", "is", "Great", "AI"]

print(process_words(words))