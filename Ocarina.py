import time
import picokeypad


keypad = picokeypad.PicoKeypad()

#Buttons
a_button = '9, 0x00, 0x00, 0x20'
c_up = '0, 0x20, 0x20, 0x00'
c_left = '4, 0x20, 0x20, 0x00'
c_right = '1, 0x20, 0x20, 0x00'
c_down = '5, 0x20, 0x20, 0x00'
r_button = '6, 0x40, 0x40, 0x40'
z_button = '10, 0x50, 0x50, 0x50'

#Songs
Epona = ['c_up','c_left','c_right','c_up','c_left','c_right']
Zelda = ['c_left','c_up','c_right','c_left','c_up','c_right']
Saria = ['c_down','c_right','c_left','c_down','c_right','c_left']
Sun = ['c_right','c_down','c_up','c_right','c_down','c_up']
Time = ['c_right','a_button','c_down','c_right','a_button','c_down']
Storm = ['a_button','c_down','c_up','a_button','c_down','c_up']
Forest = []
Water = []
Spirit = []
Light = []
Example = ['c_up','c_up','c_up','c_up','c_up','c_up']

Choice = []

#Animations
def showstorm():
    print("Storm")
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x10, 0x50)
    keypad.update()
    time.sleep(2)
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update() 
    
    keypad.illuminate(0, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)      
    keypad.illuminate(5, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(0, 0x00, 0x00, 0x00)
    keypad.illuminate(9, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.illuminate(10, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(5, 0x00, 0x00, 0x00)
    keypad.illuminate(14, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(9, 0x00, 0x00, 0x00)
    keypad.illuminate(15, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(10, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(14, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(15, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)
    
    
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(5, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)      
    keypad.illuminate(6, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(1, 0x00, 0x00, 0x00)
    keypad.illuminate(10, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(5, 0x00, 0x00, 0x00)
    keypad.illuminate(11, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(6, 0x00, 0x00, 0x00)
    keypad.illuminate(15, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(10, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(11, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)
    keypad.illuminate(15, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(0.1)

    Choice.clear()
        
def showepona():
    print("Epona")
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x50, 0x00)
    keypad.update()
    time.sleep(2)
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update() 
    
    keypad.illuminate(12, 0x80, 0x40, 0x20)
    keypad.illuminate(13, 0x80, 0x40, 0x20)
    keypad.illuminate(9, 0x80, 0x40, 0x20)
    keypad.illuminate(10, 0x80, 0x40, 0x20)
    keypad.illuminate(8, 0x80, 0x60, 0x40)
    keypad.illuminate(5, 0x80, 0x60, 0x40)
    keypad.illuminate(6, 0x80, 0x40, 0x20)
    keypad.illuminate(7, 0x80, 0x40, 0x20)
    keypad.illuminate(11, 0x80, 0x40, 0x20)
    keypad.illuminate(0, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(0, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()        
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(1, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(0, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(0, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(12, 0x00, 0x00, 0x00)
    keypad.illuminate(13, 0x00, 0x00, 0x00)
    keypad.illuminate(15, 0x00, 0x00, 0x00)
    keypad.illuminate(11, 0x00, 0x00, 0x00)
    Choice.clear()
    
def showzelda():

    print("Zelda")
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x50, 0x00)
    keypad.update()
    time.sleep(2)
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update() 
    
    keypad.illuminate(5, 0x20, 0x20, 0x00)
    keypad.illuminate(6, 0x20, 0x20, 0x00)
    keypad.illuminate(7, 0x20, 0x20, 0x00)
    keypad.illuminate(9, 0x20, 0x20, 0x00)
    keypad.illuminate(10, 0x20, 0x20, 0x00)
    keypad.illuminate(13, 0x20, 0x20, 0x00)
    
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(0, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(0, 0x00, 0x00, 0x00)
    keypad.update()        
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(1, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(0, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(0, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(13, 0x00, 0x00, 0x00)

    Choice.clear()
        
def showsun():
    Choice.clear()
def showsaria():
    print("Saria")
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x50, 0x00)
    keypad.update()
    time.sleep(2)
    for i in range(16):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update() 
    
    keypad.illuminate(2, 0x00, 0x60, 0x00)
    keypad.illuminate(5, 0x00, 0x60, 0x00)
    keypad.illuminate(7, 0x00, 0x60, 0x00)
    keypad.illuminate(13, 0x00, 0x60, 0x00)
    keypad.illuminate(8, 0x00, 0x60, 0x00)
    keypad.illuminate(9, 0x00, 0x00, 0x60)
    keypad.illuminate(6, 0x00, 0x00, 0x60)
    keypad.illuminate(15, 0x80, 0x40, 0x20)
    keypad.illuminate(10, 0x80, 0x40, 0x20)
    keypad.illuminate(11, 0x80, 0x40, 0x20)
    keypad.illuminate(14, 0x80, 0x40, 0x20)
    keypad.update()
    keypad.illuminate(5, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(5, 0x00, 0x60, 0x00)
    keypad.update()
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(1, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(1, 0x00, 0x00, 0x00)
    keypad.update()
    keypad.illuminate(5, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(5, 0x00, 0x60, 0x00)
    keypad.update()
    keypad.illuminate(4, 0x20, 0x20, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(4, 0x00, 0x00, 0x00)
    keypad.update()
    time.sleep(1)
    keypad.illuminate(12, 0x00, 0x00, 0x00)
    keypad.illuminate(13, 0x00, 0x00, 0x00)
    keypad.illuminate(15, 0x00, 0x00, 0x00)
    keypad.illuminate(14, 0x00, 0x00, 0x00)
    keypad.illuminate(11, 0x00, 0x00, 0x00)
    Choice.clear()
def showtime():
    Choice.clear()
while True:
#Link button presses to variables and clear lights when not pressed
    button_states = keypad.get_button_states()
    print(button_states)
    time.sleep(0.2)
    for i in range(11):
        keypad.illuminate(i, 0x00, 0x00, 0x00)
    keypad.update() 
    keypad.illuminate(0, 0x50, 0x50, 0x00)
    keypad.illuminate(1, 0x50, 0x50, 0x00)
    keypad.illuminate(4, 0x50, 0x50, 0x00)
    keypad.illuminate(5, 0x50, 0x50, 0x00)
    keypad.illuminate(9, 0x00, 0x00, 0x50)
    keypad.illuminate(6, 0x40, 0x40, 0x40)
    keypad.illuminate(10, 0x50, 0x50, 0x50)
    keypad.update()
    
#Button input and choose animation based on choice
    if len(Choice) < 6:
        if button_states == 1:
            keypad.illuminate(0, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('c_up')
                print (Choice)
            elif Choice[-1] != 'c_up':
                Choice.append('c_up')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 2:
            keypad.illuminate(1, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('c_right')
                print (Choice)
            elif Choice[-1] != 'c_right':
                Choice.append('c_right')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 16:
            keypad.illuminate(4, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('c_left')
                print (Choice)
            elif Choice[-1] != 'c_left':
                Choice.append('c_left')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 32:
            keypad.illuminate(5, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('c_down')
                print (Choice)
            elif Choice[-1] != 'c_down':
                Choice.append('c_down')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 512:
            keypad.illuminate(9, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('a_button')
                print (Choice)
            elif Choice[-1] != 'a_button':
                Choice.append('a_button')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 64:
            keypad.illuminate(6, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('r_button')
                print (Choice)
            elif Choice[-1] != 'r_button':
                Choice.append('r_button')
                print (Choice)
            else:
                print (Choice)
        elif button_states == 1024:
            keypad.illuminate(10, 0x00, 0x50, 0x00)
            keypad.update()
            if len(Choice) == 0:
                Choice.append('z_button')
                print (Choice)
            elif Choice[-1] != 'z_button':
                Choice.append('z_button')
                print (Choice)
            else:
                print (Choice)
    
    elif Choice == Epona:
        showepona()
    elif Choice == Zelda:
        showzelda()
    elif Choice == Storm:
        showstorm()
    elif Choice == Saria:
        showsaria()
    else:
        print("GanonDorrrrrffff!!!!!")
        for i in range(16):
            keypad.illuminate(i, 0x50, 0x00, 0x00)
        keypad.update()
        time.sleep(2)
        for i in range(16):
            keypad.illuminate(i, 0x00, 0x00, 0x00)
        keypad.update() 
        keypad.illuminate(1, 0x50, 0x00, 0x00)
        keypad.illuminate(2, 0x50, 0x00, 0x00)
        keypad.illuminate(4, 0x50, 0x00, 0x00)
        keypad.illuminate(5, 0x50, 0x00, 0x00)
        keypad.illuminate(8, 0x50, 0x00, 0x00)
        keypad.illuminate(6, 0x50, 0x50, 0x00)
        keypad.illuminate(9, 0x50, 0x50, 0x00)
        keypad.illuminate(10, 0x00, 0x50, 0x00)
        keypad.illuminate(11, 0x00, 0x50, 0x00)
        keypad.illuminate(14, 0x00, 0x50, 0x00)
        keypad.update()
        time.sleep(2)
        
        
        for i in range(16):
            keypad.illuminate(i, 0x00, 0x00, 0x00)
        keypad.update() 
        Choice.clear()
        
