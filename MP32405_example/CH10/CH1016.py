import wordcloud   # 滙入詞雲

sample = '''With the proliferation of data in the past
         decade, Python emerged as a viable language
         for data processing and analysis.
         Its simple syntax and powerful toolbox
         and libraries make Python the standard
         language for data.'''

# 1.建立詞雲物件，背景為透明
show = wordcloud.WordCloud(mode = 'RGBA',
      background_color = None, width = 350,
      height = 250, margin = 2)
# 2. 詞雲裡放入文字資料
show.generate(sample)
# 3. 產生詞雲圖片
show.to_file('Demo02.png')
