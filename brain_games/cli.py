import prompt

def welcome_user():

    print('Welcome to the Brain Games!')

    name = prompt.string('Hey there! Wait! What was your name again? ')

    print('Right.. ' + name + '...')

    return None

