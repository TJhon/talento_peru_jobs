import argparse
from selenium_init import scrapper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n_reg", type=int, required=True, help="Numero de region")

    args = parser.parse_args()

    # Aquí puedes utilizar el valor de r_reg como necesites
    scrapper(n_reg=args.n_reg)


if __name__ == "__main__":
    main()
