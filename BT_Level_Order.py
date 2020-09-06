# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

# For example:
# Given binary tree [3,9,20,null,null,15,7],
#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its level order traversal as:

# [
#   [3],
#   [9,20],
#   [15,7]
# ]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(self, root: TreeNode) -> list[list[int]]:
    result = []
    queue = []
    if not root:
        return []
    queue.append(root)
    result.append(root.val)
    while(1):
        node = queue.pop(0)
        if(node.left):
            queue.append(node.left)
            result.append(node.left.val)
        else:
            result.append(None)
        if(node.right):
            queue.append(node.right)
            result.append(node.right.val)
        else:
            result.append(None)
        if not queue:
            break
    print(result)

def main():
    print("")

if __name__ == "__main__":
    main()
