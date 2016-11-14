# word_count.py
def words(word_list):
    """
    :param word_list:
    :return {'word': word_occurrence_count}:
    """
    word_count = {}
    for word in [w for w in word_list.split()]:
        try:
            word = int(word)
            try:
                if word_count[word]:
                    word_count[word] += 1
            except KeyError:
                word_count[word] = 1
        except ValueError:
            try:
                if word_count[word]:
                    word_count[word] += 1
            except KeyError:
                word_count[word] = 1
    return word_count

def main():
    print(words('testing 1 2 testing'))

if __name__ == '__main__':main()
