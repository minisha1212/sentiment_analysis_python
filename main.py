# Cleaning Text Steps
# 1) Create a text file and take text from it.
# 2) Convert the letter into lowercase( 'Apple' is not equal to 'apple')
# 3) Remove Punctuations like .,!? etc.( Hi, this is Real-Time Sentiment Analysis on Social Media: Using Public Opinion to Gain Actionable Insights)

import string
from collections import Counter
import matplotlib.pyplot as plt

text = open('read.txt',encoding='utf-8').read()
lowerCase = text.lower()
print(text)
print(lowerCase)
print(string.punctuation)
# str1 : Specifies the list of characters that need to be replaced.
# str2 : Specifies the list of characters with which the characters need to be replaced
# str3 : Specifies the list of characters that needs to be deleted.
#
# Returns : Returns the translation table which specifies the conversions that can be used
cleanedText = lowerCase.translate(str.maketrans('','',string.punctuation))
print(cleanedText)
tokenizedWords = cleanedText.split()
print(tokenizedWords)

stopWords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

finalWords = []
for word in tokenizedWords:
    if word not in stopWords:
        finalWords.append(word)

print(finalWords)

# NLP Emotion Algorithm
# 1) Check if the word in the final word list is also present in emotion.txt
# - Open the emotion file
# - Loop through each line and clean it
# - Extract the word and emotion using split.
# 2) If word is present -> add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list.

emotionList = []
with open('emotions.txt','r') as emotionalFile:
    for fileLine in emotionalFile:
        # print(fileLine)
        cleanFileLine=fileLine.replace('\n','').replace(",","").replace("'","")
        # print(cleanFileLine)
        word,emotion = cleanFileLine.split(":")
        # print("Word: "+word)
        # print("Emotion: "+ emotion)

        if word.strip() in finalWords :
            emotionList.append(emotion.strip())

print(emotionList)
w = Counter(emotionList)
print(w)
fig, ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.xlabel('Emotions')
plt.ylabel('Count')
plt.title('Emotion Analysis')
plt.savefig('graph.png')
plt.show()






