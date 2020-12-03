"""
Program is try to translate a sentence captured as user input.
Read in Text file textese.txt
then from text file we create a list of stings from each line in tect file
then create dictionary from list 
close file

define function for translating which invovles splitting user input (sentence) 
into array of strings 
(enjoy the excellent bad tonight)    
(enjoy, the, excellent, band, tonight)

once we have array of strings representing user input sentence:
loop through each words, find the key matching words and return back the value
tied to the word in our dictionary

print out translated sentence to the user
"""
"""
main:
    set sentence = input
    translate(sentence, dictioanry)


translate(sentence, dictionary):
words = for each word in sentence
for each word, translate word
print translated sentence

    
create_dictionary():
    read in textese.txt
    create list = each line from file
    close file
    create dictionary off of list
    return dictionary

main()
"""
def main():
    sentence = input("Enter a Sentence: ")
    dictionary = create_dictionary("textese.txt")
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, "r")
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(",") for word in words])


def translate(sentence, dictioanry):
    print("From translate", sentence)
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end= "")



main()