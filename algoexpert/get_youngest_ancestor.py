# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(v+d+h^2) - time

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    desc_one_ancestors = []
    desc_two_ancestors = []
    current_ancestor = None
    get_ancestors(descendantOne, topAncestor, desc_one_ancestors, current_ancestor)
    get_ancestors(descendantTwo, topAncestor, desc_two_ancestors, current_ancestor)

    left_index = 0
    right_index = 0

    print([x.name for x in desc_one_ancestors],
          [x.name for x in desc_two_ancestors], )
    # return list(set(desc_one_ancestors).intersection(desc_two_ancestors))[0]
    while left_index < len(desc_one_ancestors):
        right_index = 0
        while right_index < len(desc_two_ancestors):
            if desc_one_ancestors[left_index] == desc_two_ancestors[right_index]:
                return desc_one_ancestors[left_index]
            else:
                right_index += 1
        left_index += 1


def get_ancestors(node, topAncestor, ancestors, current_ancestor):
    if node is None:
        return
    ancestors.append(node)
    if node == topAncestor:
        current_ancestor = node
        return current_ancestor
    else:
        return get_ancestors(node.ancestor, topAncestor, ancestors, current_ancestor)

