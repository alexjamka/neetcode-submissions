def get_longer_word(word1: str, word2: str) -> str:
    length_1 = len(word1)
    length_2 = len(word2)
    if length_1 > length_2:
        return word1
    elif length_1 == length_2:
        return word1
    else:
        return word2



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
