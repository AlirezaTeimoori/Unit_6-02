# Created by: Alireza Teimoori
# Created on: Dec 2017
# Unit_6-02
# This app is for practicing ENUM

from enum import Enum

Day = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
#print("what is your favorite day?")

while True:
    print('Hello!')
    day_selected = raw_input('what is your favorite day?'+'\n')
    if day_selected in Day:
        counter = 1
        print (day_selected + ' is a valid day') 
        for a_day in Day:
            if day_selected == str(a_day):
                print (counter)
            else:
                counter = counter + 1
                
        print("Thank you! Bye!"+"\n\n")
    else:
        print('Wrong Input.')     
        day_selected = int(input('At least enter a number for day of the week to see its name!...'))
        if 1 <= day_selected <= 7:
            print('That day would be...hmmmmm...')
            print(Day[day_selected-1])
            print("Thank you! Bye!"+"\n\n")
        else:
            print("Whats wrong with you!? :|      Seriously... \n Bye!... \n\n")
