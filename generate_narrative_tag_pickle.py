import pickle
import nltk

data=pickle.load(open('all_narrative_cleanup.txt','rb'))

tagged_narrative=[]
print('total length %d'% len(data))

for element in data:
    tagged_narrative.append(nltk.pos_tag(element))
        
pickle.dump(tagged_narrative,open('all_narrative_tagged.txt','wb'))
    
