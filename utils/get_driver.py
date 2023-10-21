from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from config import HEADLESS, USE_SELNIUM_GRID, SELENIUM_GRID_URL
from utils.helpers import get_node_available

def get_chrome_driver():
    options = webdriver.ChromeOptions()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/107.0.0.0 Safari/537.36"
    )
    if HEADLESS:
        options.add_argument("-headless")
    options.add_argument("window-size=1920x1080")
    options.add_argument("--lang=en")
    options.add_argument("start-maximized")
    options.add_argument("-no-sandbox")
    options.add_argument("-disable-dev-shm-usage")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("test-type")
    options.add_experimental_option(
        "excludeSwitches", ["ignore-certificate-errors"]
    )
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    prefs = {}
    prefs["profile.default_content_settings.popups"] = 0
    prefs["download.prompt_for_download"] = False
    prefs["download.directory_upgrade"] = True
    prefs["plugins.always_open_pdf_externally"] = True
    prefs["profile.default_content_setting_values.automatic_downloads"] = 1
    # disable save creds :
    prefs["credentials_enable_service"] = False
    prefs["profile.password_manager_enabled"] = False
    # disable cookies
    prefs["profile.default_content_settings.cookies"] = 2

    if USE_SELNIUM_GRID:
        nodes = get_node_available(remote_url=SELENIUM_GRID_URL)
        if not nodes:
            raise Exception("Please Check if Selenium Grid is up or not, if it is up check availibality of nodes")
    
        driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, desired_capabilities={'browserName': 'chrome' , 'javascriptEnabled': True, 'goog:loggingPrefs':{'performance': 'ALL'}, 'se:vncEnabled': False}, options=options)

        
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install(),
                                options=options)  # Relevant chromedriver should be in the working directory
    return driver