class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def pre_order(self):
        """
        root left right
        """
        values = []

        def walk(root):
            if root is None:
                return
            values.append(root.value)
            walk(root.left)
            walk(root.right)

        walk(self.root)

        return values

    def in_order(self):
        """
        left root right
        """
        values = []

        def walk(root):
            if root is None:
                return

            walk(root.left)
            values.append(root.value)
            walk(root.right)

        walk(self.root)

        return values

    def post_order(self):
        """
        left right root
        """

        def walk(root, values):
            if root is None:
                return

            walk(root.left, values)
            walk(root.right, values)
            values.append(root.value)

            return values

        return walk(self.root, [])

    def find_max_value(self, root):
        if root is None:
            return(None)
        maxfind = root.value
        leftfound = self.find_max_value(root.left)
        rightfound = self.find_max_value(root.right)

        if leftfound and (leftfound > maxfind):
            maxfind = leftfound
        if rightfound and (rightfound > maxfind):
            maxfind = rightfound

        return maxfind



