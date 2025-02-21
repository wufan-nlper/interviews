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
"""