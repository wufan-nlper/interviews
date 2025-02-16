"""
岗位：AI算法工程师
"""

"""
1.23一面

1. LLaMA3的结构？
    回答：LLaMA3是一个decoder-only的模型，主要因素有
        - GQA
        - RoPE
        - RMSNorm
        - FFN
        - 残差连接
        - 词汇表规模达到128K
        - 上下文支持达到8K
2. 为什么用LLaMA3？
    回答：实验对比的结果
3. DPO算法解释一下？
    回答：DPO的核心思想是通过人类偏好数据直接优化语言模型，绕过显式奖励模型的拟合和强化学习优化过程。
        具体来说，DPO利用一种特殊的参数化技巧，将奖励函数与策略模型的关系直接嵌入到优化目标中，从而避免了显式奖励模型的需求

最长公共子串，求子串内容
只做出来求子串长度
https://leetcode.cn/problems/longest-common-subsequence/
"""

def func(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp

def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)
    
    # 创建动态规划表
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 填充动态规划表
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # 反向追踪构造 LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])  # 当前字符属于 LCS
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    
    # 因为是从后往前追踪的，所以需要反转结果
    lcs.reverse()
    return ''.join(lcs)

# 示例
X = "ABCBDAB"
Y = "BDCAB"
print("最长公共子序列是:", longest_common_subsequence(X, Y))


"""
2.7 18点半二面

1. 瓴岳科技的业务主要是金融借贷、催收，属于行业第二梯队龙头，资产规模600亿（度小满2000亿，花呗4000亿）
2. AI方面，主要涉及到催收/客服/电话销售的机器人，以及交易流程的质量检测
3. AI研发部门分四个部分：算法、评测、数据、工程
4. 目前对话机器人由：意图树和LLM拼接而成
5. 算力一般，主要用云服务
6. 三面和AI研发总监面
7. 工作节奏10-7-5，稍有加班
8. 工作地点是团结湖附近，地铁通勤需要一个小时
"""


"""等待三面"""
