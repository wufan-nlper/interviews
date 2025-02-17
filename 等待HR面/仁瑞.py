"""
岗位：算法工程师
"""

"""
2.8 15点一面

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

1. 项目介绍

无代码题
"""


"""
2.13 6点半三面

1. 母公司是天和仁康，已成立21年以上
2. 主营业务是保健品、医疗器械的团购超市，用户忠诚度高，复购率98%以上
3. 潜在应用场景比较丰富，与北邮有技术合作
4. 弹性打卡上班，上午最迟11点，在公司待够11小时（包含8小时工作时间和3小时午晚餐时间）
5. 半年晋升一次
6. 绩效是月度评定，按照基本工资的70%发放底薪，30%的部分会乘以绩效比例（0.8~1.2）发放

已完成
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


