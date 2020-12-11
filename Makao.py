from Game import Game

if __name__ == "__main__":
    value_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    color_list = ['♣', '♦', '♥', '♠']
    play = Game(value_list, color_list, N_Players = 2, N_Decks = 1)
