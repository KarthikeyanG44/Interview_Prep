class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def pathSum(self, root, sum):
        if not root:
            return []
        bfsQueue = [root]
        pathList = [[root.val,root.val]]
        res = []
        lenQ = 1
        while len(bfsQueue)>0:
            tLen = 0
            for i in range(lenQ):
                leftF,rightF = True,True
                if bfsQueue[i].left:
                    bfsQueue.append(bfsQueue[i].left)
                    pathList.append(pathList[i]+[bfsQueue[i].left.val])
                    pathList[-1][0]+=bfsQueue[i].left.val
                    tLen+=1
                    leftF = False
                if bfsQueue[i].right:
                    bfsQueue.append(bfsQueue[i].right)
                    pathList.append(pathList[i]+[bfsQueue[i].right.val])
                    pathList[-1][0]+=bfsQueue[i].right.val
                    tLen+=1
                    rightF = False
                if leftF and rightF:
                    if pathList[i][0]==sum:
                        res.append(pathList[i][1:])
            del pathList[:lenQ]
            del bfsQueue[:lenQ]
            lenQ = tLen
        return res