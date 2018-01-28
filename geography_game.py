import random



def main():
    print '***GEOGRAPHY GAME***'
    print 'Hi! This is a game in which you must guess the capitals of selected countries.'
    print('\n')
    country_capital_dict = {'Slovenia': 'Ljubljana',
                            'Croatia': 'Zagreb',
                            'Serbia': 'Belgrade',
                            'Bosna and Hercegovina': 'Sarajevo',
                            'Macedonia': 'Skopje',
                            'Montenegro': 'Podgorica'}

    while True:
        random_num = random.randint(0, 5)
        selected_country = country_capital_dict.keys()[random_num]
        guess = raw_input('What is the capital of %s: ' % selected_country)
        check_guess(guess, selected_country, country_capital_dict)
        again= raw_input('Would you like to continue this game? (y/n)')
        if again != 'y' and again != 'yes':
            break

    print('\n')
    print 'Thank you for trying our game'
    print '_____________________________'

def check_guess(user_guess, country, cc_dict):
    capital = cc_dict[country]

    if user_guess == capital:
        print 'Correct! The capital of %s is indeed %s.' % (country, capital)
        return True
    else:
        print 'Sorry, you are wrong. The capital of %s is %s.' % (country, capital)
        return False

if __name__ == '__main__':
    main()


