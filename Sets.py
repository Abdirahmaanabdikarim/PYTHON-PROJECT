

SetofNaturalNumbers ={1,2,3,4,5,6,7,8,9,10,11}
setOfEvenNumbers ={2,4,6,8,10}


print(SetofNaturalNumbers-setOfEvenNumbers)#this is what is common

print(SetofNaturalNumbers.intersection(setOfEvenNumbers))
print(SetofNaturalNumbers|setOfEvenNumbers)

print(SetofNaturalNumbers& setOfEvenNumbers)#intersection of the set


print(SetofNaturalNumbers.issubset(setOfEvenNumbers))
print(setOfEvenNumbers.issubset(SetofNaturalNumbers))
