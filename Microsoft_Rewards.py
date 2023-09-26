# %%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# %%
robot = webdriver.Edge()
robot. get("https://www.bing.com/?scope=web&cc=BR&FORM=ANNNB1")

# %% [markdown]
# 1ª Pesquisa:

# %%
robot.implicitly_wait(10)
input_search = robot.find_element("xpath","/html/body/div[3]/div/div[3]/div[2]/form/div[1]/div/textarea")  # Find the search bar by its xpath
input_search.clear()  # Tell your robot to click the button.
input_search.send_keys("1")
input_search.send_keys(Keys.ENTER)

# %% [markdown]
# Rejeitar os cookies:

# %%
button = robot.find_element("id","bnp_btn_reject")
button.click()

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("2")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("3")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("4")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("5")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("6")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("7")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("8")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("9")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("10")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("11")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("12")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("13")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("14")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("15")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("16")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("17")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("18")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("19")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("20")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("21")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("22")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("23")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("24")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("25")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("26")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("27")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("28")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("29")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("30")
input_search.send_keys(Keys.ENTER)

# %%
input_search = robot.find_element("id","sb_form_q")
input_search.clear()

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("31")
input_search.send_keys(Keys.ENTER)

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("32")
input_search.send_keys(Keys.ENTER)

# %%
robot.implicitly_wait(3)
input_search = robot.find_element("id","sb_form_q")
input_search.clear()
input_search.send_keys("33")
input_search.send_keys(Keys.ENTER)
# %%
robot.quit()


