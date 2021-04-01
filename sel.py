from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import cred

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument('--headless')

browser = webdriver.Chrome('./chromedriver', chrome_options=options)

#browser.get("https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442")
browser.get(cred.link) #link to what you want

#checking if it is in stock
def Stock():
    inStock = False

    while inStock == False:
        try:
            addToCart = browser.find_element_by_class_name("btn-disabled")
            #item = browser.find_element_by_class_name("sku-title")
            print(f"Item not in stock")
            time.sleep(1)
            browser.refresh()

        except:
            addToCart = browser.find_element_by_class_name("btn-primary")
            print("we got it")
            addToCart.click()
            inStock = True

def Checkout():
    print("Starting Checkout")

    time.sleep(4)
    goCart = browser.find_element_by_class_name("go-to-cart-button")
    goCart.click()
    print("Going to cart")

    time.sleep(1)
    checkoutBtn = browser.find_element_by_class_name("checkout-buttons__checkout")
    checkoutBtn.click()
    print("Checking out")

    time.sleep(1.5)
    guest = browser.find_element_by_class_name("cia-guest-content__continue")
    guest.click()
    print("Checking out as guest")

    time.sleep(1)
    store = browser.find_element_by_class_name("ispu-card__switch")
    store.click()
    print("We will be shipping it")

    #info filling
    time.sleep(1)
    emailAddr = browser.find_element_by_id("user.emailAddress")
    phoneNbr = browser.find_element_by_id("user.phone")
    fname = browser.find_element_by_id("consolidatedAddresses.ui_address_5.firstName")
    lname = browser.find_element_by_id("consolidatedAddresses.ui_address_5.lastName")
    address1 = browser.find_element_by_id("consolidatedAddresses.ui_address_5.street")
    city = browser.find_element_by_id("consolidatedAddresses.ui_address_5.city")
    stateSelect = browser.find_element_by_id("consolidatedAddresses.ui_address_5.state")
    zipCode = browser.find_element_by_id("consolidatedAddresses.ui_address_5.zipcode")

    print("filling info")
    emailAddr.send_keys(cred.User.email)
    phoneNbr.send_keys(cred.User.phone)
    fname.send_keys(cred.User.fname)
    lname.send_keys(cred.User.lname)
    address1.send_keys(cred.User.addr)
    city.send_keys(cred.User.city)
    zipCode.send_keys(cred.User.zip)

    print("Selecting state")
    select = Select(browser.find_element_by_id("consolidatedAddresses.ui_address_5.state"))
    select.select_by_visible_text(cred.User.state)

    print("Payment info")
    pay = browser.find_element_by_class_name("btn-secondary")
    pay.click()

    #card input
    time.sleep(3)
    card = browser.find_element_by_id("optimized-cc-card-number")
    card.send_keys(cred.User.cardNum)
    print("Card Num inputted")

    print("Placing order now")
    placeOrder = browser.find_element_by_class_name("btn-primary")
    placeOrder.click()
    print("Order placed")


#TODO Add while checking loops, prt statements, and the works. QA and testing, maybe sign in beforehand for faster checkout? Optimiziong will
#have to come later. 
def run(): 
    Stock()
    Checkout()

run()