"""
1. In this code we are scraping naukri.com for python developer jobs
#Search for "Python Development"

2. Extract job title, company, location
3. Click into a job and get description"""


from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.naukri.com/")
wait = WebDriverWait(driver, 10)

try:
    enter_skills = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".suggestor-input")))
    enter_skills.send_keys("pyt")

    skills_suggestions = wait.until(
        EC.presence_of_all_elements_located(
            (By.XPATH, "//ul/li[@class='tuple-wrap ']"
             )
        )
    )

    for suggestion in skills_suggestions:
        if "Python Testing" in suggestion.text:
            suggestion.click()
            break

    click_exp = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#expereinceDD"
             )
        )
    )

    click_exp.click()

    exp_suggestions = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li[class = ' ']"
             )
        )
    )

    for experience in exp_suggestions:
        if "10 years" in experience.text:
            experience.click()
            break

    location_details = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input[placeholder='Enter location']"
             )
        )
    )

    location_details.send_keys("che")

    location_suggestion = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "li[class='tuple-wrap ']"
             )
        )
    )

    for location in location_suggestion:
        if "Chennai" in location.text:
            location.click()
            break

    submit = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".qsbSubmit"
             )
        )
    )

    submit.click()

    click_on_first_result = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "(//a[@class='title '][1])[1]"
             )
        )
    )

    click_on_first_result.click()

    windowsOpened = driver.window_handles
    driver.switch_to.window(windowsOpened[1])

    job_title = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "h1[class='styles_jd-header-title__rZwM1']"))).text
    company = wait.until(EC.presence_of_element_located(
        (By.XPATH, "/html[1]/body[1]/div[1]/div[1]/main[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/a[1]"))).text
    location = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span[class='styles_jhc__location__W_pVs']"))).text.replace("Hyderabad, ", "").strip()
    readmore = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_read-more-link__dD_5h"))).click()
    job_description = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".styles_JDC__dang-inner-html__h0K4t"))).text

    print(f"Job Title: {job_title}")
    print(f"Company Name: {company}")
    print(f"Location: {location}")
    print("-" * 20)
    print(f"Job Description: {job_description}")
    driver.switch_to.default_content()
    time.sleep(3)

except Exception as e:
    print(f"There is an exception {e}")

driver.quit()


