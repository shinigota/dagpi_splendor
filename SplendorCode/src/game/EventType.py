from enum import Enum


class EventType(Enum):
    START = 1
    EXIT = 2
    SAVE_GAME_PARAMETERS = 3
    CLICK_CARD = 4
    CLICK_TOKEN = 5
    CLICK_TILE = 6
    POPUP_PURCHASE = 7
    POPUP_RESERVE = 8
    CANCEL_ACTION = 9
    VALIDATE_ACTION = 10
