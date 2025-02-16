"""
2.8 19点一面
飞书面试：457733143

1. 表格识别是怎么做的，可以用paddle开源的
2. BERT和LLaMA在架构上的区别？它们的计算过程是怎样的？
3. DeepSeek的创新点？
    回答：MLA、GRPO、MoE架构、fp8精度训练
4. 了解哪些attention计算方法？
    回答：MHA、MQA、GQA、MLA
5. 模型训练有遇到过拟合吗，怎么解决？
6. 有哪些模型微调办法？除了LoRA
    回答：adapter tuning、p-tuning、llama-pro

代码题：找到第k大的元素
"""

def func1(nums, k):
    l = len(nums)

    def partition(left, right, pivot):
        p = nums[pivot]
        nums[pivot], nums[right] = nums[right], nums[pivot]
        cache_index = left
        for i in range(left, right):
            if nums[i] < p:
                nums[cache_index], nums[i] = nums[i], nums[cache_index]
                cache_index += 1
        nums[right], nums[cache_index] = nums[cache_index], nums[right]
        return cache_index

    def quicksort(left, right, k):
        if left == right:
            return left
        
        pivot = (left + right) // 2
        pivot = partition(left, right, pivot)
        if pivot == (l - k):
            return nums[pivot]
        elif pivot < (l - k):
            return quicksort(pivot+1, right, k)
        else:
            return quicksort(left, pivot+1, k)
        
    return quicksort(0, l-1, k)


"""等待二面"""