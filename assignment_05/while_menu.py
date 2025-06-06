menu_option = ''

while menu_option != 'q':
    print('MENU:','a: Autoclaving Biohazardous Materials', 
          'b: Lab Procedures', 'q: quit', sep='\n')
    menu_option = input('Enter a letter for more info about the lab: ')
    if menu_option == 'a':
        print('Make sure to properly bag and mark materials before '
              'autoclaving.')
    elif menu_option == 'b':
        print('Be sure to wear PPE!')
