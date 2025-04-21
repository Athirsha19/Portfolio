from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Replace with your correct local path
base_path = "file:///C:/Users/YourUsername/Documents/portfolio/"

# Home
driver.get("file:///C:/Users/HS/OneDrive/Desktop/Portfolio/index.html")
assert "Team Portfolio" in driver.title

# Go to Alice's page
driver.find_element(By.LINK_TEXT, "Athirsha").click()
assert "Athirsha" in driver.title
time.sleep(1)

# Back to Home
driver.back()

# Go to Bob's page
driver.find_element(By.LINK_TEXT, "Lefana Rose").click()
assert "Lefana Rose" in driver.title
time.sleep(1)

driver.back()

# Charlie
driver.find_element(By.LINK_TEXT, "Madhumitha").click()
assert "Madhumitha" in driver.title
time.sleep(1)

driver.back()

# Diana
driver.find_element(By.LINK_TEXT, "Susi Melinda").click()
assert "Susi Melinda" in driver.title
time.sleep(1)

driver.quit()
print("All pages tested successfully!")
