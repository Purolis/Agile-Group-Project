from Deck import Deck
from Player import Player
from Dealer import Dealer
import os
import time


def main():
    decklist = Deck([])
    decklist.create_deck()
    decklist.shuffle_deck()

    p1 = Player([], 0, 1000)
    dealer = Dealer([], 0)
    players = [p1, dealer]
    player_wealth = p1.get_player_wealth()

    for x in range(2):
        for player in players:
            player.draw(decklist.draw_card())

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')

        p1_value = p1.count_hand()
        dealer_value = dealer.count_hand()

        if dealer_value != 21:
            if p1_value != 21 or p1_value == 21 and len(p1.get_hand()) > 2:
                print('Their Hand:')
                print(f'[{dealer.get_hand()[0].get_name()}]', end=' ')
                print(f'[]\n')
                display_player_cards(p1.get_hand(), p1_value)
                user_choice = choice()

                if user_choice.upper() == 'H':
                    p1.draw(decklist.draw_card())
                    p1_value = p1.count_hand()

                    if p1_value > 21:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)
                        print('\nYou busted, you lose!')
                        player_wealth -= 50
                        p1.set_player_wealth(player_wealth)
                        print('\nYou lost $50 Dollars! You now have $', player_wealth, 'dollars!\n')
                        print("You lost all your money! You lose at life!")

                        break

                else:
                    while dealer_value < 17:
                        time.sleep(1.5)
                        os.system('cls' if os.name == 'nt' else 'clear')

                        dealer.draw(decklist.draw_card())
                        dealer_value = dealer.count_hand()

                        os.system('cls' if os.name == 'nt' else 'clear')
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)

                    os.system('cls' if os.name == 'nt' else 'clear')
                    if dealer_value > 21:
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)
                        print('\nDealer busts, you win!')
                        player_wealth += 50
                        p1.set_player_wealth(player_wealth)

                        print('\nYou won $50 Dollars! You now have $', player_wealth, 'dollars!')
                        break

                    if p1_value > dealer_value:
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)
                        print(f'\n{p1_value} beats {dealer_value}, you win!')
                    elif p1_value == dealer_value:
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)
                        print(f'\n{p1_value} ties {dealer_value}, you push!')
                    else:
                        display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                        print()
                        display_player_cards(p1.get_hand(), p1_value)
                        print(f'\n{p1_value} loses to {dealer_value}, you lose!')
                        player_wealth -= 50
                        p1.set_player_wealth(player_wealth)
                        print('\nYou lost $50 Dollars! You now have $', player_wealth, 'dollars!\n')
                        print("You lost all your money! You lose at life!")

                    break
            else:
                display_player_cards(dealer.get_hand(), dealer_value, 'Their')
                print()
                display_player_cards(p1.get_hand(), p1_value)
                print('\nYou have Black Jack, you win!')
                player_wealth += 50
                p1.set_player_wealth(player_wealth)

                print('\nYou won $50 Dollars! You now have $', player_wealth, 'dollars!')
                break
        else:
            display_player_cards(dealer.get_hand(), dealer_value, 'Their')
            print()
            display_player_cards(p1.get_hand(), p1_value)
            print('\nThe dealer has Black Jack, you lose!')
            player_wealth -= 50
            p1.set_player_wealth(player_wealth)
            print('\nYou lost $50 Dollars! You now have $', player_wealth, 'dollars!\n')
            print("You lost all your money! You lose at life!")
            break


def display_player_cards(hand, player_value, player='Your'):
    print(f'{player} Hand:')
    for card in hand:
        print(f'[{card.get_name()}]', end=' ')
    print(f'[Value: {player_value}]')


def choice():
    user = input('\nHit or Stand | Type H or S: ')
    while True:
        try:
            if user.upper() == 'H' or user.upper() == 'S':
                break
            else:
                user = input('Not a valid input | Type H or S: ')
        except:
            pass

    return user


if __name__ == '__main__':
    main()
