from behave import given, when, then
from selenium.webdriver.common.by import By
import time

# Variável com a URL do site que iremos interagir.
base_url = 'https://qualityprovider.dguardcloud.com.br/authentication/login'
user_element = '/html/body/app-root/block-ui/app-blank/nb-layout/div/div/div/div/div/nb-layout-column/app-login/nb-card/nb-card-body/div/form/div[1]/input'
# password_element = '/html/body/app-root/block-ui/app-blank/nb-layout/div/div/div/div/div/nb-layout-column/app-login/nb-card/nb-card-body/div/form/div[2]/input'
confirm_element = '/html/body/app-root/block-ui/app-blank/nb-layout/div/div/div/div/div/nb-layout-column/app-login/nb-card/nb-card-body/div/form/button'
layout9_element = '/html/body/app-root/block-ui/app-full/nb-layout/div[1]/div/div/div/div/nb-layout-column/nb-card/app-camera-panel/div[1]/div[1]/button[4]'
cameraMap_element = '/html/body/app-root/block-ui/app-full/nb-layout/div[1]/div/div/nb-sidebar/div/div/nb-menu/ul/li[1]/ul/li[2]/a'
cameraPanel_element = '/html/body/app-root/block-ui/app-full/nb-layout/div[1]/div/div/nb-sidebar/div/div/nb-menu/ul/li[1]/ul/li[1]/a'
comunity_element = '/html/body/app-root/block-ui/app-full/nb-layout/div/div/div/nb-sidebar/div/div/nb-menu/ul/li[1]/ul/li[4]/a'

user = 'tryout@seventh.com.br'
password = 'Seventh@23'


@given(u'acesso o D-Guard Cloud')
def step_impl(context):
    context.web.get(base_url)
    context.web.set_window_size(1280,1024)

@when(u'faço o meu login')
def fazer_login(context):
    time.sleep(3)
    context.user_element = context.web.find_element(By.XPATH, user_element)
    context.user_element.click()
    context.user_element.send_keys(user)

    time.sleep(1)
    password_element = context.web.find_element(By.XPATH, '/html/body/app-root/block-ui/app-blank/nb-layout/div/div/div/div/div/nb-layout-column/app-login/nb-card/nb-card-body/div/form/div[2]/input')
    password_element.click()
    password_element.send_keys(password)

    context.confirm = context.web.find_element(By.XPATH, confirm_element)
    context.confirm.click()

    time.sleep(5)


@when(u'começo a gerar várias auditorias de acesso as câmeras')
def poluir_auditoria(context):
    for i in range (5):
        time.sleep(4)
        context.layout9_element = context.web.find_element(By.XPATH, layout9_element)
        context.layout9_element.click()
        time.sleep(3)
        context.cameraMap_element = context.web.find_element(By.XPATH, cameraMap_element)
        context.cameraMap_element.click()
        time.sleep(3)
        context.cameraPanel_element = context.web.find_element(By.XPATH, cameraPanel_element)
        context.cameraPanel_element.click()
        # context.comunity_element = context.web.find_element(By.XPATH, comunity_element)  #se for pra visualizar câmeras da comunidade é só descomentar esses 2 trechos e comentar o de cima.
        # context.comunity_element.click()        



@then(u'eu polui a auditoria')
def step_impl(context):
    time.sleep(5)
