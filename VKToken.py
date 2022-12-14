# import requests
from pydantic import BaseModel
from urllib.parse import urlparse, urlencode
from my_token import TOKEN

class DisplayTypes(BaseModel):
    page: str = "page"
    popup: str = "popup"

class ScopeTypes(BaseModel):
    FRIENDS: str = "friends"
    WALL: str = "wall"

    def scope_list(self):
        return [self.FRIENDS, self.WALL]

    @property
    def scope(self):
        return ','.join(self.scope_list())

APP_ID = 51503617

class VKClient:
    URL_AUTH = "https://oauth.vk.com/authorize"
    URL_REDIRECT = "https://oauth.vk.com/blank.html"
    # SCOPE_LIST: list[str] = [FRIENDS, WALL]     --  Эти строки убраны из ввода класса ScopeTypes(BaseModel)
    # SCOPE: str = ','.join(SCOPE_LIST)           --
    PROTOCOL_V: str = "5.131"

    def __init__(self, token: str, user_id:str):
        self.token = token
        self.user_id = user_id

    def get_token(self):
        param = {
            "client_id": APP_ID,
            "redirect_url": self.URL_REDIRECT,
            "display": DisplayTypes().page,
            "scope": ScopeTypes().scope,
            "response_type": "token"
        }
        print("Нажать ==>", '?'.join((self.URL_AUTH, urlencode(param))))   # Строка запроса авторизации

client = VKClient(TOKEN, "1")
client.get_token()