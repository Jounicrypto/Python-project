#1. Building Dictionaries from a List
wordlist = ["apple","durian","banana","durian","apple","cherry",
"cherry","mango","apple","apple","cherry","durian","banana",
"apple","apple","apple","apple","banana","apple"]

def makeDic(wList):
    dic = {}
    for w in wList:
        check = dic.get(w,-1)
        if check <0 :
            dic[w] =1
        else: 
            dic[w] +=1

    return dic
print('The dictionary is: ')
print(makeDic(wordlist))

#2. Building Dictionaries from a String

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
"apple,apple,cherry,durian,banana,apple,apple,apple," + \
"apple,banana,apple"

def wFrequency(aStr):
    wList = aStr.split(',')
    wFreq = {}
    for w in wList :
        check = wFreq.get(w, -1)
        if check < 0 :
            wFreq[w] = 1
        else:
            wFreq[w] +=1
    return wFreq

print ('Words frequency is:')
print(wFrequency(text))

# 3. Translating

english_dutch = { "last":"laatst", "week":"week", "the":"de",
"royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
"zaag", "first":"eerst", "performance":"optreden", "of":"van",
"a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij",
"one":"een", "world":"wereld", "leading":"leidend", "modern":
"modern", "composer":"componist", "composers":"componisten",
"two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson." 

def formatSentence(aSentence):
    str =''
    for char in aSentence:
        if char.isalpha():
            str +=char
        else:
            str += ' '
    return str


def translation(aSentence):

    formatedSentence = formatSentence(sentence)
    wordsList = formatedSentence.split(' ')

    result= aSentence
    currentPos = 0

    for word in wordsList:
        translatedWord = english_dutch.get(word.lower(), word)

        idx = result[currentPos:].find(word)
        
        result = result[:currentPos+idx] + translatedWord + result[len(word)+currentPos+idx:]
        
        currentPos = currentPos+ len(translatedWord)+idx

    return result

print('Tranlated sentence is: ')
print (translation(sentence))