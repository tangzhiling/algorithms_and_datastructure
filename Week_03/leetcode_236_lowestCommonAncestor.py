# leetcode 236 lowest common ancestor of a binary tree

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if not root: return None
        if p==root or q==root: return root 
        L=self.lowestCommonAncestor(root.left,p,q)
        R=self.lowestCommonAncestor(root.right,p,q)
        if L and R: return root
        return L if L else R