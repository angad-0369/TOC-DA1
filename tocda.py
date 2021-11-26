import re #import regex library
def matching_pattern(): #making a function matching_pattern
    identif=re.compile(r'[A-Z]*[a-z]+[0-9]*[@]+') #making a regular expression
    pat=input('Enter the identifier you want to validate:') #taking input from
    res=re.match(identif,pat) #matching the regular expression with the input
    if(res):
        print('Valid identifier') #if the input is valid
    else:
        print('Invalid identifier') #if the input is invalid
def main():
    matching_pattern() #calling the function
if __name__ == "__main__": #calling the main function
     main()