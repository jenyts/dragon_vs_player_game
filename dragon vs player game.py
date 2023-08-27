import random
import time
try:
    name=input('enter a name :')
    print(f'{name},welcome to the mistory of "AWAKENING"')
    time.sleep(3)
    print('AWAKENING')
    time.sleep(4)
    print('Once up on a time there was a villege.Where people lived in harmony.But it was broken by the awakening of a DRAGON that lived beside that village ')
    time.sleep(4)
    print('The villegers were fritened by the awakaning of dragon.The villegers tried to defeat the dragon but their power was not near any range of dragon.The villegers began to loose their hopes ')
    time.sleep(4)
    print('The news of dragon began to spread around near villeges and  many people came to test their strength with the dragon, but no one got suceeded in it ')
    time.sleep(4)
    print(f'Then one day {name} came to that village to test his luck . {name} chalenged the dragon.')
    time.sleep(4)
    print('THE FIGHT BEGAIN')
    time.sleep(4)
    php=100
    dhp=100
    print('Both has HP of 100')
   
    print('The dragon made the first move')
    
    while php>=0 or dhp>=0:
        
        if php<=0 or dhp<=0:
            
            if dhp>php:
                 
                 print('Dragon won the fight')
                 print('The villege were distroyesd')
                 print('THE END')
                 break
            else:
                 print(f'The player {name} won the fight')    
                 print('The villegers lived in peace')
                 print('THE END')
                 break
        else:
            if php>0 or dhp>0:
              
                dragonmove=('flame thrower','leach','dragon breath','dragon claw','blaze')
                dragon=random.choice(dragonmove)
                print(f'Dragon used the move {dragon}')
    
                if dragon=='flame thrower':
                    php=php-20
                    print(f'now the {name} has a hp of {php}')
                elif dragon=='leach':
                    php=php-5
                    print(f'now the {name} has a hp of {php}')
                elif dragon=='dradon breath':
                    php=php-10
                    print(f'now the {name} has a hp of {php}')
                elif dragon=='dragon claw':
                    php=php-15
                    print(f'now the {name} has a hp of {php}')
                elif dragon=='blaze':
                    php=php-5
                    print(f'now the {name} has a hp of {php}')
                 
                
                playermove=('slash','bubble','water sword','dual slash','wave')
                print(f"these are the moves of {name} and the damages caused by it: slash=5,bubble=5,water sword=15,dual slash=15,wave=10")
                print(f'choose a move from these {playermove}')
                while True:

                    player=input('Enter a move ')
                
                    if player not in playermove:
                        print('only enter the moves thats given ')
                    else :
                        break

                if php>0: 

                    if player=='slash':
                        dhp=dhp-5
                        print(f'now the dragon has a hp of {dhp}')
                    elif player=='water sword':
                        dhp=dhp-15
                        print(f'now the dragon has a hp of {dhp}')
                    elif player=='bubble':
                        dhp=dhp-5
                        print(f'now the dragon has a hp of {dhp}')        
                    elif player=='dual slash':
                        dhp=dhp-15
                        print(f'now the dragon has a hp of {dhp}')
                    elif player=='wave':
                        dhp=dhp-10
                        print(f'now the dragon has a hp of {dhp}')  
except ValueError:
    print('value error has occured')    