from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


gsc_url = 'gallghergmc.com' #input('what is the url associated with GSC? \n')
a_name = 'Gallagher GMC' #input('What is the account name?\n')
login_email = 'google@mydealerworld.com'
login_pass = 'Dealer531World'
demo_studio_folder = '_Demo Studio'
demo_studio_title = 'Demo Data Studio 07/2019'
demo_data_sheet = 'Demo Data Sheet 07/2019'

browser = webdriver.Chrome('/Users/garrettscott/chromedriver')

browser.get('https://accounts.google.com/signin/v2/identifier?service=wise&passive=1209600&continue=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F0BylNy6qIbU5aRW11dHBmNkpua2c&followup=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F0BylNy6qIbU5aRW11dHBmNkpua2c&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
time.sleep(2)


user_email = browser.find_element_by_id('identifierId')
user_email.send_keys(login_email)

email_next_button = browser.find_element_by_id('identifierNext')
email_next_button.click()
time.sleep(2)

password = browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
print(password.text)
#variable did not work in send_keys
password.send_keys(login_pass)
time.sleep(2)

password_next_button = browser.find_element_by_id('passwordNext')
password_next_button.click()
time.sleep(5)

#New Folder Window
ActionChains(browser).key_down(Keys.SHIFT).send_keys('f').key_up(Keys.SHIFT).perform()
time.sleep(5)

#Generic Type Command
ActionChains(browser).send_keys(a_name).perform()
time.sleep(2)

#Generic Enter Commond
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(4)

#Search Client Folder
browser.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]').send_keys(a_name)

#Search Client Folder (enter)
browser.find_element_by_xpath('//*[@id="gs_lc50"]/input[1]').send_keys(Keys.ENTER)
time.sleep(2)

#Click specific folder
browser.find_element_by_css_selector('div[aria-label="'+a_name+' Shared Google Drive Folder"]').click()

#Generic Enter Command
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(5)

#Make New Folder
ActionChains(browser).key_down(Keys.SHIFT).send_keys('f').key_up(Keys.SHIFT).perform()
time.sleep(2)

#Generic Type Command
ActionChains(browser).send_keys('Connectors').perform()
time.sleep(2)

#Generic Enter Commond
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(4)

'''
#Click Search Bar
browser.find_element_by_css_selector('div[aria-label="Search Drive"]').click()
time.sleep(1)
'''

#Enter Search in Search Bar
browser.find_element_by_css_selector('input[aria-label="Search Drive"]').send_keys(demo_data_sheet)
time.sleep(1)

#Generic Enter Command
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(1)

#Click specific file
browser.find_element_by_css_selector('div[aria-label="'+demo_data_sheet+'"]').click()

#Generic Enter Command
ActionChains(browser).send_keys(Keys.ENTER).perform()

########################### Google Sheet Open ##################################

print('Make a copy of this and update the SuperMetics Parameters')
print()
user_status = input('Are you ready to automate this bitty? \n')
print()
print('Fasten your seatbelts!')

########################### OPEN DEMO DATA STUDIO ##############################
browser.switch_to.window(browser.window_handles[1])

browser.get('https://datastudio.google.com/reporting/1-6lVWLkE5ftuErzs3Si8DSQoMv8egGz_/page/1teX')
time.sleep(15)

#browser.switch_to.window(browser.window_handles[0])

browser.find_element_by_xpath('//*[@id="reporting-app-header"]/md-toolbar/div/div[3]/div[10]/button/md-icon').click()
time.sleep(4)

try:
    browser.find_element_by_css_selector('div[flex class="ng-binding flex"]').click()
    print('1pass')
except:
    print('oh jeez')
    pass

try:
    browser.find_element_by_class('md-button md-data-studio-theme md-ink-ripple').click()
    print('2pass')
except:
    print('double jeez')
    pass


elem = find_element_by_selector(selector)
ac = ActionChains(browser)
ac.move_to_element(elem).move_by_offset(x_off, y_off).click().perform()
