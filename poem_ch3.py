from nltk.corpus import wordnet as ws
class PoemPlay:


    def __init__(self):
        pass

    def get_synset(self,word,i):
        return ws.synset("%s.n.0%d" % (word,i))

    def get_synsets(self,word,w_type):
        return ws.synset(word,w_type)

    def get_syn(self,synset):
        return synset.lemma_names()

    def get_examples(self,synset):
        return synset.examples()

    def get_definition(self,synset):
        return synset.definition()

    def get_hyponyms(self,synset):
        return synset.hyponyms()

    def part_meronyms(self,synset):
        return synset.part_meronyms()

    def substance_meronyms(self,synset):
        return synset.substance_meronyms()

    def member_holonyms(self,synset):
        return synset.member_holonyms()

    def member_entailments(self,synset):
        return synset.member_entailments()

    def member_antonyms(self,synset):
        return synset.antonyms()

    def member_antonyms(self,synset):
        return synset.lowest_common_hypernyms()

    def similarity(self,synset):
        return (synset.min_depth,right.lowest_common_hypernyms(synset))

if __name__ == "__main__":
    i = 0
    m = PoemPlay()

    main_syn = m.get_synset("middle",1)
    words = m.get_syn(main_syn)

    print
    for w in words:
        for i in xrange(1,4):
            syn1 = m.get_synset(w,i)
            syn2 = m.get_hyponyms(syn1)
            syn3 = m.part_meronyms(syn1)
            syns = [syn1] + syn2 + syn3
            for syn in syns:
                print " ".join(m.get_examples(syn))
                print "".join(m.get_definition(syn))
            print
        print


