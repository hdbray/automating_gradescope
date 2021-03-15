import pyautogui
import time

# something to try next time: 
# calculate the correct number of assignments by reading the html
# <div class="table--header"><h1>13 Assignments</h1>

def pause_prompt():
    print('')
    a1=input('press enter when ready')


def multi_tabs(n):
    for i in range(n):
        time.sleep(0)
        pyautogui.press('tab')

def rev_multi_tabs(n):
    pyautogui.keyDown('shift')
    multi_tabs(n)
    pyautogui.keyUp('shift')

def create_rubric(rubric_item, pts, with_pause=True, p=1.5,s=0):
    if with_pause==True:
        pause_prompt()
    time.sleep(p)

    pyautogui.keyDown('command')
    pyautogui.press('l')
    pyautogui.keyUp('command')

    rev_multi_tabs(9)
    pyautogui.press('enter')

    rev_multi_tabs(1)
    multi_tabs(1)
    pyautogui.press('enter')

    pyautogui.press('left')
    pyautogui.press('left')
    pyautogui.keyDown('fn')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.press('delete')
    pyautogui.keyUp('fn')

    pyautogui.write(rubric_item, interval = s)

    rev_multi_tabs(1)

    pyautogui.write('-' + str(pts))

    pyautogui.press('enter')


def create_multi_rubric(list_rubric_pt_pairs,with_pause=True,p=1.5):
    if with_pause==True:
        pause_prompt()
        time.sleep(p)
    for rubric_pt_pair in list_rubric_pt_pairs:
        rubric_item=rubric_pt_pair[0]
        pts=rubric_pt_pair[1]
        create_rubric(rubric_item, pts,False,p)


def create_multi_prob_rubric(rubric_item,pts,num_probs,p=1.5):
    pause_prompt()
    time.sleep(p)

    for i in range(num_probs):
        create_rubric(rubric_item, pts, False)
        pyautogui.press('.')

def create_multi_prob_multi_rubric(list_rubric_pt_pairs,num_probs,p=1.5):
    pause_prompt()
    time.sleep(p)

    for i in range(num_probs):
        create_multi_rubric(list_rubric_pt_pairs,False)
        pyautogui.press('.')


first_rubric_item='testing'

#create_rubric(first_rubric_item,1)

#create_multi_rubric(first_rubric_item,1,3)

first_list_rubric_items=[('first rubric item',1),('second rubric item',2)]

#create_multi_rubric(first_list_rubric_items)

#create_multi_rubric(first_list_rubric_items, 3)

