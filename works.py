import argparse
from TalentPeru.selenium_init import scrapper
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# linux
#options.binary_location = "/usr/bin/chromium-browser"


def main():

    scrapper(n_reg=12, options=options, github=True)


if __name__ == "__main__":
    main()
