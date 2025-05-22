
def madlib(adj, animal, verb, plural_noun, emotion, weather, exclamation):
    """Madlib with 7 variables using a function"""
    story = (f'''
    Mad Lib Story:

    Last weekend, I went on a trip to the {adj} mountains. 
    While hiking, I spotted a {animal} quietly 
    {verb} in the bushes. The trail was full of 
    {plural_noun}, which made walking a bit tricky.
    I felt so {emotion} being surrounded by nature and breathing in 
    the crisp {weather} air. At the top of the mountain, I 
    shouted, "{exclamation}" because the view was absolutely breathtaking.
    ''')
    return(story)


def get_input():
    """Function to get variables for the madlib"""
    adj = input('Please enter an adjective: ')
    animal = input('Please enter an animal: ')
    verb = input('Please enter an verb ending with -ing: ')
    plural_noun = input('Please enter an plural noun: ')
    emotion = input('Please enter an emotion: ')
    weather = input('Please enter an type of weather: ')
    exclamation = input('Please enter an exclamation: ')
    return adj, animal, verb, plural_noun, emotion, weather, exclamation

inputs = get_input()

print(madlib(*inputs))
