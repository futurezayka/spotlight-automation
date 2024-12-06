import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from app.constants import SPOTLIGHT_URL
from app.selectors import LOGIN_BUTTON_SELECTOR
from app.wallet import WalletConnect


class SpotlightAutomation:
    def __init__(self):
        self.driver = self.__get_driver()
        self.__wallet = WalletConnect(self.driver)

    @staticmethod
    def __get_driver() -> uc.Chrome:
        options = uc.ChromeOptions()
        # options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--load-extension=metamask")
        options.add_argument("--disable-blink-features=AutomationControlled")

        return uc.Chrome(options=options)

    def __click_login_button(self):
        self.driver.get(SPOTLIGHT_URL)
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.XPATH, LOGIN_BUTTON_SELECTOR)))
        self.driver.find_element(By.XPATH, LOGIN_BUTTON_SELECTOR).click()

    def __call__(self, *args, **kwargs):
        self.__wallet.setup_metamask_wallet()
        self.__click_login_button()
        self.__wallet.connect()
