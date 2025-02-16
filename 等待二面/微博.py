"""
2.12 10点半一面

1. 讲一下大模型三段式训练，PT、SFT、RLHF各自的流程以及作用
2. 如何解决大模型的幻觉问题？
3. 为什么要用DPO对齐？

微博内容安全团队
新浪总部大厦

算法题：最长回文子串
"""

def find_substr(s):
    l = len(s)
    if l < 2:
        return s

    dp = [[False] * l for _ in range(l)]
    for i in range(l):
        dp[i][i] = True

    max_len = 1
    begin = 0

    for i in range(2, l):
        for j in range(l):
            k = i+j-1
            if k > l:
                break

            if s[j] != s[k]:
                dp[j][k] = False
            else:
                if k-j < 3:
                    dp[j][k] = True
                else:
                    dp[j][k] = dp[j+1][k-1]
            
            if dp[j][k] and k-j+1 > max_len:
                max_len = k-j+1
                begin = j

    return s[begin: begin+max_len]


"""
2.18 16点线下二面
"""

if __name__ == "__main__":
    s = "asdwedcxxcdewed"
    print(find_substr(s))