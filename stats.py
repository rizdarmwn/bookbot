def get_words_count(text):
    return len(text.split())


def get_char_count(text):
    lower_text = text.lower()
    result = {}
    for c in lower_text:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1
    return result


def sorted_dict(chars):
    def sort_on(items):
        return items["num"]

    modified_chars = []
    for c in chars:
        modified_chars.append({"char": c, "num": chars[c]})

    sorted_chars = sorted(modified_chars, reverse=True, key=sort_on)

    return sorted_chars
