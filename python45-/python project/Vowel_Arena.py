import random
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
    used_CP = []
    CP_total = 0
    for wrd in range(5):
                         # type: ignore
        Round_wrd = 0
        val=0
        count = 0
        wrd_vowel = ""
        wrd = input("| ENTER THE WORD HERE:-")
        print()
        wrd = wrd.lower()
     
        if wrd in used_words:                 #sixth RULE -> used_wrd 
          print("!!repeated word Not allowed!!")
          print()
          continue 
        used_words.append(wrd)
        for i in range(1,len(wrd)): #second the repeated condi.. rule
         if wrd[i] == wrd[i-1]:
           count+=1
        if count>=2:
           print("!!do not stretch the word !!")
           print()
           continue
        if len(wrd)<=4 or len(wrd)>=11: # One char size condition applied
           print("!!-reminder:-.ch length should be btw 4 and 11| this chance is waste-!!")  # One char size condition applied
           print()
           continue  
        if not wrd.isalpha(): #third no num in wrd RULE
          print("Only alphabet is allowed")  
          print()
          continue
        if wrd == 'aeiou' or wrd =='uoiea':
          print("direct aeiou wrd is not allowed")
          print()
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
        Round_wrd += len(used_words)
        total = total + val  #vowel total
        print("-"*4,"US_ROUND:","-"*4,"{",Round_wrd,"}")
        print("You:",wrd,":","score",":",val )
        print("|Eaten|->",wrd_vowel)
        print()
        CP_total = Comp_player(Round_wrd, used_CP, CP_total)
    print("US_TOTAL POINTS-",total)

  elif choice == 3: 
    print("succssfully exit from the program")
    return 
  else:
   print("invalid choice")
   break
  

def Comp_player(nob,used_CPP,CPP_total):
  
  CP_wrds =[ "audience","aeroplane","oceanic","euphoria","picture","holiday", "family","journey", "welcome",
            "america", "article", "library", "academy", "elephant", "umbrella", "hospital"]
 

  
  CP_wrd = random.choice(CP_wrds)  #***
  CP_wrd = CP_wrd.lower()
  for x in range(1):
        val=0
        count = 0     
        CP_vowel = ""
        if CP_wrd in used_CPP:                 #sixth RULE -> used_wrd 
         print("repeated word Not allowed")
         continue 
        used_CPP.append(CP_wrd)

        for i in range(1,len(CP_wrd)): #second the repeated condi.. rule
          if CP_wrd[i] == CP_wrd[i-1]:
           count+=1
        if count>=2:
           print("do not stretch the word")
           continue
        if len(CP_wrd)<=4 or len(CP_wrd)>=13: # One char size condition applied
           print("reminder:-.ch length should be btw 4 and 11| this chance is waste")  # One char size condition applied
           continue  
        if not CP_wrd.isalpha(): #third no num in wrd RULE
           print("Only alphabet is allowed") 

           continue
        if CP_wrd == 'aeiou' or CP_wrd =='uoiea':
           print("direct aeiou wrd is not allowed")
           print()
           continue
        # # elif wrd[1:] == wrd[:-1]:  #second the repeated ch/wrd condition .
        #   print("repeated character not allowed!!")
         # continue  
          
        CP_wrd = CP_wrd.lower()  #fourth 
        for ch in CP_wrd:   #fifth
          if ch in "aeiou" :
            val+=1   #for the vowel count
        # if wrd == "A" or wrd == "E" or wrd == "I"or wrd == "O"or wrd == "U"or wrd == "a" or wrd == "e":
            continue
          CP_vowel += ch
        CPP_total = CPP_total +  val  #vowel total #total reset prib*****
        print("-"*4,"PC_ROUND:","-"*4,"{",nob,"}")
        print("PC:",CP_wrd,":","score",":",val)
        print("|Eaten|->",CP_vowel)
        print()
  if nob == 5:
    print("CP_TOTAL POINTS-", CPP_total)  
    return CPP_total
  
again()
