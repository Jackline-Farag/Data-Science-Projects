str_manip = input(" Enter a Sentence: ")
print(str_manip)

sentence_len = len(str_manip)
print(sentence_len)

idx= str_manip[-1]
print(idx)

msg_rep = str_manip.replace(str_manip[-1],"@")
print(msg_rep)

Three_last= str_manip[:-4:-1]
print(Three_last)

Three_letter_first= str_manip[0:3]
Two_last=str_manip[-2:]
print(Three_letter_first+Two_last)