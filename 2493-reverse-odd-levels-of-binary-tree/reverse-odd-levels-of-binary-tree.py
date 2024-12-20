
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
    
        from collections import deque

        queue = deque([root])
        level = 0
        odd_level_values = []

    # Collect values at odd levels
        while queue:
            level_size = len(queue)
            current_level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                odd_level_values.append(current_level_values)
            level += 1
    # Reverse and assign values back
        for i in range(len(odd_level_values)):
            odd_level_values[i].reverse()

        queue = deque([(root, 0)])
        odd_index = 0

        while queue:
            level_size = len(queue)

            for _ in range(level_size):
                node, node_level = queue.popleft()

                if node_level % 2 == 1:
                    node.val = odd_level_values[odd_index].pop(0)

                if node.left:
                    queue.append((node.left, node_level + 1))
                if node.right:
                    queue.append((node.right, node_level + 1))

            if node_level % 2 == 1:
                odd_index += 1

        return root
        