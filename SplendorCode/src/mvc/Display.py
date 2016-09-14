from tkinter import *

from src.element.Card import Card
from src.element.ResourceType import ResourceType
from src.mvc.EventType import EventType
from src.mvc.GameBoard import GameBoard
from src.mvc.GameRules import GameRules
from src.player.AI import AI


class Display:
    window = None
    text = "test"
    game_rules = None
    game_board = None
    w = None
    h = None

    def __init__(self):
        self.window = Tk()
        self.create_image()

    def create_window(self):
        self.window.title(GameRules.game_name)
        self.w, self.h = 1900, 1000
        self.window.geometry("%dx%d+0+0" % (self.w, self.h))
        self.window.config(bg=None)

    def display_tiles(self):
        i = 1
        for tile in self.game_board.displayed_tiles:
            self.display_tile(i, tile)
            i += 1

    def display_tile(self, position, tile):
        canvas = Canvas(self.window, width=100, height=100,
                        background='#725202')
        canvas.create_image(13, 13, image=self.get_image_points(tile.points))
        i = 1
        for key in tile.gems_conditions:
            number = tile.gems_conditions[key]
            if number > 0:
                textcolor = "white"
                if ResourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    canvas.create_image(27, 40, image=self.get_image_rect_gem(
                        key))
                    txtBuy1 = canvas.create_text(25, 40, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    canvas.create_image(27, 80, image=self.get_image_rect_gem(
                        key))
                    txtBuy2 = canvas.create_text(25, 80, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    canvas.create_image(77, 80, image=self.get_image_rect_gem(
                        key))
                    txtBuy3 = canvas.create_text(75, 80, text=number,
                                                 fill=textcolor)
                    i = 0
        canvas.place(x=170 + 120 * (position - 1), y=100)
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_TILE,
                                         t=tile: self.game_rules.event(e, t))

    def display_cards(self):
        for lvl in range(1, int(self.game_rules.nb_lvl_card) + 1):
            i = 1
            for card in self.game_board.displayed_cards[lvl]:
                x = 170 + 120 * (i - 1)
                y = 490 - (130 * (lvl - 1))
                self.display_card(self.window, x, y, card,
                                  EventType.CLICK_DISPLAYED_CARD)
                i += 1

    def display_card(self, canvas, x, y, card, event):
        canvas = Canvas(canvas, width=100, height=120,
                        background=self.get_color(int(card.level)))
        canvas.create_image(50, 75, image=self.get_image_card_gem(
            card.income_gem))
        canvas.create_image(15, 20, image=self.get_image_points(card.points))
        i = 1
        for key in card.purchase_gems:
            number = card.purchase_gems[key]
            if number > 0:
                textcolor = "white"
                if ResourceType.get_color(key) == "white":
                    textcolor = "black"
                if i == 1:
                    canvas.create_image(25, 100,
                                        image=self.get_image_circle_gem(key))
                    txtBuy1 = canvas.create_text(25, 100, text=number,
                                                 fill=textcolor)
                    i = 2
                elif i == 2:
                    canvas.create_image(75, 100,
                                        image=self.get_image_circle_gem(key))
                    txtBuy2 = canvas.create_text(75, 100, text=number,
                                                 fill=textcolor)
                    i = 3
                elif i == 3:
                    canvas.create_image(25, 60,
                                        image=self.get_image_circle_gem(key))
                    txtBuy3 = canvas.create_text(25, 60, text=number,
                                                 fill=textcolor)
                    i = 4
                elif i == 4:
                    canvas.create_image(75, 60,
                                        image=self.get_image_circle_gem(key))
                    txtBuy4 = canvas.create_text(75, 60, text=number,
                                                 fill=textcolor)
                    i = 0
        canvas.place(x=x,
                     y=y)
        if event is not None:
            canvas.bind("<Button-1>",
                        lambda event, e=event,
                               c=card: self.game_rules.event(e, c))

    def display_stacks(self):
        for i in range(1, int(self.game_rules.nb_lvl_card) + 1):
            self.display_stack(i, self.game_board.is_deck_empty(i))

    def display_stack(self, level, empty):
        color = Display.get_color(level)
        if empty:
            color = "grey"
        canvas = Canvas(self.window, width=100, height=120, background=color)
        canvas.create_text(50, 50, text="PILE DE NIVEAU", fill="black")
        canvas.create_text(50, 70, text=level, fill="black")
        canvas.place(x=50, y=490 - (130 * (level - 1)))
        canvas.bind("<Button-1>", lambda event, e=EventType.CLICK_DECK_CARD,
                                         l=level: self.game_rules.event(e, l))

    def display_bank(self, bank):
        x = 70
        y = 650
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                self.display_gold(self.window, 70, 115, bank[token])
            else:
                self.display_gem(self.window, x, y, bank[token], token)
                x += 100

    def display_gold(self, canvas, x, y, nb):
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_image(40, 40, image=self.get_image_token_gem("Gold"))
        canvas.create_image(40, 40, image=self.get_image_points(nb))
        canvas.place(x=x, y=y)

    def display_gem(self, canvas, x, y, nb, gem):
        canvas = Canvas(canvas, width=80, height=80)
        canvas.create_image(40, 40, image=self.get_image_token_gem(gem))
        canvas.create_image(40, 40, image=self.get_image_points(nb))
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_TAKE_TOKEN_GAMEBOARD,
                           g=gem: self.game_rules.event(e, g))

    ###################### Display hand of player #################################

    def display_players(self):
        x = 1300
        y = 40
        for player in self.game_board.players:
            if type(player) == AI:
                self.display_player_ia(x, y, player)
                y += 280
            else:
                self.display_player_human(player)

    def display_player_human(self, player):
        color = "grey"
        if self.game_board.get_current_player() == player:
            color = "orange"
        canvas = Canvas(self.window, width=500, height=270,
                        highlightbackground=color)
        self.display_player_bank(canvas, 100, 10, player)
        canvas.create_text(50, 45, text=player.nickname, fill="black")
        canvas.create_text(50, 65, text=str(player.calcul_point_in_game()) +
                                        " / "
                                        "%d" %
                                        self.game_rules.nb_points_end,
                           fill="black")
        y = 130
        i = 1
        for card in player.reserved_cards:
            x = 10 + 120 * (i - 1)
            self.display_card(canvas, x, y, card, EventType.RESERVE_PURCHASE)
            i += 1
        self.display_player_tile(canvas, 370, 140, player)
        canvas.place(x=750, y=320)

    def display_player_ia(self, x, y, player):
        color = "grey"
        if self.game_board.get_current_player() == player:
            color = "orange"
        canvas = Canvas(self.window, width=500, height=270,
                        highlightbackground=color)
        canvas.place(x=x, y=y)
        self.display_player_bank(canvas, 100, 10, player)
        canvas.create_text(50, 45, text=player.nickname, fill="black")
        canvas.create_text(50, 65, text=str(player.calcul_point_in_game()) +
                                        " / "
                                        "%d" %
                                        self.game_rules.nb_points_end,
                           fill="black")
        y = 130
        i = 1
        for card in player.reserved_cards:
            x = 10 + 120 * (i - 1)
            self.display_card_ia(canvas, x, y, card.level)
            i += 1
        self.display_player_tile(canvas, 370, 140, player)

    def display_card_ia(self, canvas, x, y, level):
        color = Display.get_color(level)
        canvas = Canvas(canvas, width=100, height=120, background=color)
        canvas.place(x=x, y=y)

    def display_player_tile(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=100, height=100,
                        background='#725202')
        canvas.create_text(50, 50, text=len(player.owned_tiles), fill="black")
        canvas.place(x=x, y=y)

    def display_player_bank(self, canvas, x, y, player):
        canvas = Canvas(canvas, width=390, height=120)
        canvas.place(x=x, y=y)
        x = 0
        y = 60
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                self.display_player_gold(canvas, 320, 30, player.bank[token])
            else:
                self.display_player_gem(canvas, x, y, player.bank[token],
                                        token)
                x += 60
        x = 0
        y = 0
        for token in ResourceType.get_sorted_resources():
            if token == "Gold":
                pass
            else:
                self.display_player_income_card(canvas, x, y,
                                                player.get_card_income()[
                                                    token],
                                                token)
                x += 60

    def display_player_gold(self, canvas, x, y, nb):
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_oval(10, 10, 50, 50,
                           fill=ResourceType.get_color("Gold"))
        canvas.create_text(30, 30, text=nb, fill="black")
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                           g="Gold": self.game_rules.event(e, g))

    def display_player_gem(self, canvas, x, y, nb, gem):
        color = "white"
        if ResourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_oval(10, 10, 50, 50,
                           fill=ResourceType.get_color(gem))
        canvas.create_text(30, 30, text=nb, fill=color)
        canvas.place(x=x, y=y)
        canvas.bind("<Button-1>",
                    lambda event, e=EventType.CLICK_GIVE_BACK_PLAYER_TOKEN,
                           g=gem: self.game_rules.event(e, g))

    def display_player_income_card(self, canvas, x, y, nb, gem):
        color = "white"
        if ResourceType.get_color(gem) == "white":
            color = "black"
        canvas = Canvas(canvas, width=60, height=60)
        canvas.create_rectangle(10, 10, 50, 50,
                                fill=ResourceType.get_color(gem))
        canvas.create_text(30, 30, text=nb, fill=color)
        canvas.place(x=x, y=y)

    def popup_select_card_action(self, isreserved, ispurchase, card):
        popup = Toplevel(height=250, width=280)
        # popup.protocol("WM_DELETE_WINDOW", self.on_exit)
        Label(popup, text="Sélectionnez votre action :", height=1,
              width=30).place(x=40, y=10)
        self.display_card(popup, 90, 50, card, None)
        if isreserved:
            canvas = Canvas(popup, height=20,
                            width=60, background="grey")
            canvas.create_text(30, 10, text="Réserver", fill="black")
            canvas.bind("<Button-1>", lambda event,
                                             p=popup,
                                             e=EventType.POPUP_RESERVE,
                                             c=card:
            self.click_on_popup(p, e, c))
            canvas.place(x=60, y=200)
        if ispurchase:
            canvas = Canvas(popup, height=20,
                            width=60, background="grey")
            canvas.create_text(30, 10, text="Acheter", fill="black")
            canvas.bind("<Button-1>", lambda event,
                                             p=popup,
                                             e=EventType.POPUP_PURCHASE,
                                             c=card:
            self.click_on_popup(p, e, c))
            canvas.place(x=160, y=200)

    def click_on_popup(self, popup, event, objet):
        self.game_rules.event(event, objet)
        popup.destroy()

    def on_exit(self):
        """When you click to exit, this function is called"""
        pass

    def create_image(self):
        self.img0 = PhotoImage(file='../res/0.gif')
        self.img0 = self.img0.subsample(3, 3)
        self.img1 = PhotoImage(file='../res/1.gif')
        self.img1 = self.img1.subsample(3, 3)
        self.img2 = PhotoImage(file='../res/2.gif')
        self.img2 = self.img2.subsample(3, 3)
        self.img3 = PhotoImage(file='../res/3.gif')
        self.img3 = self.img3.subsample(3, 3)
        self.img4 = PhotoImage(file='../res/4.gif')
        self.img4 = self.img4.subsample(3, 3)
        self.img5 = PhotoImage(file='../res/5.gif')
        self.img5 = self.img5.subsample(3, 3)
        self.img6 = PhotoImage(file='../res/6.gif')
        self.img6 = self.img6.subsample(3, 3)
        self.img7 = PhotoImage(file='../res/7.gif')
        self.img7 = self.img7.subsample(3, 3)

        self.img_card_D = PhotoImage(file='../res/card_diamant.gif')
        self.img_card_D = self.img_card_D.subsample(5, 5)
        self.img_card_E = PhotoImage(file='../res/card_emeraude.gif')
        self.img_card_E = self.img_card_E.subsample(5, 5)
        self.img_card_O = PhotoImage(file='../res/card_onyx.gif')
        self.img_card_O = self.img_card_O.subsample(5, 5)
        self.img_card_R = PhotoImage(file='../res/card_rubis.gif')
        self.img_card_R = self.img_card_R.subsample(5, 5)
        self.img_card_S = PhotoImage(file='../res/card_saphir.gif')
        self.img_card_S = self.img_card_S.subsample(5, 5)

        self.img_circle_D = PhotoImage(file='../res/white_circle.gif')
        self.img_circle_D = self.img_circle_D.subsample(2, 2)
        self.img_circle_E = PhotoImage(file='../res/green_circle.gif')
        self.img_circle_E = self.img_circle_E.subsample(2, 2)
        self.img_circle_O = PhotoImage(file='../res/black_circle.gif')
        self.img_circle_O = self.img_circle_O.subsample(2, 2)
        self.img_circle_R = PhotoImage(file='../res/red_circle.gif')
        self.img_circle_R = self.img_circle_R.subsample(2, 2)
        self.img_circle_S = PhotoImage(file='../res/blue_circle.gif')
        self.img_circle_S = self.img_circle_S.subsample(2, 2)

        self.img_rect_D = PhotoImage(file='../res/white_rect.gif')
        self.img_rect_D = self.img_rect_D.subsample(2, 2)
        self.img_rect_E = PhotoImage(file='../res/green_rect.gif')
        self.img_rect_E = self.img_rect_E.subsample(2, 2)
        self.img_rect_O = PhotoImage(file='../res/black_rect.gif')
        self.img_rect_O = self.img_rect_O.subsample(2, 2)
        self.img_rect_R = PhotoImage(file='../res/red_rect.gif')
        self.img_rect_R = self.img_rect_R.subsample(2, 2)
        self.img_rect_S = PhotoImage(file='../res/blue_rect.gif')
        self.img_rect_S = self.img_rect_S.subsample(2, 2)

        self.img_token_D = PhotoImage(file='../res/token_diamant.gif')
        self.img_token_D = self.img_token_D.subsample(3, 3)
        self.img_token_E = PhotoImage(file='../res/token_emeraude.gif')
        self.img_token_E = self.img_token_E.subsample(3, 3)
        self.img_token_R = PhotoImage(file='../res/token_rubis.gif')
        self.img_token_R = self.img_token_R.subsample(3, 3)
        self.img_token_S = PhotoImage(file='../res/token_saphir.gif')
        self.img_token_S = self.img_token_S.subsample(3, 3)
        self.img_token_O = PhotoImage(file='../res/token_onyx.gif')
        self.img_token_O = self.img_token_O.subsample(3, 3)
        self.img_token_G = PhotoImage(file='../res/token_gold.gif')
        self.img_token_G = self.img_token_G.subsample(3, 3)

    def get_image_points(self, points):
        if points == 0:
            return self.img0
        elif points == 1:
            return self.img1
        elif points == 2:
            return self.img2
        elif points == 3:
            return self.img3
        elif points == 4:
            return self.img4
        elif points == 5:
            return self.img5
        elif points == 6:
            return self.img6
        elif points == 7:
            return self.img7

    def get_image_card_gem(self, gem):
        if gem == "Diamond":
            return self.img_card_D
        elif gem == "Emerald":
            return self.img_card_E
        elif gem == "Sapphire":
            return self.img_card_S
        elif gem == "Onyx":
            return self.img_card_O
        elif gem == "Ruby":
            return self.img_card_R

    def get_image_circle_gem(self, gem):
        if gem == "Diamond":
            return self.img_circle_D
        elif gem == "Emerald":
            return self.img_circle_E
        elif gem == "Sapphire":
            return self.img_circle_S
        elif gem == "Onyx":
            return self.img_circle_O
        elif gem == "Ruby":
            return self.img_circle_R

    def get_image_rect_gem(self, gem):
        if gem == "Diamond":
            return self.img_rect_D
        elif gem == "Emerald":
            return self.img_rect_E
        elif gem == "Sapphire":
            return self.img_rect_S
        elif gem == "Onyx":
            return self.img_rect_O
        elif gem == "Ruby":
            return self.img_rect_R

    def get_image_token_gem(self, gem):
        if gem == "Diamond":
            return self.img_token_D
        elif gem == "Emerald":
            return self.img_token_E
        elif gem == "Sapphire":
            return self.img_token_S
        elif gem == "Onyx":
            return self.img_token_O
        elif gem == "Ruby":
            return self.img_token_R
        elif gem == "Gold":
            return self.img_token_G

    @staticmethod
    def get_color(level):
        if level == 1:
            color = '#0483f9'
        if level == 2:
            color = '#05e002'
        if level == 3:
            color = '#ffac07'
        return color

    def refresh(self):
        self.display_bank(self.game_board.bank)
        self.display_stacks()
        self.display_cards()
        self.display_tiles()
        self.display_players()


display = Display()
display.game_board = GameBoard(display, GameRules())
display.game_rules = display.game_board.game_rules
display.game_rules.game_board = display.game_board
display.game_rules.display = display
display.create_window()
display.refresh()
display.window.mainloop()
