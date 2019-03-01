from nltk.book import *
class PoemPlay:


    def __init__(self,text):
        self.text= []
        self.dist = FreqDist(text)

    def get_long_weird_words(self,length=10,distribution=5,total=5):
        return [w for w in set(text1) if len(w) >length and self.dist[w] > distribution][:total]

    def get_short_banal_words(self,length=10, distribution=2,total=3):
        return [w for w in set(text1) if len(w) < length and self.dist[w] > distribution][:total]

    def get_short_weird_words(self,length=10, distribution=5,total=3):
        return [w for w in set(text1) if len(w) < length and self.dist[w] > distribution][:total]


if __name__ == "__main__":
    texts = [text1,text2,text3,text4,text5,text6,text7,text8,text9]
    i = 0
    for t in texts:
            m = PoemPlay(t)
            print " ".join(m.get_short_banal_words())
            print " ".join(m.get_short_weird_words())
            print " ".join(m.get_long_weird_words())
            print

