import re
import jieba.posseg as pseg
from wordcloud import WordCloud


def create_word_cloud(string, filename):
    words = pseg.cut(string)
    string = " ".join([x.word for x in words])
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               "]+", flags=re.UNICODE)
    string = emoji_pattern.sub(r'', string)
    word_cloud = WordCloud(font_path='NotoSansHK.otf', background_color="white", max_font_size=50,
                           max_words=200)
    word_cloud = word_cloud.generate_from_text(string)
    word_cloud.generate(string)
    word_cloud.to_file(filename)
