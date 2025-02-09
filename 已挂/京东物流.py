"""1.8一面"""

"""
1. 温度、topk、topp差异？
    回答：温度是一个超参数，用来控制生成的多样性，topk是一个超参数，用来控制生成的多样性，topp是一个超参数，用来控制生成的多样性。
2. DPO和PPO区别？
    回答：PPO的全称是Proximal Policy Optimization，是一种基于梯度裁剪的强化学习算法。
    DPO的全称是Direct Preference Optimization，是一种基于偏好的强化学习算法。
3. LoRA原理？
4. 显存估计：以bf16精度训练一个7B参数的模型，显存估计？
    回答：56G显存。
5. 文本向量怎么做？
6. 对Agent、RAG的理解？
"""


"""
你一个整数数组 coins = [1, 2, 5]，表示不同面额的硬币，以及一个整数 amount = 11，
表示总金额。计算并返回可以凑成总金额所需的最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1
"""

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1


"""break"""