# filename1 = 'netease_playlist_desc.txt'
# filename2 = 'qq_playlist_desc.txt'
# output_filename = 'playlist_desc.txt'

filename1 = 'netease_comment.txt'
filename2 = 'qq_comment.txt'
output_filename = 'comment.txt'

# filename1 = 'netease_lyric.txt'
# filename2 = 'qq_lyric.txt'
# output_filename = 'lyric.txt'

if __name__ == '__main__':
    with open('./data/raw/{}'.format(filename1),'r',encoding='utf8') as fn_p:
        fn_p_content = fn_p.readlines()

    with open('./data/raw/{}'.format(filename2),'r',encoding='utf8') as fq_p:
        fq_p_content = fq_p.readlines()

    content = fn_p_content + fq_p_content

    with open('./data/{}'.format(output_filename),'w',encoding='utf8') as f:
        f.writelines(content)