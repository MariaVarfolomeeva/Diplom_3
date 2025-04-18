import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)


class BrowserConfig:
    def __init__(self, browser_name: str):
        self.browser_name = browser_name
        self.config = load_config()

    def get_driver(self):
        browser_config = self.config['browsers'].get(self.browser_name, {})
        if self.browser_name == 'chrome':
            return self._get_chrome_driver(browser_config)
        elif self.browser_name == 'firefox':
            return self._get_firefox_driver(browser_config)
        else:
            raise ValueError(f"Unsupported browser: {self.browser_name}")

    def _get_chrome_driver(self, config):
        options = Options()
        if config.get("headless", False):
            options.add_argument("--headless")
        if config.get("options"):
            for option, value in config["options"].items():
                options.add_argument(f"--{option}={value}")

        return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def _get_firefox_driver(self, config):
        options = FirefoxOptions()
        if config.get("headless", False):
            options.add_argument("--headless")
        if config.get("options"):
            for option, value in config["options"].items():
                options.add_argument(f"--{option}={value}")

        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
