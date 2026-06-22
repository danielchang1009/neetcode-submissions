# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # 1. 在外面定義一個變數來存「全球最大直徑」
        self.ans = 0
        
        # 2. 定義一個輔助用的「算高度」函數
        def get_height(node):
            if not node:
                return 0
            
            # 遞迴算出左邊跟右邊的高度
            left = get_height(node.left)
            right = get_height(node.right)
            
            # 【關鍵步驟 A】：在這裡更新全球最大直徑！
            # 提示：利用 left 和 right 算出通過這個點的直徑，
            # 並拿去跟 self.ans 比較，誰大就留誰。
            pot=left+right
            self.ans=max(self.ans,pot)
            # 【關鍵步驟 B】：回傳「高度」給上一層。
            # 提示：就是你原本寫的那行 max(left, right) + 1
            return max(left,right)+1

        # 3. 執行這個輔助函數
        get_height(root)
        
        # 4. 最後回傳存好的全球最大值
        return self.ans