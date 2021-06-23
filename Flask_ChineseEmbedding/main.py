from gensim.models import KeyedVectors

if __name__ == '__main__':
    file = 'lib/data/100000-small.txt'
    print('正在加载模型...')
    wv_from_text = KeyedVectors.load_word2vec_format(file, binary=False) # 加载时间比较长
    print('模型加载完毕！')
    wv_from_text.init_sims(replace=True)
    word = '男人'
    if word in wv_from_text.wv.vocab.keys():
        vec = wv_from_text[word]
        print(wv_from_text.most_similar(positive=[vec], topn=10))
    else:
        print("没找到")