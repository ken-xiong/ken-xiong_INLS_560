# This program checks whether you are able to spar

MIN_EXP = 3  # The minimum number of months of experience
USAB_ACC = "Y"    # The existence of a USA Boxing Account


# Get the Boxer's experience.
exp = int(input('Enter the amount of boxing experience in months: '))

# Get the number of years on the current job.
acc = str(input('Do you have a USA Boxing Account? Y or N: ').strip().upper())

# Determine whether the customer qualifies.
if exp >= MIN_EXP and acc == USAB_ACC:
    print('You qualify for sparring! Good Luck!')
else:
    print(f'''You do not qualify sparring.\n
          The minimum qualifications are: \n 
          -  {MIN_EXP} Months of Experience \n
          -  A USA Boxing Account''')
