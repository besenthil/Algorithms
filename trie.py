import sys

if __name__ == "__main__":
    trie = dict()
    for x in ['senthil','kumar','shiv','bala','g']:
        str_arr = list(x)
        for index,z in enumerate(str_arr):
            if len (str_arr[index+1:index+2]) > 0:
                for y in str_arr[index+1:index+2]:
                    try:
                        if y is not None:
                            trie[z].add(y)
                    except KeyError:
                        trie[z] = set(y)
            else:
                trie[z] = set('$')

    print (trie)
