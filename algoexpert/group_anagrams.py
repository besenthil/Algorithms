# O(n*nlogn) - time
# O(n) - space
def groupAnagrams(words):
    hash_anagram = {}
    for word in words:
        sorted_word = "".join(sorted(word))
        output = hash_anagram.get(sorted_word, [])
        output.append(word)
        hash_anagram[sorted_word] = output
    return list(hash_anagram.values())
