'''Save the sentence given as a string
replace every exclamation mark with a blank space
Change all the letters in the sentence into an upper case
and finally print the sentence in reverse'''



Sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog"
Sentence_rep = Sentence.replace("!"," ")
print(Sentence_rep)
Sentence_rep_upper = Sentence_rep.upper()
print(Sentence_rep_upper)
Sentence_rev = Sentence_rep_upper[::-1]
print(Sentence_rev)