import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def run():

    for file in os.listdir(os.path.join(BASE_DIR, 'files')):
        try:
            df = pd.read_excel(os.path.join(BASE_DIR, 'files', file))
        except Exception:
            df = pd.read_html(os.path.join(BASE_DIR, 'files', file))
        print(df)

if __name__ == "__main__":
    run()