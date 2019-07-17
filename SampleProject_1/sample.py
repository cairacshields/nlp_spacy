#import spacy to begin 
import spacy

# also import Matcher from spacy
from spacy.matcher import Matcher

#load the english version of spacy 
nlp = spacy.load('en_core_web_sm')


#Tokenization (The art of breaking up text into individual tokens that hold deeper information such as: Parts Of Speech, Lemma's, Named Entities, etc.)
#-----------------
doc = nlp(u'Tesla is a company that is looking to purchase several startups for $6 millon.')
# for token in doc:
#   print(token.pos_)

#-----------------




#Lemma's (Lemmatization is the art of finding the true root of a work based on it's overall context)
#---------------
doc1 = nlp(u"Welcome to the amazing world of gumball, a show about a blue guy with super cool humor powers running the world.")

# for token in doc1:
#   print(token.lemma_)

  # Should output the root of a word, if it can understand one

#----------------




#Stop Words (Words that commonly don't hold any value, and can sometimes make the NLP more difficult)
#----------------
#print(nlp.Defaults.stop_words) #Should print a set of about 300+ stop words 
  
  #Checking if a word is a stop work
  # nlp.vocab['btw'].is_stop #Should return false

  # #Adding our own stop words 
  # nlp.Defaults.stop_words.add('btw')
  # nlp.vocab['btw'].is_stop = True 

  # #Removing our own stop words 
  # nlp.Defaults.stop_words.remove('btw')
  # nlp.vocab['btw'].is_stop = False 


# Matcher 
# --------------

#Set up the matcher:
matcher = Matcher(nlp.vocab)

# We can open a .txt file from our directory 
with open('./TextFiles/frenchToast.txt') as f:
  doc3 = nlp(f.read())

#print(doc3)

# Check how many words/tokens are in the document 
#print(len(doc))

#Check how many sentences are in a document 
  # We should start by chopping the document up into a list of sentences 
  doc_sentences = [sent for sent in doc3.sents] # <---- we are using list conprehension to form a list from every sentence in the given document
  # print(len(doc_sentences))

# Create a pattern to match on
pattern = [{'LOWER': 'french'}]

# Add the pattern to our matcher 
matcher.add('MatchPatter1', None, pattern)

# Now we can go through our document and grab all of the matches for the given pattern (right now it's just a single lower case word 'french')
found_matches = matcher(doc3)

#If we print out found_matches, we should see a list of all the matches that were found. They will hold the id for the match, as well as the start and end index in the doc
 #print(found_matches)

#We can also print out the sentence surrounding our match by using the start abnd end position that was returned to us
  #Let's create a simple function that will search a given document for the phrase starting and ending at a given index
def surrounding(document, start, end):
  print(document[start-5:end+10])
  #Now let's call it using the matcher values we got back previously
# surrounding(doc3, found_matches[0][1], found_matches[0][2])  

# Here we create a function that will esentially use the start index of our match word to find and print the full sentence that it belongs to...
def returnFullSentence():
  for sentence in doc_sentences:
    if found_matches[0][1] < sentence.end :
      print(sentence)
      break
returnFullSentence()















print("Spacy and NLP 101...")