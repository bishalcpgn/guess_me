from random import randint
from os import system 
#outer loop to continue the game
while True:
    count=0
    user_entry=[]
    num=randint(0,100)
    print("\n\n\033[1;33m************************************************\033[00m")
    print("\033[5;33m               GUESS_ME    \033[00m")
    print("\033[1;33m************************************************\033[00m")
#inner loop    
    while True:
        count+=1
        print(f"\n\033[5;33mAttempt : {count}\033[00m")
        try:
            user_data=int(input("\033[5;33m Guess the number between 0-100 : \033[00m"))
 #checks if number is alredy entered
            if user_data in user_entry:
                print(f"Oops .. , You have already tried {user_data}")
#update the entry           
            user_entry.append(user_data)
 #conditions with entry         
            if user_data<0 or user_data>100:
                print("Enter number between 0-100.\n")
                print("\033[5;33m************************************************")
            elif user_data==num:
                print(f"\n\033[5;33mYou won in {count} attempts.\n")  
                print(f"\n\033[5;33mYour entries : {user_entry}\n")  

                print("\033[5;33m************************************************")
                print("\033[5;33m************************************************")

                break
            elif user_data<num:
                    print("Hint : Guess higher number.\n")
                    print("\033[5;33m************************************************")

            elif user_data>num:
                    print("Hint : Guess lower number.\n")
                    print("\033[5;33m************************************************")

            
        except:
            print("\n\n\033[5;33mSomething wrong in your entry ...  !! \n\n")
            break
 #outer loop try and except   
    try:
        if input("\n\033[5;33mEnter 'y' to retart any other key to exit : ") == "y" :
            system('clear')
            continue
        else :
            exit("\nThank you !!\n\n")
    except :
       exit("\n\nThank you !!\n\n")
           

    

