import PySimpleGUI as sg
import os

from my_functions import check_files, create_files, add_html_content, MY_FILES, HTML_BOILERPLATE


#layout
sg.theme('DarkBrown')

layout = [
    [sg.Text('Enter the url below and press enter to create files', 
             text_color= 'White', key='-msg-',
             justification='center')],
    [sg.Input(key='-input-',expand_x=True, tooltip= 'Enter Url..', 
                  text_color= 'White', size=(100, 40))],
     [sg.Button('Enter', key='-btn-', button_color= ('Teal','LightGreen'),
                size=(10, 40), expand_x=True)]
    ]


#creating window object
window = sg.Window('Create HTML CSS JS FILES', layout, size=(550,200))


# Event loop starts
while True:
    event, values = window.read()
    print(f"event: {event}, values: {values}")
    
    if event == sg.WIN_CLOSED:
        break
    elif event == '-btn-':
        window['-btn-'].update(button_color = ('Yellow'))
        
        # get path from input
        path = values['-input-']
        
        if os.path.exists(path) == False:
            window['-msg-'].update(text_color = 'Red')
            window['-msg-'].update('PATH DOES NOT EXIST')
        else:
            #change directory
            os.chdir(path)

            #file check
            file_check = check_files()
            
            if file_check == 1:
                window['-msg-'].update(text_color = 'Red')
                window['-msg-'].update('FILES ALREADY EXIST')
            else:
                create_files(MY_FILES)
                
                add_html_content(HTML_BOILERPLATE)
                
                window['-msg-'].update(text_color = 'LightGreen')
                window['-msg-'].update('FILES HAS BEEN CREATED')
        

window.close()