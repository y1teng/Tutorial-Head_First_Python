# def search4vowels(word):
#    """母音が見つかったかどうかによってブール値を返す。"""
#    vowels = set("aeiou")
#    found = vowels.intersection(set(word))
#    return bool(found)


# def search4vowels(word: str) -> set:
#    """指定された単語内の母音を返す。"""
#    vowels = set("aeiou")
#    return vowels.intersection(set(word))


def search4letters(phrase: str, letters: str = "aeiuo") -> set:
    """pharase内のlettersの集合を返す。"""
    return set(letters).intersection(set(phrase))
