print('welcome to our program')
print("enter 'quit' to leave the program")
active = True
while active:
        travel = ['kigali', 'joharnesberg', 'london']
        travel_place = input('where do you want to travel to?')
        ticket_no=input('how many tickets do you want?')
        if travel_place == 'kigali':
            del travel [0]
            print( ticket_no +' ticket for kigali purchased')
        elif travel_place == 'joharnesberg':
            del travel[1]
            print('one ticket for joharnesberg purchased')
        elif travel_place == 'london':
            del travel [2]
            print('one ticket for london purchased')
        else:
            print('please select a valid destination')
            print(travel[0].title())
            print(travel[1].title())
            print(travel[2].title())
          
        message=input("enter: \n'ok' to continue  \n'quit' to leave\n :")
        if message== 'quit':
            active = False
        elif message != 'ok' and message != 'quit' :
            print('please select a valid option \n ok: \n quit: ')
            message=input('write your answer')
            if message != 'ok':
               active= False      
               
            
