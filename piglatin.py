import numpy as np

def ScorePigLatin(beforeword, afterword):
    if(afterword[-2:] != "ay"):
        return False

    transposed = beforeword[1:] + beforeword[0]   
    if(transposed != afterword[:-2]):

        return False
    return True

def ConvertWord(word):
    x = 0
    while(True):
        x = x + 1
        ss = np.random.permutation(list(word))

        qq = ""
        for i in ss:
            qq = qq + i

        qq = qq + "ay"

        if(ScorePigLatin(word, qq)):
            #print(qq + " discovered in " + str(x) + " iterations.")
            return qq
    
def ConvertSentence(sentence):
    if(sentence == ""):
        return "Error: empty input sentence."
    
    RetSentence = ""
    for word in str.split(sentence):
        RetSentence = RetSentence + ConvertWord(word) + " "
    
    return RetSentence[0:-1]
        
        
print(ConvertSentence("the quick brown"))
