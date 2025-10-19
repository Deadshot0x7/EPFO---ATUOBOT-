import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import getpass

class EPFOAccess:
    def __init__(self):
        self.base_url = "https://unifiedportal-mem.epfindia.gov.in/memberinterface/"
        self.driver = None
        
    def setup_driver(self):
        """Setup Chrome WebDriver with options"""
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        
        # Uncomment below for headless mode
        # chrome_options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.wait = WebDriverWait(self.driver, 20)
        
    def login(self, uan, password):
        """Login to EPFO portal"""
        try:
            print("Opening EPFO portal...")
            self.driver.get(self.base_url)
            time.sleep(3)
            
            # Enter UAN
            print("Entering UAN...")
            uan_field = self.wait.until(
                EC.presence_of_element_located((By.ID, "username"))
            )
            uan_field.clear()
            uan_field.send_keys(uan)
            
            # Enter Password
            print("Entering password...")
            password_field = self.driver.find_element(By.ID, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Handle Captcha (Manual entry required)
            print("\n*** Please solve the captcha manually ***")
            input("Press Enter after solving captcha and before clicking Sign In...")
            
            # Click Sign In
            sign_in_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            sign_in_btn.click()
            
            time.sleep(5)
            print("Login successful!")
            return True
            
        except Exception as e:
            print(f"Login failed: {str(e)}")
            return False
    
    def access_passbook(self):
        """Access and view EPF passbook"""
        try:
            print("\nAccessing Passbook...")
            
            # Navigate to View section
            view_menu = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View"))
            )
            view_menu.click()
            time.sleep(2)
            
            # Click on Passbook
            passbook_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Passbook"))
            )
            passbook_link.click()
            time.sleep(3)
            
            # Get member ID dropdown and select first option
            member_id_select = self.wait.until(
                EC.presence_of_element_located((By.ID, "memberid"))
            )
            member_id_select.click()
            time.sleep(1)
            
            # Select first member ID from dropdown
            first_option = self.driver.find_element(
                By.XPATH, "//select[@id='memberid']/option[2]"
            )
            first_option.click()
            time.sleep(2)
            
            print("Passbook loaded successfully!")
            print("You can now view your passbook details on screen.")
            time.sleep(5)
            
            return True
            
        except Exception as e:
            print(f"Error accessing passbook: {str(e)}")
            return False
    
    def access_service_history(self):
        """Access service history"""
        try:
            print("\nAccessing Service History...")
            
            # Navigate to View section if not already there
            view_menu = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View"))
            )
            view_menu.click()
            time.sleep(2)
            
            # Click on Service History
            service_history_link = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Service History"))
            )
            service_history_link.click()
            time.sleep(3)
            
            print("Service History loaded successfully!")
            print("You can now view your service history on screen.")
            time.sleep(5)
            
            return True
            
        except Exception as e:
            print(f"Error accessing service history: {str(e)}")
            return False
    
    def download_passbook(self):
        """Download passbook as PDF"""
        try:
            print("\nDownloading Passbook PDF...")
            
            # Look for download button
            download_btn = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Download')]"))
            )
            download_btn.click()
            time.sleep(3)
            
            print("Passbook download initiated!")
            return True
            
        except Exception as e:
            print(f"Error downloading passbook: {str(e)}")
            return False
    
    def close(self):
        """Close the browser"""
        if self.driver:
            print("\nClosing browser...")
            self.driver.quit()

def main():
    print("=" * 50)
    print("EPFO Account Access Script")
    print("=" * 50)
    print("\nPlease provide your EPFO credentials:")
    print("-" * 50)
    
    # Get credentials from user
    uan = input("\nEnter your UAN (Universal Account Number): ").strip()
    
    # Validate UAN (should be 12 digits)
    while not uan.isdigit() or len(uan) != 12:
        print("Invalid UAN! UAN should be 12 digits.")
        uan = input("Enter your UAN (Universal Account Number): ").strip()
    
    password = getpass.getpass("Enter your EPFO password: ")
    
    # Confirm credentials
    print(f"\nUAN entered: {uan}")
    confirm = input("Is this correct? (y/n): ")
    
    if confirm.lower() != 'y':
        print("Please restart the script and enter correct credentials.")
        return
    
    # Create EPFO access instance
    epfo = EPFOAccess()
    
    try:
        # Setup driver
        epfo.setup_driver()
        
        # Login
        if epfo.login(uan, password):
            print("\n" + "=" * 50)
            print("What would you like to access?")
            print("1. Passbook")
            print("2. Service History")
            print("3. Both")
            print("=" * 50)
            
            choice = input("\nEnter your choice (1/2/3): ")
            
            if choice in ['1', '3']:
                epfo.access_passbook()
                
                # Ask if user wants to download
                download = input("\nDo you want to download passbook? (y/n): ")
                if download.lower() == 'y':
                    epfo.download_passbook()
            
            if choice in ['2', '3']:
                epfo.access_service_history()
            
            # Keep browser open for viewing
            input("\nPress Enter to close browser...")
        
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
    
    finally:
        epfo.close()
        print("\nScript completed!")

if __name__ == "__main__":
    main()
