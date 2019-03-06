from nltk.corpus import gutenberg, nps_chat
import random
import nltk
import re
class PoemPlay:


    def __init__(self,corups):
        self.text = nltk.Text(gutenberg.words(corups))
        self.cv_word_pairs = [(cv, w) for w in self.text for cv in re.findall(r'[ptksvr][aeiou]', w)]
        self.cv_index = nltk.Index(self.cv_word_pairs)

    def get_pairs(self,dist):
        return [cv for w in self.text for cv in re.findall(r'[%s][aeiou]'% dist, w)]

    def get_word_pairs(self,pair):
        return self.cv_index[pair]

    def get_matches(self,first,second):
        try:
            words =' '.join(self.text.findall(r"<%s> (<.*>) <%s>" % (first,second)))
            return words
        except:
            return ""

if __name__ == "__main__":
    i = 0
    m = PoemPlay("melville-moby_dick.txt")


    pairs =  m.get_pairs("ptk")
    water =  m.get_matches("a","woman")
    whale =  m.get_matches("a","storm")
    wood =   m.get_matches("the","whale")
    pairs2 = m.get_word_pairs("ta")
    total =["freckled","terrible","violent","wounded","great","great","mighty","sperm","sperm","sperm","Norwegian","wondrous","American","American","sperm","dying","Greenland","Greenland","Greenland","Greenland","sperm","sperm","entire","Trumpa","Physeter","Sperm","Greenland","right","sperm","right","right","sperm","humpbacked","Greenland","Greenland","Greenland","sperm","sperm","Hyena","Tusked","Horned","Unicorn","Folio","white","white","white","white","white","white","white","white","white","Albino","sperm","sperm","entire","sperm","sperm","white","white","sperm","sperm","sperm","sperm","sperm","right","sperm","English","snowy","true","Right","stranded","living","Greenland","boiling","foremost","particular","sperm","spermaceti","sperm","stricken","sperm","waning","same","heaving","tremendous","great","beheaded","mightiest","great","sperm","dead","towing","fagged","sperm","right","sperm","sperm","stricken","wounded","sunken","sunken","first","stricken","flying","towing","whole","sperm","towing","unborn","stricken","schoolmaster","controverted","drugged","other","blasted","other","lighter","Dutch","slack","stricken","sperm","white","other","adult","last","hunted","great","eternal","living","last","dead","dead","stricken","white","famous","white","gliding","sperm","white","white","white","white","hated","before","stricken"]
    final =[]
    l = len(pairs)
    for t in xrange(0,len(total)-1):
        final.append(total[t])
        if t % random.randint(2,10) == 0:
            final.append(pairs[t])
        if t % random.randint(2,4) == 0:
            final.append(pairs2[t])
            final.append("\n")


    print " ".join(final)





