import spacy
from collections import Counter

def get_subject_predicate_relations(text):
    relationships=[]
    found = set()
    try:
        nlp = spacy.load("pt_core_news_lg")
    except:
        import subprocess
        import sys
        subprocess.check_call([sys.executable, "-m","spacy","download","pt_core_news_lg"])
        nlp = spacy.load("pt_core_news_lg")
        
    
    for doc in nlp(text).sents:

        subject = []
        predicate = []

        root = False

        # Find the subject and predicate
        for token in doc:
            if (token.dep_ == 'ROOT'): root = True
            if "subj" in token.dep_ and not root:
                subject.append(token.text)
            elif ("obj" in token.dep_) and root:
                predicate.append(token.text)

        # If subject or predicate is not found, return empty list
        if subject is not None and predicate is not None:
            for subj in subject:
                for obj in predicate:
                    if (subj,obj) in found:   
                        relationships.append((subj,obj))
                    else:
                        relationships.append((obj,subj))
                        found.add((obj,subj))


    return Counter(relationships)