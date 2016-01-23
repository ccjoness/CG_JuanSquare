from BlackJackModel import Player, Deck, Card
from BlackJackView import View

class Game():
    def __init__(self):
#TODO Delete this evan list it should be a blank list
        self.current_player = 0
        self.player_object_list = []
        self.deck = Deck(6) # create the deck object
        self.deck.create_deck() # call method to populate deck with cards
        self.view = View()

    def get_players(self):
        num_players = self.view.number_of_players_prompt()
        name_players = self.view.names_of_players(num_players)
        for name in name_players:
            self.player_object_list.append(Player(name))

    def spawn_dealer(self):
        dealer = Player('Dealer')
        dealer.dealer = True
        self.player_object_list.append(dealer)

    def set_player_hand(self, player, cards):
        '''
        tests function to set a player's hand
        player: is a player object
        cards: a list of card objects
        '''
        for card in cards:
            player.current_hand.append(card)

    def set_hand_val(self, player):
        pass

    def hit_deal(self):
        self.player_object_list[self.current_player].current_hand.append(self.deck.cards.pop())


    def player_turn(self):
        """ next_turn method. Gives each player their turns. selects player turns by going through playerobjectlist."""
        if self.current_player < len(self.player_object_list)-1:
            self.current_player += 1
        else:
            self.current_player = 0

    def check_bust(self):
        player = self.player_object_list[self.current_player]
        if player.current_hand_value > 21:
            player.busted = True

    def dealer_decision(self):
        dealer = self.player_object_list[-1]
        if dealer.current_hand_value <= 16:
            return True
        if dealer.current_hand_value > 16:
            return False

    def check_deck_empty(self):
        if len(self.deck.cards) < 101:
            self.deck.cards = []
            self.deck.create_deck()
            self.deck.shuffle()

    def check_end_round(self):
        if self.player_object_list[self.current_player].dealer == True:
            return True
        else:
            return False

    def deal_cards(self):
        for player in self.player_object_list:
            for i in range(2):
                player.current_hand.append(self.deck.cards[0])
                self.deck.cards.pop(0)
                if player == self.player_object_list[-1]:
                    showing_card = player.current_hand[0]
                    showing_card.showing = False
