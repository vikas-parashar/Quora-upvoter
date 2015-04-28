from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium.webdriver.common.keys import Keys
import os
import getpass

your_email = raw_input("Enter your Email for login on quora: ")
your_pass  = getpass.getpass()
url 	   = raw_input("Enter the user's profile link(ex: https://www.quora.com/username):")
chromedriver = "/home/vicodin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)
browser.set_window_size(1120, 550)
browser.get('http://www.quora.com')
time.sleep(3)
body = browser.find_element_by_tag_name("body")
form = browser.find_element_by_class_name('regular_login')
user = form.find_element_by_name('email').send_keys(your_email)
password = form.find_element_by_name('password').send_keys(your_pass, Keys.RETURN)

time.sleep(5)

browser.get(url+'/answers')
# print url+'/answers'
print "opening answres.. "
time.sleep(3)
body = browser.find_element_by_tag_name("body")
loaded_answers_length = len(browser.find_elements_by_class_name("pagedlist_item"))
# Load all the answers first.
count = 0
print "Loading all answers..."
while True:
	body.send_keys(Keys.END)
	time.sleep(3)
	loaded_answers_length_new = len(browser.find_elements_by_class_name("pagedlist_item"))
	if loaded_answers_length == loaded_answers_length_new:
		count += 1
		if count == 3:
			break
	else:
		loaded_answers_length = loaded_answers_length_new
time.sleep(3)
print "All answers loaded "
upvote = browser.find_elements_by_class_name('primary_item')


for link in upvote:
	upvote_btn = link.find_element_by_tag_name('a')
	webdriver.ActionChains(browser).move_to_element(upvote_btn).click(upvote_btn).perform()
	time.sleep(1)

print "we are done!!"



browser.close()