from array import*

Subjec = ['chem', 'Bio', 'Math','Ire', 'Geography']
#traversing

# for i in Subjec:
#     # print(i)

    #insert
Subjec.append('Business')
print(Subjec)
Subjec.insert(0, 'physics')
# print(Subjec)
# print(len(Subjec))
#deletion
# Subjec.pop(0)
Subjec.remove(Subjec[3])
print(Subjec)
Subjec.reverse();
print(Subjec)