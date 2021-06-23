## 使用说明
author: Reki Liu

update time: 2020.11.05

#### 原版词向量
- 词向量规模：6.31G，解压约16G，需要16G+内存运行，包含800多万中文词汇。
- 文档地址： Tencent AI Lab Embedding Corpus for Chinese Words and Phrases - [https://ai.tencent.com/ailab/nlp/en/embedding.html](https://ai.tencent.com/ailab/nlp/en/embedding.html)

#### 缩减版词向量
本服务对原版词向量进行了切割，选择部分词向量进行测试。

- 词向量规模：181MB，包含10万中文词汇。

#### 调用方法
##### 网页请求
- 点击网站“近义词”即可使用，请求地址：[http://ip:port/similar](http://ip:port/similar)

##### api请求
- 请求方法：POST
- 请求地址：`http://ip:port/api/similar/`
- 请求参数：直接拼接keywords即可，如`http://ip:port/api/similar/特朗普`

将返回以下结果：

```
{
    "keywords": "川普",
    "most similar": [
        [
            "川普",
            1.0
        ],
        [
            "特朗普",
            0.8885799646377563
        ],
        [
            "美国总统",
            0.8341415524482727
        ],
        [
            "奥巴马",
            0.8174577951431274
        ],
        [
            "特朗普总统",
            0.8017677068710327
        ],
        [
            "唐纳德·特朗普",
            0.7950495481491089
        ],
        [
            "克林顿",
            0.7815995216369629
        ],
        [
            "trump",
            0.7731729745864868
        ],
        [
            "希拉里",
            0.7726494669914246
        ],
        [
            "新总统",
            0.7635796070098877
        ]
    ]
}
```
