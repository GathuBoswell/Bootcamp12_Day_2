# word_count.py
def words(word_list):
    """
    :param word_list:
    :return {'word': word_occurrence_count}:
    """
    words = {}
    for word in [w for w in word_list.split()]:
        try:
            if words[word]:
                words[word] += 1
        except KeyError:
            words[word] = 1
    return words

print(words('¡Hola! ¿Qué tal? Привет!'))
