# milestone_scraper_robust.py
# Author: Sapient, Tom
# Date: July 21, 2024
# Description: This script scrapes milestone data from a specified URL using either Chrome or Firefox.
#              It attempts to use Chrome first, and falls back to Firefox if Chrome fails.
#              The scraped data is saved in JSON, CSV, and TXT formats.

import logging
import json
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException, NoSuchElementException

# Set up logging to track the script's progress and any errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def setup_chrome_driver():
    """
    Set up and return a Chrome WebDriver instance.
    Returns None if setup fails.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--no-sandbox")  # Disable the sandbox for more stable execution
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    
    try:
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        logging.info("Chrome WebDriver initialized successfully.")
        return driver
    except WebDriverException as e:
        logging.error(f"Failed to initialize Chrome WebDriver: {str(e)}")
        return None

def setup_firefox_driver():
    """
    Set up and return a Firefox WebDriver instance.
    Returns None if setup fails.
    """
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")  # Run in headless mode (no GUI)
    
    try:
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=options)
        logging.info("Firefox WebDriver initialized successfully.")
        return driver
    except WebDriverException as e:
        logging.error(f"Failed to initialize Firefox WebDriver: {str(e)}")
        return None

def scrape_milestone_content(url, driver):
    """
    Scrape milestone content from the given URL using the provided WebDriver.
    Returns a dictionary containing the raw content of the page.
    """
    try:
        driver.get(url)
        logging.info(f"Page title: {driver.title}")

        # Wait for the page to load
        time.sleep(5)  # Simple wait; could be replaced with an explicit wait for a specific element

        # Try different selectors to find the content
        selectors = [
            (By.CLASS_NAME, "milestone-form-group"),
            (By.CLASS_NAME, "form-group"),
            (By.TAG_NAME, "form"),
            (By.TAG_NAME, "body")  # Fallback to get all content
        ]

        content_found = False
        for selector in selectors:
            elements = driver.find_elements(*selector)
            if elements:
                logging.info(f"Found {len(elements)} elements with selector: {selector}")
                content_found = True
                break

        if not content_found:
            logging.warning("No content found with any selector")
            return {}

        # Extract text content from the body of the page
        page_text = driver.find_element(By.TAG_NAME, "body").text
        logging.info(f"Extracted text content (first 500 chars): {page_text[:500]}")

        # Return the raw text content
        return {"raw_content": page_text}

    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
        return {}

def save_as_json(data, filename):
    """Save the scraped data as a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    logging.info(f"Data saved to {filename}")

def save_as_csv(data, filename):
    """Save the scraped data as a CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Key', 'Value'])
        for key, value in data.items():
            writer.writerow([key, value])
    logging.info(f"Data saved to {filename}")

def save_as_txt(data, filename):
    """Save the scraped data as a plain text file."""
    with open(filename, 'w', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}:\n{value}\n\n")
    logging.info(f"Data saved to {filename}")

def main():
    """Main function to orchestrate the scraping process."""
    url = "https://milestones.projectcatalyst.io/projects/1100299/milestones/1"
    
    # Try Chrome first
    driver = setup_chrome_driver()
    
    # If Chrome fails, try Firefox
    if driver is None:
        logging.info("Falling back to Firefox WebDriver.")
        driver = setup_firefox_driver()
    
    if driver is None:
        logging.error("Failed to initialize any WebDriver. Exiting.")
        return
    
    try:
        logging.info("Attempting to scrape data")
        data = scrape_milestone_content(url, driver)
        logging.info(f"Data scraped: {bool(data)}")
        if data:
            save_as_json(data, 'milestone_content.json')
            save_as_csv(data, 'milestone_content.csv')
            save_as_txt(data, 'milestone_content.txt')
            logging.info("Data has been scraped and saved in JSON, CSV, and TXT formats.")
        else:
            logging.warning("No data was scraped from the page.")
    except Exception as e:
        logging.error(f"Scraping failed: {str(e)}", exc_info=True)
    finally:
        driver.quit()

    logging.info("Script execution completed.")

if __name__ == "__main__":
    main()
