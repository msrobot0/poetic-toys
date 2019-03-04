from nltk.book import *
class PoemPlay:


    def __init__(self,text,sent):
        self.text= text
        self.first_line= sent

    def get_first_line(self,length=10,distribution=5,total=5):
        return self.first_line

    def get_similar(self,word):
        return self.text.similar(word)

    def get_common_contexts(self,word):
        try:
            return self.text.common_contexts([word]).replace("_"," ")
        except:
            return None

if __name__ == "__main__":
    i = 0
    #text1.concordance("monstrous")
    m = PoemPlay(text1,sent1)
    for mm in m.get_first_line():
        if "," not in mm:
            sim = m.get_similar(mm)
            if sim is not None :
                print sim.replace("_"," ")
            sim2 = m.get_common_contexts(mm)
            if sim2 is not None:
                print sim2.replace("_"," ")

