#basic String Functions

first_string="hello world!!!"
print(first_string)
first_string[0]
first_string[1]="e"      #will give us error as string is an immutable datatype.

# STRING FUNCTIONS


len(first_string)

first_string.title()
first_string.lower()
first_string.upper()

#to count a word
str1="hello world;Hello Hello hELLO"
str1=str1.lower()
str1.count("hello")     #it will show 4
str1.count("hello",11,29)   #result=3

#to find the index of a word
str1="hello world;Hello Hello hELLO"
str1=str1.lower()
str1.find("hello",10,28)    #result=12
str1.find("hello")      #result=0
str1.find("heee")       #result=-1 as the word is not present in the string

#same as find but on;y restuns error when the word can not be found
str1="hello world;Hello Hello hELLO"
str1=str1.lower()
str1.index("hello",10,28)    #result=12
str1.index("hello")      #result=0
str1.index("heee")       #result=error as the word is not present in the string

#returns true or false
str1="hello world;Hello Hello hELLO"
str1=str1.lower()
str1.endswith("!")      #result=false
str1.endswith("llo")    #result=true

str1.startswith("hee")  #result=False
str1.startswith("hel")  #result=true

str1.isalnum()      #result=flase as a symbol ";" present there
str2="hello hii how are you123"
str2.isalnum()      #result=true

str1.isspace()       #result=flase
str2="hello \t hii \t how \t are \t you123"
str2.isspace()      #result=flase
str3="\n \t \t \n"
str3.isspace()      #result=true as it only contain escape key

str1.islower()      #result=true
str1.isupper()      #result=flase
str1.istitle()      #result=flase


#to strip the excess space in a string
str2="        hello        "
str2.lstrip()       #result='hello        '
str2.rstrip()       #result='        hello'
str2.strip()        #result='hello'

#to replace old string with new one
str1="hello world"
str1.replace("hello","hii")     #result='hii world'
str1.replace("world","India")    #result='hello India'

#to join two string
str1="hello world"
str2="><"
str2.join(str1)     #result='h><e><l><l><o>< ><w><o><r><l><d'
str1.join(str2)     #result='>hello world<'


#to make partition. It is a function which always returns three value.
str1="My motherland is India"
str1.partition("is")        #result=('My motherland ', 'is', ' India')
str1.partition("are")       #result=('My motherland is India', '', '')

#to split every word of a string
str1="My motherland is India"
str1.split()        #result=['My', 'motherland', 'is', 'India']
str1.split("i")     #result=['My motherland ', 's Ind', 'a']