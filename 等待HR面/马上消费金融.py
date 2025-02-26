"""
岗位：大模型算法工程师

2.18 20点一面

部门：大模型产品研发和落地
公司：
    放贷：对用户贷款意图的识别、大模型生成内容、风控、提效、金融领域垂类应用
    mentor培养、AIGC做营收、
    9点~20点

1. 讲一下BERT的模型结构
2. LayerNorm和BatchNorm的区别？
3. LayerNorm有哪些参数可调整或者可学习？
4. BERT的每个encoder块的LayerNorm都是一样的吗？

算法题：给定一个旋转排序数组 nums 和一个目标值 target，写一个函数来返回目标值在数组中的索引。如果目标值不存在于数组中，返回 -1。
  旋转排序数组是由原始有序数组变化得到的，例如，[0,1,2,4,5,6,7] 变成 [4,5,6,7,0,1,2]
  
  输入: nums = [4,5,6,7,0,1,2], target = 0
  输出: 4
  输入: nums = [4,5,6,7,0,1,2], target = 3
  输出: -1
"""
def find(nums, target):
    n = len(nums)

    left, right = 0, n-1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target and target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        else:
            if nums[left] <= target and target < nums[mid]:
                right = mid-1
            else:
                left = mid+1


"""
2.22 10点半二面

1. BERT模型架构？
2. BERT能不能做的更大？会遇到什么问题？
3. BERT能不能和GPT一样做生成任务？
4. 讲解DPO算法，和PPO有什么区别？
5. DeepSeek有哪些创新，讲一下GRPO

短期消费贷
基于llm的营销、广告等收益提升
团队规模一二十人

算法题：
    1. K个有序数组的合并
    2. 整数开平方
数学题：
    1. 一根绳子，任取两点，求它能组成一个三角形的概率
    2. 贝叶斯公式？
"""


def merge_2(nums1, nums2):
    p1, p2 = 0, 0
    l1, l2 = len(nums1), len(nums2)
    ans = []
    while p1 < l1 and p2 < l2:
        if p1 == l1:
            ans.extend(nums2[p2: ])
            break
        elif p2 == l2:
            ans.extend(nums1[p1: ])
            break
        elif nums1[p1] < nums2[p2]:
            ans.append(nums1[p1])
            p1 += 1
        else:
            ans.append(nums2[p2])
            p2 += 1
    
    return ans


def sqrt_2(num, eps=1e-10):
    guess = num / 2
    while True:
        guess_cache = (guess + num / guess) / 2
        if abs(guess - guess_cache) < eps:
            return guess_cache
        guess = guess_cache


"""
2.26 HR电话联系
"""


if __name__ == "__main__":
    # nums1 = [1,3,5,7,9]
    # nums2 = [2,4,6,8]
    # print(merge_2(nums1, nums2))
    print(sqrt_2(3))
