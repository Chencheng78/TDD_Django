from selenium import webdriver

wdriver = webdriver.Firefox()
wdriver.get('http://localhost:8000')
assert 'Django' in wdriver.title
