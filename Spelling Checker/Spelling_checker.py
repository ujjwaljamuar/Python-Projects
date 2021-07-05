from textblob import TextBlob
 
a = str(input('Enter a text : ') )          # incorrect spelling
print("Original text: "+str(a))
 
b = TextBlob(a)
 
# prints the corrected spelling
print("Corrected text: "+str(b.correct()))