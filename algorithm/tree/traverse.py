def inorder(root):
    if root is None:
        return []

    return inorder(root.left) + [root] + inorder(root.right)
