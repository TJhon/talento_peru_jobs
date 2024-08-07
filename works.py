import argparse
from TalentPeru.selenium_init import scrapper
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# linux
options.binary_location = "/usr/bin/chromium-browser"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--n_reg", type=int, required=True, help="Peru-Region number 1-24"
    )
    parser.add_argument("--local", type=int, required=True, help="Run locally")

    args = parser.parse_args()
    if args.local == 1:
        scrapper(n_reg=args.n_reg)
    else:
        scrapper(n_reg=args.n_reg, options=options, github=True)


if __name__ == "__main__":
    main()
