from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time
import login_creds as lc

gsc_url = 'gallghergmc.com' #input('what is the url associated with GSC? \n')
a_name = 'Gallagher GMC' #input('What is the account name?\n')
login_email = lc.login_email
login_pass = lc.login_pass
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
'''
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

#Enter Search in Search Bar
browser.find_element_by_css_selector('input[aria-label="Search Drive"]').send_keys(demo_data_sheet)
time.sleep(3)

#Generic Enter Command
ActionChains(browser).send_keys(Keys.ENTER).perform()
time.sleep(3)

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

'''

########################### OPEN DEMO DATA STUDIO ##############################
#browser.switch_to.window(browser.window_handles[1])

browser.get('https://datastudio.google.com/reporting/1-6lVWLkE5ftuErzs3Si8DSQoMv8egGz_/page/1teX')
time.sleep(5)

#Hitting the 'Edit' button
browser.find_element_by_xpath('//*[@id="reporting-app-header"]/md-toolbar/div/div[3]/div[10]/button/md-icon').click()
time.sleep(3)

#Could not seem to figure out how to trigger the drop down menu for Data Studio Cloning, going to base off location of edit button.

#Set Up Anchor Point for Positional Movement
view_button = browser.find_element_by_xpath('//*[@id="reporting-app-header"]/md-toolbar/div/div[3]/div[9]/button')

#Add Shortcut for Action Chain
ac = ActionChains(browser)

#Click File Dropdown
ac.move_to_element(view_button).move_by_offset(-980, 20).click().perform()


#Click 'Make a copy...'
ac.move_to_element(view_button).move_by_offset(-965, 203).click().perform()
time.sleep(3)


#Switch to popup box
#browser.switch_to.alert

#Click the [1] Data Source "Dealer Leads"
browser.find_element_by_xpath('(//*[@class="md-select-value"]/span[1]//*[@class="md-text ng-binding"])[1]').click()
time.sleep(2)

#Seach for [1] Data Source of a_name ***REPLACE HARD VALUE HERE***
browser.find_element_by_xpath('//*[@id="input_219"]').send_keys('Gotcha')
time.sleep(2)

browser.find_element_by_xpath('//*[@id="input_219"]').clear()
time.sleep(2)

#Seach for [1] Data Source of a_name ***REPLACE HARD VALUE HERE***
browser.find_element_by_xpath('//*[@id="input_219"]').send_keys('Gallagher - Dealer Leads')
time.sleep(2)

#Generic Enter Command
#ActionChains(browser).send_keys(Keys.ENTER).perform()
#time.sleep(4)

browser.find_element_by_xpath('(//*[@class="ng-scope md-data-studio-theme md-ink-ripple"])[1]').click()

'''
#Click close
#browser.find_element_by_xpath('/html/body/div[7]/md-dialog/md-dialog-actions/button[1]').click()

#Set Up New Anchor point to the html position (0,0)
html_position = browser.find_element_by_xpath('/html')
anchor_location = html_position.location
print(anchor_location)

#Click the 'Dealer Leads' source
ac.move_to_element(html_position).move_by_offset(727, 389).click().perform()
time.sleep(2)

#Click 'Create New Data Source'
#ac.move_to_element(close_button).move_by_offset(0, -90).click().perform()
time.sleep(5)
'''
