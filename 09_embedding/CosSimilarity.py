import dashscope
import os
import numpy as np
from http import HTTPStatus


# 准备文本数据
texts = [
    '我喜欢吃苹果',
    '苹果是我最喜欢吃的水果',
    '我喜欢用苹果手机'
]

# 获取每个文本的embedding向量
embeddings = []

for text in texts:
    resp = dashscope.TextEmbedding.call(
        model="text-embedding-v4",
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        input=text
    )

    if resp.status_code == HTTPStatus.OK:
        vec = resp.output["embeddings"][0]["embedding"]
        embeddings.append(vec)

def cosine_similarity(vec1, vec2):
    """计算两个向量的余弦相似度"""
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    return dot_product / (norm_vec1 * norm_vec2)

# 比较所有文本之间的相似度
print("文本相似度比较结果：")
print("=" * 60)

for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        similarity = cosine_similarity(embeddings[i], embeddings[j])
        print(f"文本{i+1} vs 文本{j+1}:")
        print(f"  文本{i+1}: {texts[i]}")
        print(f"  文本{j+1}: {texts[j]}")
        print(f"  余弦相似度: {similarity:.4f}")
        print("-" * 40)

