class Node(object):
    def __init__(self, label):
        self.label = label
        self.leaves = []
        self.children = []
        self.parent = None

    def add_leaf(self, leaf):
        self.leaves.append(leaf)

    def add_child(self, child):
        self.children.append(child)

    def __eq__(self, obj):
        return isinstance(obj, Node) and obj.label == self.label and obj.leaves == self.leaves and obj.leaves == self.leaves and obj.children == self.children

    def __ne__(self, obj):
        return not self == obj

    def __str__(self):
        children_labels = [child.label for child in self.children]
        node = f"Node Label: {self.label}, Leaves: {self.leaves}, Children: {children_labels}"
        for child in self.children:
            node += f"\n{child}"
        return node
