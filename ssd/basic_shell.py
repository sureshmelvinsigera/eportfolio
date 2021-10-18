"""Basic python shell with 4 commands"""

import os

def shell():
    while True:
        command = input('$ ').lower()

        if command == 'list':
            for content in os.scandir('.'):
                if content.is_file():
                    print(content.name)

        if command == 'add':
            num_1 = input('First number:\n$ ')
            num_2 = input('Second number:\n$ ')
            answer = num_1 + num_2
            return print(answer)

        if command == 'help':
            print('HELP -- lists all available commands.')
            print('ADD --  adds two numbers together.')
            print('LIST -- list the content of the current directory.')
            print('EXIT -- exists the shell.')

        if command == 'exit':
            break


shell()
