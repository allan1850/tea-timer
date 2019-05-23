#import time

#table of tea temps and times in C and minutes
dictTempLow = {'white': 70, 'green': 70, 'yellow': 70, 'oolong': 70, 'black': 80, 'puer': 85, 'roobios': 90, 'herbal': 85}
dictTempHigh = {'white': 80, 'green': 85, 'yellow': 85, 'oolong': 80, 'black': 100, 'puer': 100, 'roobios': 100, 'herbal': 100}
dictTimeLow = {'white': 1, 'green': 1, 'yellow': 1, 'oolong': 2, 'black': 3, 'puer': 2, 'roobios': 5, 'herbal': 4}
dictTimeHigh = {'white': 3, 'green': 3, 'yellow': 2, 'oolong': 3, 'black': 5, 'puer': 5, 'roobios': 6, 'herbal': 5} 

#user input and very basic validation
tea = input ("What type of tea? ")
strength = input ("How strong do you like your tea? Strong/Medium/Weak ")
tea = tea.lower()
strength = strength.lower()

#checking if tea and stregth are valid
if(not(tea in dictTempLow and (strength == 'strong' or strength == 'medium' or strength == 'weak') )):
    exit()
if(strength == 'strong'):
    temp = dictTempHigh.get(tea)
    time = dictTimeHigh.get(tea)
elif(strength == 'weak'):
    temp = dictTempLow.get(tea)
    time = dictTimeLow.get(tea)
else:
    temp = (dictTempHigh.get(tea) + dictTempLow.get(tea) ) / 2
    time = (dictTimeHigh.get(tea) + dictTimeLow.get(tea) ) / 2
temp = temp * (9/5) + 32
print(tea,"tea will take",time,"minute(s) at",temp, "degrees.")

#LED on GPIO
# 7segment LED on GPIO

    

