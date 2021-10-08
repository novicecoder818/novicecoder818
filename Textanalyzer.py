"""
TEXT ANALYZER
"""
a_sentence = "Welcome Welcome Welcome To this Youtube Channel"
a = a_sentence.lower()
  #print(a)

alphabet = ("a","b","c","d","e","f","g","h",
            "i","j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z")
unique_words = []
"""Letter Frequency"""
#for i in alphabet:
 #   letter_frequency =a.count(i)
   # print(i,":",letter_frequency)

"""Word Frequency"""
words = a_sentence.split()
#print(words)
#for i in words:
#   word_frequency = words.count(i)
#   print(i,":",word_frequency)
    
#for word in words:
#    if word not in unique_words:
#           unique_words.append(word)
#   else:
#          pass
            
#for i in unique_words:
#         word_frequency = words.count(i)
#         print(i,";",word_frequency)



""""In a function"""
def TextAnalyzer():
    for i in alphabet:
        letter_frequency = a.count(i)
        print(i,":",letter_frequency)

    words = a_sentence.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
        else:
            pass

    for i in unique_words:
        word_frequency = words.count(i)
        print(i, ":",word_frequency)

    
 
