"""
2.8 15点一面
腾讯会议：376-154-817

1. 讲一下LoRA的原理？
2. LoRA的参数是如何调整的？
3. RoPE的原理？为什么要用RoPE？原版的正弦函数位置编码有什么问题？
4. 讲一下LayerNorm、BatchNorm、RMSNorm的区别？
5. 描述一下自注意力的计算过程？
6. 模型训练遇到过/欠拟合怎么办？

代码题：反转链表

"""

from ..leetcode import ListNode

def reverse(head):
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


"""
2.11 15点二面
腾讯会议：711-305-520
"""

if __name__ == "__main__":
    n1 = ListNode(1, None)
    n2 = ListNode(2, n1)
    n3 = ListNode(3, n2)
    n4 = ListNode(4, n3)
    n5 = ListNode(5, n4)

    c = n5
    while c:
        print(c.val)
        c = c.next

    print("-----------------")

    n = reverse(n5)
    c = n
    while c:
        print(c.val)
        c = c.next


