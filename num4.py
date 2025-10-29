def text_analyzer(text, top_n=5, min_length=0):

    words = text.lower().split()

    filtered_words = [word for word in words if len(word) >= min_length]

    total_words = len(words)
    total_filtered_words = len(filtered_words)
    total_chars = len(text)

    word_freq = {}
    for word in filtered_words:
        clean_word = word.strip('.,!?;:"()[]')
        if clean_word:
            word_freq[clean_word] = word_freq.get(clean_word, 0) + 1
    top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    print(f"Всего слов: {total_words}")
    print(f"Всего символов: {total_chars}")
    print(f"Слов после фильтра (длина ≥ {min_length}): {total_filtered_words}")

    print(f"\nСЛОВАРЬ ЧАСТОТ")
    for i, (word, freq) in enumerate(list(word_freq.items())):
        print(f"   '{word}': {freq}")

    print(f"\nТОП-{top_n} САМЫХ ЧАСТЫХ СЛОВ")
    for i, (word, freq) in enumerate(top_words, 1):
        print(f"   {i}. '{word}': {freq} раз(а)")

    return {
        'total_words': total_words,
        'total_chars': total_chars,
        'word_freq': word_freq,
        'top_words': top_words
    }


if __name__ == "__main__":

    sample_text = """
Программирование - это искусство создания программ для компьютеров. 
Python является одним из самых популярных языков программирования в мире. 
Язык Python прост в изучении, но при этом очень мощный и эффективный.

Разработчики используют Python для веб-разработки, анализа данных, 
искусственного интеллекта и научных вычислений. Многие компании, 
такие как Google, Facebook и NASA, используют Python в своих проектах.

Программирование на Python приносит удовольствие. Код на Python 
читается легко и понятно. Python имеет большое сообщество разработчиков, 
которые создают полезные библиотеки и фреймворки.

Изучение программирования открывает новые возможности. Каждый день 
миллионы программистов пишут код на Python, создавая amazing приложения 
и решая сложные задачи. Программирование - это не просто работа, 
это образ мышления и творческий процесс.

Python продолжает развиваться и улучшаться. Новые версии языка 
добавляют интересные функции и оптимизации. Будущее Python выглядит 
очень bright и перспективно.
"""

    result = text_analyzer(sample_text, top_n=3, min_length=3)
