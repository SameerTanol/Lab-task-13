# Q1 Calculate the height of a binary tree

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height_of_binary_tree(root):
    if root is None:
        return -1  

    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)

    return max(left_height, right_height) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

height = height_of_binary_tree(root)
print("Height of the binary tree:", height)

#Q2 Count the number of nodes in a binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

num_nodes = count_nodes(root)
print("Number of nodes in the binary tree:", num_nodes)


#Q3 Determine if a tree is a BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(root, min_val=float('-inf'), max_val=float('inf')):
    if root is None:
        return True
    
    if root.value <= min_val or root.value >= max_val:
        return False
    
    return is_bst(root.left, min_val, root.value) and is_bst(root.right, root.value, max_val)


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)


if is_bst(root):
    print("The tree is a Binary Search Tree (BST).")
else:
    print("The tree is not a Binary Search Tree (BST).")


#Q4 Find the lowest common ancestor of two nodes in a binary tree
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_lca(root, node1, node2):
    if root is None:
        return None
    
    if root.value == node1 or root.value == node2:
        return root
    
    left_lca = find_lca(root.left, node1, node2)
    right_lca = find_lca(root.right, node1, node2)
    
    if left_lca and right_lca:
        return root
    
    return left_lca if left_lca else right_lca

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

lca_node = find_lca(root, 4, 5)
print("Lowest common ancestor of nodes 4 and 5:", lca_node.value)

lca_node = find_lca(root, 4, 6)
print("Lowest common ancestor of nodes 4 and 6:", lca_node.value)


#Q5 Find the k-th smallest element in a BST
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest_element(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.value
        root = root.right

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(8)

k = 3
kth_smallest = kth_smallest_element(root, k)
print(f"The {k}-th smallest element in the BST is:", kth_smallest)


#Q6 Perform a level order traversal
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_order_traversal(root):
    if root is None:
        return []

    result = []
    queue = [root]

    while queue:
        current_level = []
        next_level = []

        for node in queue:
            current_level.append(node.value)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(current_level)
        queue = next_level

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)

traversal_result = level_order_traversal(root)
print("Level order traversal:", traversal_result)




