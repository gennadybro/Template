from Diplom import VKconnect
import config
import logging
import vk_api
import datetime


def run():
  #  try:
        logging.basicConfig(filename="basic.log", level=logging.INFO)
        log = logging.getLogger(' (' + str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + ') '))
        log.info('')
        log.info('\t === Начало работы === \t')
       # try:
        token = config.AUTH_PARAMS['TOKEN'] if config.AUTH_PARAMS['TOKEN'] else input("Введите токен")
        id = config.AUTH_PARAMS['ID'] if config.AUTH_PARAMS['ID'] else input("Введие ID:")
        vktinder_vk = VKconnect.VKTinder(age_from=config.AUTH_PARAMS['AGE_FROM'], age_to=config.AUTH_PARAMS['AGE_TO'], id = id, token = token)
        vktinder_vk.authorize_by_token()
           
        # except vk_api.exceptions.ApiError:
        log.warning('Не удалось авторизоваться в ВК!')
        raise vk_api.exceptions.ApiError
         
       # vktinder_vk()
       # my_account = vkinder_vk.get_my_profile()
        #log.info('Спарсили свой аккаунт ?????')
         
    #except: