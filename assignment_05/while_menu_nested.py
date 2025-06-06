menu_option = ''

while menu_option != 'q':
    print(f'''
          Lab Information FAQs:
          a: Autoclaving Biohazardous Materials
          b: Lab Procedures
          q: quit
          ''')
    menu_option = input('Enter a letter for more info about the lab: ')
    if menu_option == 'a':
        print('Make sure to properly bag and mark materials before '
              'autoclaving.')
    elif menu_option == 'b':
        lab_procedures = input('Have you read our Lab procedures? enter (y or n): ')
        if lab_procedures == 'y':
            print('Be sure to wear PPE!')
        else:
            print('Be sure to review our Lab procedures before our lab time.')
