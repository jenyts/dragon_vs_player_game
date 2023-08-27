import time
import datetime

def quiz():
    name=input('enter your name :')
    print(f'HELLO! WELCOME TO THE QUIZ {name}')

    c=0
    print('read the instructions correctly')

    print('INSTRUCTIONS')
    time.sleep(2)
    print('There will be five questions')
    time.sleep(2)
    print('You have 7second to answer the question')
    time.sleep(2)
    print('You have 4 options for each question to choose')
    time.sleep(2)
    print('you should only type the option or else the answer will be taken as wrong') 
    time.sleep(2)
    print('example:\n Q)full form of cpu? \n options:a)center processing unit b)central processing unit  c)central produced unit  d)central unit \n enter your answer:b')
    time.sleep(2)
    print('the total score can be only seen after completing the 5 questions')
    time.sleep(2)
    print('do you want to play the game')
    st=input('type yes to continue /no to exit:')
    print("LET'S START THE QUIZ")
    if st=='no':
       
        print('thank you for your time')  
    else:        
        current_time=datetime.datetime.now().time()
        print("start time:",current_time)
        q=print('1.Python is a ________ level programing language')
        print('options: a)low    b)free    c)high    d)medium')
        

        ans=input('enter your answer: ')
         
        
        a='c)high'
        if ans=='c':
            print('the answer is correct')
            c+=1
        else:
            print(f'the answer is wrong, the correct answer is{a}')   
        
        
        q=print('2.which among the option is not a numeric data type')     
        print('options: a)int    b)str    c)float    d)complex')
        ans=input('enter your answer: ')
        
        a='b)str'
        if ans=='b':
            print('the answer is correct')
            c+=1
        else:
            print(f'the answer is wrong, the correct answer is {a}')  
        
        
        q=print('3.string is denoted as ________') 
        print('options: a)bool    b)dict    c)list    d)str')
        ans=input('enter your answer: ')
        
        a='d)str'
        if ans=='d':
            print('the answer is correct')
            c+=1
        else:
            print(f'the answer is wrong, the correct answer is {a}') 


        q=print('4.how many forms of if....else statement type are there?')    
        print('options: a)3    b)4    c)2    d)5')     
        ans=input('enter your answer: ')
    
        a='a)3'
        if ans=='a':
            print('the answer is correct')
            c+=1
        else:
            print(f'the answer is wrong, the correct answer is {a}')


        q=print('5.which is not a characterastics of list')
        print('options:a)orderd    b)mutable    c)immutable    d)dynamic')
        ans=input('enter your answer: ')
        
        a='c)immutable'
        if ans=='c':
            print('the answer is correct')
            c+=1
        else: 
            print(f'the answer is wrong, the correct answer is {a}')    
        current=datetime.datetime.now().time()
        print("endtime:",current)
        print(f'you have {c} score')            
        print(f'you completed the quiz between {current_time} and {current}')
quiz()


