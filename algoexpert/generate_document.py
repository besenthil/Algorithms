# O(n) - time
# O(n) - space

def generateDocument(characters, document):
    hash_characters = {}
    for character in characters:
        count = hash_characters.get(character, 0)
        hash_characters[character] = count + 1

    hash_document = {}
    for doc in document:
        count = hash_document.get(doc, 0)
        hash_document[doc] = count + 1

    for key, val in (hash_document.items()):
        char_count = hash_characters.get(key, 0)
        if char_count < val:
            return False
    return True
