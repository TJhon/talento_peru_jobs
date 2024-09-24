import argparse
from TalentPeru.selenium_init import scrapper
from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
# linux
# options.binary_location = "/usr/bin/chromium-browser"


def main():
    parser = argparse.ArgumentParser(description="Scraper Jobs")
    # scrapper(n_reg=[1, 2], options=None, github=False)
    parser.add_argument(
        "--n_regs",
        nargs="+",
        type=int,
        required=True,
        help="Lista de registros a procesar. Ejemplo: --n_regs 1 2 3",
    )
    args = parser.parse_args()
    scrapper(n_reg=args.n_regs, options=None, github=False)


if __name__ == "__main__":
    main()
