import pandas as pd
import nltk
from nltk.corpus import stopwords
import pickle

accidents=pd.read_csv('Accidents.txt', sep='|')
accidents.columns=[x.lower() for x in accidents.columns]

'''
Tokenize narrative
'''
accidents_N=[]
for i in range(len(accidents)):
    if type(accidents['narrative'][i])==str:
        accidents_N.append(nltk.word_tokenize(accidents['narrative'][i]))
    else:
        accidents_N.append('')
    
print 'Tokenize finished'  

'''
Remove stopwords and some common words like 'employee','ee'. Also only remain words which are all characters using s.isalpha()
'''
remove_list=['employee'] + stopwords.words('english')+['ee']
narrative_cleanup=[]
if accidents_N!='':
    for i in range (len(accidents_N)):
        narrative_cleanup.append([w.lower() for w in accidents_N[i] if w.lower() not in remove_list and  w.isalpha()])
else:
    narrative_cleanup.append('') 
        
print 'Removed stopwords finished'

'''
Use pickle to save list in txt file
'''
pickle.dump(narrative_cleanup,open('all_narrative_cleanup.txt','wb'))