"""
2.12 19点一面

1. 讲一下BERT的结构和计算过程？
2. 为什么BERT的长度最长只限512？
3. 残差连接在BERT中的作用？
4. 了解哪些位置编码？分别介绍一下
5. 什么是梯度裁剪？用数学语言描述
6. 解释一下DPO算法，它和PPO的区别在哪里？
7. DeepSeek有哪些创新点？
8. GRPO和PPO的区别？

算法题：
1. 手搓attention
2. 二叉树的最长路径

传统线上教育：主讲老师+辅导老师
使用大模型应用在线上流程，提升效率
解题机器人、仿真客服机器人
三轮技术面+HR面
"""


import torch
from torch import nn

class Attention(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()
        self.query = nn.Linear(input_dim, output_dim)
        self.key = nn.Linear(input_dim, output_dim)
        self.value = nn.Linear(input_dim, output_dim)
        self.dk = output_dim

    def attention(self, query, key, value):
        attention_score = query @ key.transpose(-2, -1)
        attention_score /= torch.sqrt(self.dk)

        attention_weights = nn.Softmax(dim=-1)(attention_score)
        attention_final = attention_weights @ value
        return attention_final
    
    def forward():
        pass


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def find_longest_path(root):
    path = []

    def depth(node):
        if not node:
            return 0, []

        left_depth, left_path = depth(node.left)
        right_depth, right_path = depth(node.right)

        new_path = left_path + [node.val] + right_path
        if len(new_path) > len(path):
            path = new_path

        if left_depth > right_depth:
            return left_depth + 1, left_path + [node.val]
        else:
            return right_depth + 1, right_path + [node.val]

    depth(root)
    return path
    

"""
2.18 14点二面、三面、HR面 已完成

初创公司
有三轮融资
工作节奏10-10-5
有几百张GPU卡
创业团队是高途出身
五险一金按1w做base交

"""

