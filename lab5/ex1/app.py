import utils

if __name__ == '__main__':
    while True:
        inp = input('Input a number, or q to quit: ')
        if inp == 'q':
            break
        elif inp.isnumeric():
            num = int(inp)
            print('Next prime is', utils.process_item(num))
        else:
            print("I don't understand.")
r