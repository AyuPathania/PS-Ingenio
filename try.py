from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random

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
random_text = ''.join(random.choices(special_chars, k=5)) + random.choice(emojis)
emoji_text = random_text.encode('unicode_escape').decode('utf-8')
print(f"Random text with special characters and emojis: {random_text}")

driver.find_element("name", "q").send_keys(random_text)
# Close the browser after 5 seconds
import time
time.sleep(5)
# driver.quit()

