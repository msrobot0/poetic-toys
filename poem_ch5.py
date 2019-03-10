from nltk.corpus import gutenberg, nps_chat
from nltk.corpus import brown
from collections import defaultdict
import random
import nltk
import re
class PoemPlay:


    def __init__(self,corups):
        self.text = nltk.Text(gutenberg.words(corups))
        self.vocab_text =gutenberg.words(corups)
        self.vocab = nltk.FreqDist(gutenberg.words(corups))

    def get_tags(self):
        words = dict(nltk.corpus.brown.tagged_words())
        v1000 = [word for (word, _) in self.vocab.most_common(1000)]
        mapping = {}
        for v in v1000:
            try:
                k = words[v]
            except:
                k = "UNK"
            if k not in mapping:
                mapping[k] = []
            mapping[k].append(v)
        #tags = [mapping[v] for v in self.vocab_text]
        return  mapping

    def nl_tag(self):
        #nltk.corpus.brown.tagged_words()
        #unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
        #unigram_tagger.tag(self.text.sents()[2007])
        #text = word_tokenize("And now for something completely different")
        #nltk.pos_tag(text)
        pass

    def get_sim(self,dist):
        return [self.text.similar(d) for d in dist]

    def get_endings(self):
        last_letters = defaultdict(list)
        for word in self.text:
             key = word[-2:]
             last_letters[key].append(word)
        return last_letters

if __name__ == "__main__":
    i = 0
    m = PoemPlay("melville-moby_dick.txt")

    pairs =  m.get_sim(["rachel","wood","dog","sex","blubber"])
    tags =   m.get_tags()
    endings = m.get_endings()
    s = []
    for x in (0,len(endings)-1):
        for k in tags.keys():
            s.append("%s" % tags[k][x % len(tags[k])])
        s.append("%s"  % endings[x])


    print " ".join(s)

