"""1.24一面"""

"""
1. LoRA原理？LoRA初始化是怎样的，其中的参数有哪些，如何设置？
2. BERT和大模型的区别？
3. 温度、topk、topp的作用？
4。 DPO算法对齐的细节？

算法题：给定列表，输出出现次数最多的前k个元素，及其频数
"""

def func(l, topk=0):
    d = dict()
    n = len(l)
    if topk == 0:
        return d

    try:
        for ll in l:
            d[ll] = d.get(ll, 0) + 1
        
        d = [[k, v] for k, v in d.items()]
        d = sorted(d, reverse=True, key=lambda x: x[1])
        d = d[: topk]
        d = {dd[0]: dd[1] for dd in d}
    except Exception as e:
        return {"error": e}
    return d


if __name__ == "__main__":
    l = [2,3,4,1,2,4,3,2,5,6,3,1,0,4,2,3,2]
    # l = []
    print(func(l, 100))


"""break"""
