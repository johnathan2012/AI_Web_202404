import wordcloud   # 滙入詞雲

sample = {'Tomas' : 92, 'Edward' : 75,
        'Charles' : 92, 'Madeleine' : 83,
        'Lucia' : 62, 'Stavro' : 53,
          'Peter' : 48, 'Sam' : 62}

# 1.建立詞雲物件，背景為白色
show = wordcloud.WordCloud(background_color = 'white',
                           width = 200, height = 200, margin = 2)
# 2. 詞雲裡放入文字資料
show.fit_words(sample)
# 3. 產生詞雲圖片
show.to_file('Demo.png')
