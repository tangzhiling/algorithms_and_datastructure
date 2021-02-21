# leetcode 589 N-tree preorder traversal

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        if not root:
            return []

        result = []
        if root.children:
            for node in root.children:
                result.extend(self.preorder(node))

        return [root.val] + result