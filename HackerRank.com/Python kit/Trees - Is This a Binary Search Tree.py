def checkBST(root):
    inorder = []
    stack = []
    curr = root
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
            continue
        elif stack:
            curr = stack.pop()
            inorder.append(curr.data)
            curr = curr.right
        else:
            break
            
    if len(set(inorder)) != len(inorder):
        return False
    for i in range(1, len(inorder)):
        if inorder[i-1] > inorder[i]:
            return False
    return True
