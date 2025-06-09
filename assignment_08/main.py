def get_file_choice():
   choices = {'a': '60s-music.csv', 'b': 'athletes.csv'}
   while True:
       choice = input('''
What file would you like to search?:
a) 60s-music file
b) athletes file
x) to exit
''').lower()
       if choice == 'x':
           return None
       elif choice in choices:
           return choices[choice]
       else:
           print('Invalid option. Please select a, b, or x.')

def search_file(file_name, search_term):
   search_term = search_term.lower() # Normalize search term to lowercase
  
   with open(file_name, 'r') as file:
       content = file.read().lower() # Normalize file content to lowercase

   if search_term in content:
       print(f'Your search term "{search_term}" exists in the {file_name} file!')
       see_entries = input('Would you like to see the entries? (y or n)? ').lower()
       if see_entries == 'y':
           print(f'Here are all of the entries with the term "{search_term}":')
           with open(file_name, 'r') as file:
               for line in file:
                   if search_term in line.lower(): # Compare lowercase line
                       print(line.strip())
       elif see_entries == 'n':
           print('Okay, returning to main menu.')
           return # <-- This ensures we return to the main menu.
       else:
           print("Invalid option. Please enter y or n.")
   else:
       print(f'"{search_term}" does not exist in {file_name}')

def main():
   while True:
       file_name = get_file_choice()
   
       search_term = input(f'Enter the search term for {file_name} file: ').lower()
       search_file(file_name, search_term)

if __name__ == '__main__':
   main()

