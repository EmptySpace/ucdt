import six
from ucd._ucd import UCDAtom, UCDWord, UCD
from ucd.ivoa import structure
Roots = structure.init_roots()
del structure


def tests():
    pass


class UCDTree(UCDAtom):
    '''
    '''
    def __init__(self):
        super(UCDTree, self).__init__(None)
        self.root = []
        # self.init_roots()

    def __str__(self):
        return self.print_tree()

    def init_roots(self):
        for k, v in Roots.items():
            self.add_child(v)

    def print_tree(self):
        items = print_branch(self.children, 1)
        return '\n'.join(items)

    def insert(self, ucd, data=None):
        assert isinstance(ucd, UCD)
        for word in ucd:
            self._add_word(word)

    def search(self, ucd):
        assert isinstance(ucd, UCD)
        out = []
        for word in ucd:
            out.append(self._find_word(word))
        return out

    def _add_word(self, word):
        assert isinstance(word, UCDWord)
        subtree = self
        for i, atom in enumerate(word):
            # if i == 0:
            #     assert atom.is_root and self.has_child(atom)
            if not subtree.has_child(atom):
                subtree.add_child(atom)
            subtree = subtree.get_child(atom)

    def _find_word(self, word):
        assert isinstance(word, UCDWord)
        subtree = self
        for i, atom in enumerate(word):
            if not subtree.has_child(atom):
                return None
            subtree = subtree.get_child(atom)
        return subtree


def print_leaf(leaf, level):
    lvl = ''.join([' |']*level)
    fmt = '{level}-{leaf}'
    return fmt.format(level=lvl, leaf=str(leaf))


def print_branch(branch, level):
    leaves = []
    for i, leaf in enumerate(branch):
        leaves.append(print_leaf(leaf, level))
        leaves.extend(print_branch(leaf.children, level+1))
    return leaves
