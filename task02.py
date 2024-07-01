"""1.	Write a function pairwise_swap(tup) that takes a tuple of even length and returns a new tuple with each pair of elements swapped. """
# def pairwise_swap(tup):

"""
2.	Write a function unzip_tuples(tup_lst) that takes a list of tuples (each containing exactly two elements) and returns two tuples, one containing the first elements of each tuple, and the other containing the second elements.
"""
import string
tupleList = [(1,2,3,4),(5,6,7,8)]

def unzip_tuples(tupLst):
  firstTup = ()
  secondTup  = ()
  for tup in tupleList:
    firstTup = firstTup + tup[0:1]
    secondTup = secondTup + tup[1:2]
  return [firstTup, secondTup]
  
print(unzip_tuples(tupleList))


"""
3.	Write a function is_anagram(str1, str2) that takes two strings and returns True if they are anagrams of each other, otherwise False.
"""
def is_anagram(str1, str2):
   newString = str1.lower()
   newString2 =  str2.lower()
   str1 = sorted(newString)
   str2 = sorted(newString2)
   if  str1 == str2:
        print("True")
   else:
        print("false")
is_anagram("the file is my", "he is life tmy")
"""
4.	 Write a function capitalize_words(sentence) that takes a string sentence and returns a new string with the first letter of each word capitalized.
"""
def capitalize(sentence):
    return string.capwords(sentence)
print(capitalize("This text for testing"))
"""
5.	 Write a function compress_string(s) that takes a string and returns a compressed version where consecutive identical characters are replaced with the character followed by the count (e.g., "aaabb" becomes "a3b2"). If the compressed string is not shorter, return the original string.
"""
def compress_string(string):
    newString = "wedsk"
    for char in string:
        if string == newString:
         print(string)
        else:
         print(newString)
compress_string("Hello World")
"""
Sets
1.	Write a function find_common_elements(set1, set2) that takes two sets and returns a new set containing elements that are in both sets.
"""
newSet = set()
def find_common_element(set1,set2):

    for first in set1:
        for second in set2:
            if first == second:
               newSet.add(first)
    return(newSet)
print(find_common_element ({1,2,3,4},{2,5,6,1}))

"""

2.	Write a function unique_elements(lst) that takes a list of elements and returns a set of elements that appear exactly once in the list.
"""