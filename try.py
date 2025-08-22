from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
from selenium.webdriver.common.by import By
import time

# Setup Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open a website
driver.get("https://www.google.com")

# Maximize window
driver.maximize_window()

# Print title of the page
print("Page title:", driver.title)
special_chars = "!@#$%^&*()_+{}[]|:;<>?,./~`"
emojis = ["😝", "😜", "🤪", "🤨", "🔥", "❤️", "🚀", "😂", "🌟"]
random_text = ''.join(random.choices(special_chars, k=5)) + ''.join(random.choices(emojis, k=4))
# emoji_text = random_text.encode('unicode_escape').decode('utf-8')
print(f"Random text with special characters and emojis: {random_text}")

# driver.find_element("name", "q").send_keys(random_text)
driver.execute_script("document.getElementsByName('q')[0].value = arguments[0];", random_text)
time.sleep(5)  # Wait for the input to be set
# getValue=driver.get_text("document.getElementsByName('q')[0].value")
test =driver.find_element(By.XPATH, "//div[@class='YacQv']")
from_browser = test.text
print(f"Value from browser: {from_browser}")
# print(f"Value in search box: {getValue}")
# assert getValue == random_text, "Text in search box does not match the input!"
# Close the browser after 5 seconds
# import time
time.sleep(5)
# driver.quit()

