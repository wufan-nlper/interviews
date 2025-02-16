"""
2.11 10点一面

1. vLLM框架有什么优点？为什么用它？
2. BERT与大模型在架构上的差异？
3. 讲一讲DeepSeek的MoE架构的原理？

部门简况：
    领域语言意图理解、情感分析、任务执行
    大模型为核心的可调用各种函数、可记录用户偏好、可自我反思的agent
    内部氛围好、团队投入大

办公地点：诚盈中心

算法题：最长公共前缀
"""

def max_prefix(strs):
    if not strs:
        return ""

    l, cnt = len(strs[0]), len(strs)
    for i in range(l):
        c = strs[0][i]
        for j in range(cnt):
            if i == len(strs[j]) or strs[j][i] != c:
                return strs[0][: i]
        
    return strs[0]

strs = [
    "sdfsdfcd",
    "lsl",
    "fsdkk",
    "asdfxxs"
]

print(max_prefix(strs))