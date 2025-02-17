"""
岗位：算法工程师-安全技术
"""

"""
2.10 19点一面

1. 工作使用的框架有哪些？讲讲它们的原理？

算法题：最大无重复的子串长度
"""

def max_str(s):
    occur_set = set()
    l = len(s)

    p = -1
    ans = 0

    for i in range(l):
        if i > 0:
            occur_set.remove(s[i-1])
        while p+1 < l and s[p+1] not in occur_set:
            occur_set.add(s[p+1])
            p += 1
        
        ans = max(ans, p-i+1)

    return ans


"""
2.11 17点二面

打印一个等边三角形的图形
"""

def print_triangle(n=4):
    for i in range(n):
        j = i+n
        x1 = j - 2*i+1
        x2 = 2*i+1
        print(" "*x1 + "*"*x2)

print_triangle(n=18)


"""
2.13 11点三面

1. LLM微调有哪些参数要调整？它们的含义分别是什么？

团队大约20多人，涉及到NLP、CV、语音、多模态、特征融合等多种技术栈
目前在尝试用理解型模型，替换传统的算法模型
"""


"""
2.14 11点HR面
已完成
"""