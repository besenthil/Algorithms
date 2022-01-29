# O(w*c) - time
# O(w) - space
def minimumCharactersForWords(words):
    max_characters_count = {}
    for word in words:
        word_characters_count = {}
        for character in word:
            word_ch_count = word_characters_count.setdefault(character, 0)
            max_ch_count = max_characters_count.setdefault(character, 0)
            word_ch_count += 1
            if word_ch_count > max_ch_count:
                max_characters_count[character] = max(word_ch_count, max_ch_count)
            word_characters_count[character] = word_ch_count
    output = zip(list(max_characters_count.keys()), list(max_characters_count.values()))
    final_output = [[tup[0]] * tup[1] for tup in output]
    return (sum(final_output, []))
