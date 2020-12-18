# Definition for a binary tree node.
# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/530/week-3/3305/
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def insert_node(head, node): 
    if node.val < head.val:
        if head.left: 
            insert_node(head.left, node) 
        else:
            head.left = node
    elif node.val > head.val:
        if head.right: 
            insert_node(head.right, node) 
        else:
            head.right = node
    else:
        head.val = node.val

def bstFromPreorder(preorder):
    """
    :type preorder: List[int]
    :rtype: TreeNode
    """
    root = None
    for val in preorder:
        if root:
            insert_node(root, TreeNode(val))
        else:
            root = TreeNode(val)
    #preporder(root)
    ans_list = bfs(root)
    print(ans_list)

def bfs(root):
    queue = [root]
    ans_list = []
    while len(queue) > 0:
        node = queue.pop(0)
        if node:
            ans_list.append(node.val)
            if node.right and node.right:
                queue.append(node.left)
                queue.append(node.right)
            elif node.left:
                queue.append(node.left)
                queue.append(None)
            elif node.right:
                queue.append(None)
                queue.append(node.right)
        else:
            ans_list.append(None)



    return ans_list

    '''

    if node:
        if node.left:
            print(node.left.val)
            ans_list.append(node.left.val)
            next_left_node = node.left
        else:
            ans_list.append("None")
        if node.right:
            print(node.right.val)
            ans_list.append(node.right.val)
            next_right_node = node.right
        else:
            ans_list.append("None")
        
        bfs(next_left_node, ans_list)
        bfs(next_right_node, ans_list)
    '''
    

def preporder(root):
    if root.left:
        preporder(root.left)
    print(root.val)
    if root.right:
        #print("Right node", root.right.val)
        preporder(root.right)


bstFromPreorder([8,5,1,7,10,12])
