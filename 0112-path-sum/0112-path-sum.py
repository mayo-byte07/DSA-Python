class Solution(object):
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        if not root.left and not root.right:
            return targetSum == root.val
        remainingSum = targetSum - root.val
        return self.hasPathSum(root.left, remainingSum) or self.hasPathSum(root.right, remainingSum)