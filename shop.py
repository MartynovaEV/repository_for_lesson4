'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
HTML5_Forms_btn = driver.find_element_by_tag_name("[title='Mastering HTML5 Forms']")
HTML5_Forms_btn.click()
Logout = WebDriverWait(driver, 25).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary h1"), "HTML5 Forms"))'''




'''import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
HTML_btn = driver.find_element_by_css_selector(".product-categories>:nth-child(2)>a")
HTML_btn.click()
items_count = driver.find_elements_by_css_selector("ul.products>li")
if len(items_count) == 3:
    print("Отображается 3 товара")
else:
    print("Ошибка. Отображается: " + str(len(items_count)))'''




'''import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
DefaultSort = driver.find_element_by_tag_name('[name="orderby"]')
DefaultSort_check = DefaultSort.get_attribute('value')
if DefaultSort_check == 'menu_order':
    print('Выбран вариант сортировки Default sorting')
else:
    print('Выбран другой вариант сортировки:' + DefaultSort_check)
driver.find_element_by_css_selector("select[name='orderby']").click()
driver.find_element_by_css_selector("option:nth-child(6)").click()
High_to_low = driver.find_element_by_tag_name('[name="orderby"]')
High_to_low_check = High_to_low.get_attribute('value')
if High_to_low_check == 'price-desc':
    print('Выбран вариант сортировки Sort by price: high to low')
else:
    print('Выбран другой вариант сортировки:' + High_to_low_check)'''




'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
AndroidBook = driver.find_element_by_css_selector(".post-169 h3")
AndroidBook.click()
driver.implicitly_wait(20)
Book_old_price = driver.find_element_by_css_selector(".price > del > span")
Book_old_price_text = Book_old_price.text
Book_new_price = driver.find_element_by_css_selector(".price > ins > span")
Book_new_price_text = Book_new_price.text
assert Book_old_price_text == "₹600.00"
assert Book_new_price_text == "₹450.00"
Cover = WebDriverWait(driver, 25).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
Cover.click()
Cover_close = WebDriverWait(driver, 25).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
Cover_close.click()'''




'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
MyAcc_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(2)")
MyAcc_btn.click()
#Login
Email = driver.find_element_by_id("username")
Email.send_keys("martynova.ev1991@gmail.com")
Password = driver.find_element_by_id("password")
Password.send_keys("martynovaev1991@")
Login = driver.find_element_by_tag_name("[name='login']")
Login.click()
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5_btn = driver.find_element_by_css_selector(".products>:NTH-CHILD(4)>[data-product_id='182']")
HTML5_btn.click()
time.sleep(5)
Quantity = driver.find_element_by_css_selector('.wpmenucart-contents>span.cartcontents')
Quantity_text = Quantity.text
Amount = driver.find_element_by_css_selector('.wpmenucart-contents > span.amount')
Amount_text = Amount.text
assert Quantity_text == "1 Item"
assert Amount_text == "₹180.00"
Basket_btn = driver.find_element_by_id("wpmenucartli")
Basket_btn.click()
time.sleep(5)
Subtotal = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[data-title='Price'] .woocommerce-Price-amount"), "₹180.00"))
Total = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total .woocommerce-Price-amount"), "₹183.60"))'''




'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5_book_btn = driver.find_element_by_css_selector(".products>:NTH-CHILD(4)>[data-product_id='182']")
HTML5_book_btn.click()
time.sleep(5)
driver.execute_script("window.scrollBy(0, 200);")
JS_Data_book_btn = driver.find_element_by_css_selector(".products>:NTH-CHILD(5)>[data-product_id='180']")
JS_Data_book_btn.click()
Basket_btn = driver.find_element_by_id("wpmenucartli")
Basket_btn.click()
time.sleep(3)
HTML5_book_remove = driver.find_element_by_css_selector("td.product-remove>[data-product_id='182']")
HTML5_book_remove.click()
time.sleep(3)
Undo = driver.find_element_by_css_selector(".woocommerce-message > a")
Undo.click()
Clear = driver.find_element_by_css_selector("#page-34 .shop_table>:nth-child(2)>:nth-child(1)>:nth-child(5) input")
Clear.clear()
time.sleep(2)
Paste = driver.find_element_by_css_selector("#page-34 .shop_table>:nth-child(2)>:nth-child(1)>:nth-child(5) input")
Paste.send_keys("3")
time.sleep(2)
Update_basket = driver.find_element_by_css_selector(".actions>input:nth-child(2)")
Update_basket.click()
time.sleep(2)
#Value = driver.find_element_by_css_selector("#page-34 .shop_table>:nth-child(2)>:nth-child(1)>:nth-child(5) .input-text")
#Value = driver.find_element_by_css_selector("#page-34 .shop_table>:nth-child(2)>:nth-child(1)>:nth-child(5) [value='3']")
#Value = driver.find_element_by_css_selector(".quantity [value='3']")
#Value = driver.find_element_by_css_selector("#page-34 .shop_table>:nth-child(2)>:nth-child(1)>:nth-child(5)")
#Value = driver.find_element_by_tag_name("[value='3']")
#Value_get_text = Value.text
Value = driver.find_element_by_css_selector(".quantity [value='3']")
Value_check = Value.get_attribute("value")
if Value_check == "3":
    print("Value для JS Data Structures and Algorithm = 3")
else:
    print("Ошибка")
time.sleep(3)
Apply_Coupon = driver.find_element_by_css_selector(".coupon>:nth-child(3)")
Apply_Coupon.click()
alert = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error"), "Please enter a coupon code"))'''




'''import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://practice.automationtesting.in/")
driver.implicitly_wait(20)
Shop_btn = driver.find_element_by_css_selector("[itemscope='itemscope']>.main-nav>:nth-child(1)")
Shop_btn.click()
driver.execute_script("window.scrollBy(0, 300);")
HTML5_book_btn = driver.find_element_by_css_selector(".products>:NTH-CHILD(4)>[data-product_id='182']")
HTML5_book_btn.click()
time.sleep(3)
Basket_btn = driver.find_element_by_id("wpmenucartli")
Basket_btn.click()
Proceed_to_checkout_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout>a")))
Proceed_to_checkout_btn.click()
First_name = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
First_name.send_keys("Evgenia")
Last_name = driver.find_element_by_id("billing_last_name")
Last_name.send_keys("Martynova")
time.sleep(1)
Phone = driver.find_element_by_id("billing_phone")
Phone.send_keys("89001112233")
time.sleep(1)
Email = driver.find_element_by_id("billing_email")
Email.send_keys("martynova.ev1991@gmail.com")
time.sleep(2)
Country = driver.find_element_by_css_selector(".select2-arrow>b")
Country.click()
time.sleep(1)
Country_search = driver.find_element_by_id("s2id_autogen1_search")
Country_search.send_keys("Russia")
time.sleep(1)
Country_choose = driver.find_element_by_css_selector(".select2-match")
Country_choose.click()
driver.execute_script("window.scrollBy(0, 400);")
Street = driver.find_element_by_tag_name("[placeholder='Street address']")
Street.send_keys("Nevskiy av. 111")
City = driver.find_element_by_tag_name("[autocomplete='address-level2']")
City.send_keys("Saint-Petersburg")
State = driver.find_element_by_tag_name("[name='billing_state']")
State.send_keys("Saint-Petersburg")
Zip = driver.find_element_by_tag_name("[name='billing_postcode']")
Zip.send_keys("111999")
driver.execute_script("window.scrollBy(0, 400);")
time.sleep(2)
Check_Payments = driver.find_element_by_id("payment_method_cheque")
Check_Payments.click()
Place_order = driver.find_element_by_id("place_order")
Place_order.click()
Order_received = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce>:nth-child(1)'), 'Thank you. Your order has been received.'))
Payment_Method = WebDriverWait(driver, 20).until(
EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-details>.method>strong'), 'Check Payments'))'''
