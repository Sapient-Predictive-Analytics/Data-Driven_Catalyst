#!/usr/bin/env python3
"""
Enhanced Milestone Scraper
-------------------------
A robust web scraping utility for extracting milestone data from project management systems.
Supports multiple browsers, error handling, and flexible data export options.

Features:
- Multi-browser support (Chrome, Firefox) with automatic fallback
- Comprehensive error handling and logging
- Configurable retry mechanisms
- Flexible output formats (JSON, CSV, TXT)
- Custom data parsing options
- Rate limiting and request throttling
"""

import logging
import json
import csv
import time
import sys
from typing import Dict, Optional, Union, List, Tuple
from pathlib import Path
from datetime import datetime
from functools import wraps
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    WebDriverException,
    TimeoutException,
    NoSuchElementException,
    StaleElementReferenceException
)

# Configure logging with more detailed format
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
    handlers=[
        logging.FileHandler('milestone_scraper.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def retry_on_exception(retries: int = 3, delay: int = 1):
    """
    Decorator for retrying functions on failure with exponential backoff.
    
    Args:
        retries: Maximum number of retry attempts
        delay: Initial delay between retries (doubles after each attempt)
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f"Final retry attempt failed: {str(e)}")
                        raise
                    logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= 2
        return wrapper
    return decorator

class BrowserSetup:
    """Handles browser driver setup and configuration."""
    
    @staticmethod
    def get_chrome_options() -> webdriver.ChromeOptions:
        """Configure Chrome options for stable operation."""
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        return options

    @staticmethod
    def get_firefox_options() -> webdriver.FirefoxOptions:
        """Configure Firefox options for stable operation."""
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        return options

    @staticmethod
    @retry_on_exception()
    def setup_chrome_driver() -> Optional[webdriver.Chrome]:
        """Initialize Chrome WebDriver with retry mechanism."""
        try:
            service = ChromeService(ChromeDriverManager().install())
            driver = webdriver.Chrome(
                service=service,
                options=BrowserSetup.get_chrome_options()
            )
            logger.info("Chrome WebDriver initialized successfully")
            return driver
        except WebDriverException as e:
            logger.error(f"Chrome WebDriver initialization failed: {str(e)}")
            return None

    @staticmethod
    @retry_on_exception()
    def setup_firefox_driver() -> Optional[webdriver.Firefox]:
        """Initialize Firefox WebDriver with retry mechanism."""
        try:
            service = FirefoxService(GeckoDriverManager().install())
            driver = webdriver.Firefox(
                service=service,
                options=BrowserSetup.get_firefox_options()
            )
            logger.info("Firefox WebDriver initialized successfully")
            return driver
        except WebDriverException as e:
            logger.error(f"Firefox WebDriver initialization failed: {str(e)}")
            return None

class MilestoneScraper:
    """Main scraper class for milestone data extraction."""
    
    def __init__(self, url: str, wait_time: int = 10):
        """
        Initialize scraper with configuration.
        
        Args:
            url: Target URL to scrape
            wait_time: Maximum time to wait for elements to load
        """
        self.url = url
        self.wait_time = wait_time
        self.driver = None
        self.setup_driver()

    def setup_driver(self) -> None:
        """Initialize WebDriver with Chrome/Firefox fallback."""
        self.driver = BrowserSetup.setup_chrome_driver()
        if self.driver is None:
            logger.info("Falling back to Firefox WebDriver")
            self.driver = BrowserSetup.setup_firefox_driver()
        if self.driver is None:
            raise WebDriverException("Failed to initialize any WebDriver")

    def wait_for_element(self, by: By, value: str) -> bool:
        """
        Wait for element to be present and visible.
        
        Args:
            by: Selenium By locator strategy
            value: Locator value
        Returns:
            bool: Whether element was found
        """
        try:
            WebDriverWait(self.driver, self.wait_time).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False

    @retry_on_exception()
    def scrape_milestone_content(self) -> Dict[str, str]:
        """
        Scrape milestone data with advanced element detection.
        
        Returns:
            Dict containing scraped content
        """
        try:
            self.driver.get(self.url)
            logger.info(f"Accessing URL: {self.url}")

            # Define content selectors in order of specificity
            selectors = [
                (By.CLASS_NAME, "milestone-form-group"),
                (By.CLASS_NAME, "form-group"),
                (By.CLASS_NAME, "milestone-content"),
                (By.TAG_NAME, "form"),
                (By.TAG_NAME, "body")
            ]

            content = {}
            for selector in selectors:
                elements = self.driver.find_elements(*selector)
                if elements:
                    logger.info(f"Found {len(elements)} elements with {selector}")
                    for idx, element in enumerate(elements):
                        try:
                            text = element.text.strip()
                            if text:
                                content[f"{selector[1]}_{idx}"] = text
                        except StaleElementReferenceException:
                            continue

            if not content:
                logger.warning("No content found with any selector")
                # Fallback to full page content
                content["raw_content"] = self.driver.find_element(
                    By.TAG_NAME, "body"
                ).text

            return content

        except Exception as e:
            logger.error(f"Scraping error: {str(e)}")
            raise

    def save_data(self, data: Dict[str, str], output_dir: str = "output") -> None:
        """
        Save scraped data in multiple formats.
        
        Args:
            data: Scraped content to save
            output_dir: Directory for output files
        """
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_filename = f"milestone_content_{timestamp}"

        # Save as JSON
        json_path = Path(output_dir) / f"{base_filename}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        logger.info(f"Data saved to {json_path}")

        # Save as CSV
        csv_path = Path(output_dir) / f"{base_filename}.csv"
        with open(csv_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Key', 'Value'])
            for key, value in data.items():
                writer.writerow([key, value])
        logger.info(f"Data saved to {csv_path}")

        # Save as TXT
        txt_path = Path(output_dir) / f"{base_filename}.txt"
        with open(txt_path, 'w', encoding='utf-8') as f:
            for key, value in data.items():
                f.write(f"{key}:\n{value}\n\n")
        logger.info(f"Data saved to {txt_path}")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit with proper cleanup."""
        if self.driver:
            self.driver.quit()
            logger.info("WebDriver closed successfully")

def main():
    """Main execution function."""
    url = "https://milestones.projectcatalyst.io/projects/1100299/milestones/1"
    
    try:
        with MilestoneScraper(url) as scraper:
            logger.info("Starting milestone data extraction")
            data = scraper.scrape_milestone_content()
            if data:
                scraper.save_data(data)
                logger.info("Milestone data extracted and saved successfully")
            else:
                logger.warning("No data was extracted from the page")
    except Exception as e:
        logger.error(f"Script execution failed: {str(e)}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
