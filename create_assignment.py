import pyautogui
import time

# something to try next time: 
# calculate the correct number of assignments by reading the html
# <div class="table--header"><h1>13 Assignments</h1>

def multi_tabs(n):
    for i in range(n):
        time.sleep(0)
        pyautogui.press('tab')

def new_assignment(assignment_name,releasedate,closedate,latedate,p=1.5,s=0):
    print('')
    a1=input('press enter when you are ready to start')
    time.sleep(p)
    pyautogui.keyDown('command')
    pyautogui.press('l')
    pyautogui.keyUp('command')
    pyautogui.keyDown('shift')
    multi_tabs(4)
    pyautogui.keyUp('shift')
    multi_tabs(1)
    pyautogui.press('enter')
    
    multi_tabs(2)
    
    pyautogui.press('down')
    pyautogui.press('enter')
    
    multi_tabs(3)
    pyautogui.press('enter')
    
    pyautogui.write(assignment_name, interval = s)
    
    multi_tabs(1)
    pyautogui.press('enter')
    
    print('')
    a1=input('press enter when you are ready for the next step')
    time.sleep(p)
    multi_tabs(3)
    pyautogui.write(releasedate, interval = s)
    multi_tabs(1)
    pyautogui.write(closedate, interval = s)
    
    print('')
    a1=input('press enter when you are ready for the next step')
    time.sleep(p)
    multi_tabs(9)
    pyautogui.press('left')
    pyautogui.keyDown('fn')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.keyUp('fn')
    pyautogui.write(latedate, interval = s)

# that's probably all you need to do! you should probably press 'create
# assignment' yourself after looking over the details 

#mp6='Mastery Problem Set 6:'
#mp6_release='03/20/2021 11:00 AM'
#mp6_close='03/21/2021 11:59 PM'
#mp6_late='03/23'

assmt='Worksheet 8: Factors, Multiples, and Elementary Number Theory'
release='03/18/2021 12:00 AM'
due='03/22/2021 11:59 PM'
late='03/23'

new_assignment(assmt,release,due,late)

