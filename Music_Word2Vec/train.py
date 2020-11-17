import jieba
import jieba.posseg as pseg
import re
from Music_Word2Vec.lib.config import *
from gensim.models import word2vec

def get_stopwords():
    with open('./data/stopwords/baidu_stopwords.txt','r',encoding='utf8') as f_baidu:
        stopwords_baidu = [i.strip('\n') for i in f_baidu.readlines()]
    with open('./data/stopwords/cn_stopwords.txt','r',encoding='utf8') as f_cn:
        stopwords_cn = [i.strip('\n') for i in f_cn.readlines()]
    with open('./data/stopwords/hit_stopwords.txt','r',encoding='utf8') as f_hit:
        stopwords_hit = [i.strip('\n') for i in f_hit.readlines()]
    with open('./data/stopwords/scu_stopwords.txt','r',encoding='utf8') as f_scu:
        stopwords_scu = [i.strip('\n') for i in f_scu.readlines()]
    stopwords = list(set(stopwords_baidu+stopwords_cn+stopwords_hit+stopwords_scu))
    return stopwords

def pre_process():
    res = ''
    stopwords_list = get_stopwords()
    with open('./data/comment.txt','r',encoding='utf8') as f:
        content = f.readlines()

    for i in content:
        sentence = pseg.cut(i.strip())
        for word_raw in sentence:
            if word_raw.flag in POS_DICT:
                word = ''.join(re.findall(u'[\u4e00-\u9fa5a-zA-Z]', word_raw.word))
                if word not in stopwords_list and not i.isdigit() and len(word)>1:
                    res += word + ' '

    with open('./data/comment_cut_res.txt','w',encoding='utf8') as f:
        f.write(res)

    return res

def train():
    content = word2vec.Text8Corpus(u'./data/comment_cut_res.txt')

    # sg=1 是 skip-gram 算法，对低频词敏感；默认 sg=0 为 CBOW 算法。
    # size 是输出词向量的维数，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般值取为100到200之间。
    # window 是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b 个词，后面看 b 个词（b 在0-3之间随机）。
    # min_count 是对词进行过滤，频率小于 min-count 的单词则会被忽视，默认值为5。
    # negative 和 sample 可根据训练结果进行微调
    # sample 表示更高频率的词被随机下采样到所设置的阈值，默认值为 1e-3。
    # hs=1 表示层级 softmax 将会被使用，默认 hs=0 且 negative 不为0，则负采样将会被选择使用。
    model = word2vec.Word2Vec(content, sg=1, size=100, window=5, min_count=2, negative=1,
                     sample=0.001, workers=4)
    model.save('./model/comment.model')

def predict():
    model = word2vec.Word2Vec.load('./model/comment.model')
    print(model.most_similar(positive=['乡村']))

if __name__ == '__main__':
    print(pre_process())
    train()
    predict()