def again():
        

 while True: #running until i ecplisitly stop it by exit

  print("-"*26)
  print("|","WELCOME TO VOWEL ARENA","|")
  print("-"*26)
  
  print("-"*19)
  print("|"," "*3,"OPTIONS"," "*3,"|")
  print("|"," "*15,"|")
  print("|"," "*2,"1.DETAILS"," "*2,"|")   
  print("|"," "*2,"2.START"," "*4,"|")
  print("|"," "*2,"3.Exit"," "*5,"|")
  print("-"*19)


  choice = int(input("select your choice TYPE (1/2/3):"))
 


  if choice == 1:


    print(" "*15,"|","WLC IN DETAILS SECTION","|")

    print("-"*55)
    print("|"," "*2,"1.Game consists of 5 rounds"," "*20,"|")   
    print("|"," "*2,"2.Each round - Enter word"," "*22,"|")   
    print("|"," "*2,"3.Vowels are removed from each word"," "*12,"|")
    print("|"," "*2,"4.Score is calculated"," "*26,"|")   
    print("|"," "*2,"4.Results are diplayed in the end of 5th round"," ","|")   
    print("-"*55)


    print(" "*25,"|","RULES","|")

    print("-"*70)
    print("|"," "*2,"1.WORD MUST CONTAIN AT LEAST ONE VOWEL. |BANANA✔️ | |rhythm❌|"," "*1,"|")   
    print("|"," "*2,"2.WORD LENGTH MUST BE BETWEEN 4 AND 10 CHARACTERS."," "*12,"|")   
    print("|"," "*2,"3.NO REPEATED LETTERS EX-aaaaaa❌"," "*29,"|")
    print("|"," "*2,"4.ONLY ALPHABETS ARE ALLOWED."," "*33,"|")
    print("|"," "*2,"5.PREVIOUSLY USED WORDS CANNOT BE REUSED."," "*21,"|")   
    print("|"," "*2,"6.EVERY VOWEL REMOVED GIVES 1 POINT"," "*27,"|")   
    print("-"*70)

  elif choice==2:
    print("-"*26)
    print("|","WELCOME TO VOWEL ARENA","|")
    print("-"*26)
    total = 0
    used_words = []
   
    for wrd in range(5):
        score = 0
        val=0
        count = 0
        wrd_vowel = ""
        wrd = input("| ENTER THE WORD HERE:-")
        wrd = wrd.lower()
        if wrd in used_words:                 #sixth RULE -> used_wrd 
          print("repeated word Not allowed")
          continue 
        used_words.append(wrd)
        for i in range(1,len(wrd)): #second the repeated condi.. rule
         if wrd[i] == wrd[i-1]:
           count+=1
        if count>=2:
           print("do not stretch the word")
           continue
        if len(wrd)<=4 or len(wrd)>=11: # One char size condition applied
           print("reminder:-.ch length should be btw 4 and 11| this chance is waste")  # One char size condition applied
           continue  
        if not wrd.isalpha(): #third no num in wrd RULE
          print("Only alphabet is allowed")  
          continue
        if wrd == 'aeiou' or wrd =='uoiea':
          print("direct aeiou wrd is not allowed")
          continue
        # elif wrd[1:] == wrd[:-1]:  #second the repeated ch/wrd condition .
        #   print("repeated character not allowed!!")
        #   continue  
        wrd = wrd.lower()  #fourth
        for ch in wrd:   #fifth
         if ch in "aeiou" :
          val+=1   #for the vowel count
        # if wrd == "A" or wrd == "E" or wrd == "I"or wrd == "O"or wrd == "U"or wrd == "a" or wrd == "e":
          continue
         wrd_vowel += ch
        score +=1
        total = total +  val  #vowel total
        print(wrd,":",score,":",val," |word|->",wrd_vowel)
    print("TOTAL POINTS-",total)


  elif choice == 3:
    print("succssfully exit from the program")
    return 
  else:
   print("invalid choice")
   break
  
again()

# no num allowed rul ]
#no using privious entered word