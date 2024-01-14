class BinaryTree:
    def __init__(self, node):
        self.root = node

    def __str__(self):
        return f'{self.root}'

    def getHeight(self):
        def height(currentNode, prevDepth, maxDepth):
            if currentNode is None:
                return maxDepth
            depth = prevDepth + 1
            if depth > maxDepth:
                maxDepth = depth
            leftMax = height(currentNode.left, depth, maxDepth)
            rightMax = height(currentNode.right, depth, maxDepth)
            return max(leftMax, rightMax)

        return height(self.root, -1, -1)

    def balanced(self):
        def checkBalancedAt(node):
            if node is None:
                return 0

            leftH =  checkBalancedAt(node.left)
            rightH = checkBalancedAt(node.right)

            if -1 in [leftH,rightH]:
                return -1

            if abs(leftH - rightH) > 1:
                return -1

            return 1 + max(leftH,rightH)

        return checkBalancedAt(self.root) != -1

    def lca(self, a, b):
        curr = self.root
        while curr:
            if curr.data < a.data and curr.data < b.data:
                curr = curr.right
            elif curr.data > a.data and curr.data > b.data:
                curr = curr.left
            else:
                return curr


    @staticmethod
    def height(n):
        if n is None:
            return -1
        return 1 + max(BinaryTree.height(n.left), BinaryTree.height(n.right))

    def getPaths(self):
        def paths(node, path):
            if node is None:
                return
            path.append(node)
            if node.left is None and node.right is None:
                ps.append(path[:])

            paths(node.left, path)
            paths(node.right, path)

            path.pop()

        ps = []
        paths(self.root, [])
        return ps


    @staticmethod
    def preorderProcess(node, func):
        if node is None:
            return
        func(node)
        BinaryTree.preorderProcess(node.left,func)
        BinaryTree.preorderProcess(node.right,func)

    @staticmethod
    def inorderProcess(node,func):
        if node is None:
            return
        BinaryTree.inorderProcess(node.left, func)
        func(node)
        BinaryTree.inorderProcess(node.right, func)

    @staticmethod
    def postorderProcess(node,func):
        if node is None:
            return
        BinaryTree.postorderProcess(node.left, func)
        BinaryTree.postorderProcess(node.right, func)
        func(node)

    @staticmethod
    def reconstructTree(preorder, inorder):
        def constructSubtree(preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None

            rootValue =  preorder[preStart]
            root = TreeNode(rootValue)
            k = mapping[rootValue]
            root.left  = constructSubtree(preStart+1, preStart + (k - inStart), inStart, k-1)
            root.right = constructSubtree(preStart + (k - inStart) + 1, preEnd, k+1, inEnd)
            return root

        mapping = {v: i for i,v in enumerate(inorder)}
        return constructSubtree(0, len(preorder)-1, 0, len(inorder)-1)

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.visited = False
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.data}'

    def __str__(self):
        return f'Data: {self.data} - Left {self.left} right {self.right}; '
