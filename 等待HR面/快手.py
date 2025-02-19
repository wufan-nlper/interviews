"""
岗位：NLP算法工程师-内容风控
"""

"""
2.10 11点一面

1. 讲一下LLaMA的正则化是怎么做的？
2. attention的计算主要有哪些种类？
3. 讲一下RoPE的原理？

算法题1：求排序旋转数组的最小值和最大值
算法题2：求字符串的最长子串，这个子串要求最多有三种字符，且每种字符出现次数至少为两次
"""

def find_min_max(nums):
    l = len(nums)
    left = 0
    right = l - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1

    return nums[left], nums[right]


def find_longest_substring(s):
    l = len(s)
    left = 0
    right = 0
    max_len = 0
    max_left = 0
    max_right = 0
    counter = {}
    while right < l:
        counter[s[right]] = counter.get(s[right], 0) + 1
        while len(counter) > 3:
            counter[s[left]] -= 1
            if counter[s[left]] == 0:
                del counter[s[left]]
            left += 1
        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_left = left
            max_right = right
        right += 1

    return s[max_left:max_right+1]


"""
2.11 19点一面

算法题：给定从0开始的等差数列，其中缺失了一个数，找出缺失的那个数是几
"""

def find(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        num = nums[mid]
        if num == mid:
            left = mid+1
        else:
            right = mid
    return left

nums = [0,1,2,3,5,6,7]
print(find(nums))


"""
2.14 15点三面

1. DeepSeek的创新点？为什么它成本低、推理速度快？
2. MLA的计算过程？
3. 为什么出来换工作？你过往的项目如何用在快手？
4. 为什么当时入职雪球？

数学题：给定相互独立的随机分布x和y，都是0~1范围内的均匀分布，求max(xy)的期望
"""


"""
2.18 15点HR面 已完成
"""