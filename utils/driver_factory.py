from config.browser_config import BrowserConfig


class DriverFactory:
    @staticmethod
    def create_driver(browser_name: str):
        browser_config = BrowserConfig(browser_name)
        return browser_config.get_driver()
