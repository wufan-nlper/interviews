"""
1.15一面
1. embedding是怎么做的？为什么要做embedding？
    回答：embedding是将稀疏的one-hot编码转换为稠密的向量，可以减少维度，提高模型的泛化能力。
2. 讲一下LoRA原理？
    回答：LoRA引入低秩矩阵，将原始的注意力矩阵分解为两个低秩矩阵的乘积，减少了参数量。
3. 对RAG的理解？做RAG需要什么？流程是什么？
    回答：RAG是Retrieval Augmented Generation的缩写，是一种基于检索的生成模型。
    需要一个检索模块和一个生成模块，检索模块用来检索相关的信息，生成模块用来生成答案。
4. 写过Prompt吗，写Prompt的时候有什么需要注意的？
    回答：Prompt是一种零样本学习的方法，需要注意的是Prompt的设计，需要设计一个合适的Prompt。
5. 使用Pytorch，如何让参数不用梯度？
    回答：可以使用torch.no_grad()上下文管理器，或者使用detach()方法。
6. Dataset和DataLoader的区别？
    回答：Dataset是一个数据集类，DataLoader是一个数据加载类，Dataset用来加载数据，DataLoader用来加载数据并生成batch。
7. Pytorch的动态图和Tensorflow的静态图有什么区别？
    回答：Pytorch是动态图，Tensorflow是静态图，动态图是在运行时构建计算图，静态图是在编译时构建计算图。
8. safetensors和bin这两种模型文件有什么区别？
    回答：safetensors是一种安全的模型文件，bin是一种二进制的模型文件。
"""


"""
1.21二面
1. transformer的多头自注意力为什么要分多个头？
    回答：多头自注意力可以学习到不同的特征，增加模型的表达能力。
2. transformer的自注意力机制是怎么计算的？
    回答：计算QKV矩阵，计算attention score，softmax，最后计算输出。
"""


"""
准备三面
"""