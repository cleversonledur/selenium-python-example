from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#Acessar a url http://automationpractice.com
driver = browser = webdriver.Chrome(executable_path=r"./chromedriver")
driver.get("http://automationpractice.com")

#Realizar login (usuario: novoemailteste@gmail.com, senha: teste123)
loginButton = driver.find_element_by_class_name("login")
time.sleep(3)
loginButton.click()
time.sleep(3)

emailField = driver.find_element_by_id("email")
passwordField = driver.find_element_by_id("passwd")
loginButton = driver.find_element_by_id("SubmitLogin")

emailField.send_keys("novoemailteste@gmail.com")
passwordField.send_keys("teste123")
loginButton.click()

time.sleep(3)

#Acessar a categoria T-SHIRTS
driver.find_element_by_partial_link_text("T-SHIRTS").click()
time.sleep(3)

#Validar se esta na categoria
assert "T-SHIRTS" in driver.find_element_by_class_name("cat-name").text

#Acessar o primeiro/unico produto da listagem
product_list = driver.find_elements_by_class_name("product_list")

assert len(product_list) >= 1

_product_name_in_list = product_list[0].find_element_by_class_name("product-name").text
product_list[0].find_element_by_class_name("product_img_link").click()

time.sleep(3)

#Comparar o nome do produto da lista de produtos com a tela de detalhe de produto
assert _product_name_in_list in driver.find_element_by_tag_name("h1").text

#Adicionar o produto ao carrinho
driver.find_element_by_id("add_to_cart").find_element_by_tag_name("button").click()

time.sleep(3)

#Fazer o processo de checkout ate finalizar a venda
driver.find_element_by_partial_link_text("Proceed to checkout").click()
time.sleep(3)

driver.find_element_by_partial_link_text("Proceed to checkout").click()
time.sleep(5)

driver.find_element_by_name("processAddress").click()
time.sleep(5)

driver.find_element_by_id("cgv").click()
driver.find_element_by_name("processCarrier").click()
time.sleep(5)

driver.find_element_by_class_name("payment_module").click()
time.sleep(5)

driver.find_element_by_class_name("cart_navigation").find_element_by_tag_name("button").click()
time.sleep(5)

#Ao finalizar, validar a mensagem de sucesso da tela "Your order on My Store is complete."
assert "Your order on My Store is complete." in driver.find_element_by_class_name("cheque-indent").text

driver.close()