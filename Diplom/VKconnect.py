import vk_api

class VKTinder:
    def __init__(self, id, token, age_from=18, age_to=18, **kwargs):
        self.token = token
        self.id = id
        self.sex = None
        self.city = None
        self.VK = None
        self.age_from = age_from
        self.age_to = age_to
        self.kwargs = kwargs
        
    def authorize_by_token(self):
        vk_session = vk_api.VkApi(token=self.token)
        vk = vk_session.get_api()
        self.VK = vk