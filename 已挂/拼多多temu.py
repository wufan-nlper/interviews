"""
1.12一面

算法题：二叉树层序遍历
"""
from ..leetcode import *

def levelOrder(root: TreeNode):
    if not root:
        return []
    res = []
    q = deque([root])
    while q:
        size = len(q)
        level = []
        for _ in range(size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res


"""
1.20二面

算法题1：判断回文链表 https://leetcode-cn.com/problems/palindrome-linked-list/
算法题2：删除链表中的重复节点 https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/

1. transformer的attention计算过程？
    回答：embedding层输出x，分别计算QKV矩阵，计算attention score，softmax，最后计算输出。
2. softmax是怎么计算的，写代码实现
    回答：exp(x) / sum(exp(x))
3. 多头注意力为什么要分多个头？
    回答：多头注意力可以学习到不同的特征，增加模型的表达能力。
4. QKV矩阵的作用分别是什么？
    回答：Q和K计算attention score，再乘以V计算输出。
5. 多头注意力的初始化是怎么样的？
    回答：多头注意力的初始化是随机初始化。
6. 以transformer为基础的大模型的输出，是如何控制的？
    回答：通过调整温度、top-k、top-p等参数来控制输出。
"""
def isPalindrome(head: ListNode) -> bool:
    """找到链表中点"""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    """反转后半部分链表"""
    pre = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = pre
        pre = cur
        cur = nxt
    
    """比较前后两部分链表"""
    while pre:
        if pre.val != head.val:
            return False
        pre = pre.next
        head = head.next
    return True


def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            pre.next = head.next
        else:
            pre = pre.next
        head = head.next
    return dummy.next


"""break"""