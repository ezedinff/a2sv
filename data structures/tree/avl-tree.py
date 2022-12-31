class AVLTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1
    
    def leftRotation(self):
        newRoot = self.right
        self.right = newRoot.left
        newRoot.left = self
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot
    
    def rightRotation(self):
        newRoot = self.left
        self.left = newRoot.right
        newRoot.right = self
        self.height = 1 + max(self.getHeight(self.left), self.getHeight(self.right))
        newRoot.height = 1 + max(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        return newRoot
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height

class AVLTree:
    def __init__(self):
        self.root = None
    
    def insert(self, val):
        self.root = self.insertHelper(self.root, val)
    
    def insertHelper(self, root, val):
        if not root:
            return AVLTreeNode(val)
        elif val < root.val:
            root.left = self.insertHelper(root.left, val)
        else:
            root.right = self.insertHelper(root.right, val)
        root.height = 1 + max(root.getHeight(root.left), root.getHeight(root.right))
        balance = root.getHeight(root.left) - root.getHeight(root.right)
        if balance > 1 and val < root.left.val:
            return root.rightRotation()
        if balance < -1 and val > root.right.val:
            return root.leftRotation()
        if balance > 1 and val > root.left.val:
            root.left = root.left.leftRotation()
            return root.rightRotation()
        if balance < -1 and val < root.right.val:
            root.right = root.right.rightRotation()
            return root.leftRotation()
        return root
    
    def delete(self, val):
        self.root = self.deleteHelper(self.root, val)
    
    def deleteHelper(self, root, val):
        if not root:
            return root
        elif val < root.val:
            root.left = self.deleteHelper(root.left, val)
        elif val > root.val:
            root.right = self.deleteHelper(root.right, val)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.getMin(root.right)
            root.val = temp.val
            root.right = self.deleteHelper(root.right, temp.val)
        if not root:
            return root
        root.height = 1 + max(root.getHeight(root.left), root.getHeight(root.right))
        balance = root.getHeight(root.left) - root.getHeight(root.right)
        if balance > 1 and root.left.getHeight(root.left) >= root.left.getHeight(root.right):
            return root.rightRotation()
        if balance < -1 and root.right.getHeight(root.right) >= root.right.getHeight(root.left):
            return root.leftRotation()
        if balance > 1 and root.left.getHeight(root.left) < root.left.getHeight(root.right):
            root.left = root.left.leftRotation()
            return root.rightRotation()
        if balance < -1 and root.right.getHeight(root.right) < root.right.getHeight(root.left):
            root.right = root.right.rightRotation()
            return root.leftRotation()
        return root
    
    def getMin(self, root):
        if not root.left:
            return root
        return self.getMin(root.left)
    
    def getMax(self, root):
        if not root.right:
            return root
        return self.getMax(root.right)
    
    def inorder(self):
        self.inorderHelper(self.root)
        print()
    
    def inorderHelper(self, root):
        if not root:
            return
        self.inorderHelper(root.left)
        print(root.val, end=" ")
        self.inorderHelper(root.right)
    
    def preorder(self):
        self.preorderHelper(self.root)
        print()
    
    def preorderHelper(self, root):
        if not root:
            return
        print(root.val, end=" ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)
    
    def postorder(self):
        self.postorderHelper(self.root)
        print()
    
    def postorderHelper(self, root):
        if not root:
            return
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.val, end=" ")
    
    def search(self, val):
        return self.searchHelper(self.root, val)
    
    def searchHelper(self, root, val):
        if not root:
            return False
        if root.val == val:
            return True
        elif val < root.val:
            return self.searchHelper(root.left, val)
        else:
            return self.searchHelper(root.right, val)
    
    def levelOrder(self):
        if not self.root:
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()
    
    def reverseLevelOrder(self):
        if not self.root:
            return
        queue = [self.root]
        stack = []
        while queue:
            node = queue.pop(0)
            stack.append(node.val)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        while stack:
            print(stack.pop(), end=" ")
        print()
    
    def height(self):
        return self.getHeight(self.root)
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def size(self):
        return self.getSize(self.root)
    
    def getSize(self, root):
        if not root:
            return 0
        return 1 + self.getSize(root.left) + self.getSize(root.right)
    
    def isBalanced(self):
        return self.isBalancedHelper(self.root)
    
    def isBalancedHelper(self, root):
        if not root:
            return True
        balance = root.getHeight(root.left) - root.getHeight(root.right)
        if abs(balance) > 1:
            return False
        return self.isBalancedHelper(root.left) and self.isBalancedHelper(root.right)
    
if __name__ == '__main__':
    myTree = AVLTree()
    root = AVLTreeNode(10)
    myTree.root = root
    arr = [20, 30, 40, 50, 25]
    for i in arr:
        myTree.insert(i)
    myTree.inorder()
    myTree.preorder()
    myTree.postorder()
    print(myTree.search(30))
    print(myTree.search(35))
    myTree.levelOrder()
    myTree.reverseLevelOrder()
    print(myTree.height())
    print(myTree.size())
    print(myTree.isBalanced())
    myTree.delete(20)
    myTree.inorder()
    myTree.preorder()
    myTree.postorder()
    print(myTree.search(30))
    print(myTree.search(35))
    myTree.levelOrder()
    myTree.reverseLevelOrder()