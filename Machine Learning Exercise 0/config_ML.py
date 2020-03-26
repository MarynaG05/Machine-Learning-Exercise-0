import os

this_dir = os.path.dirname(os.path.realpath(__file__))

DATA_DIR = os.path.join(this_dir, "data")

MELBOURNE_DATA_PATH = os.path.join(DATA_DIR, "Melbourne_housing_FULL.csv")
CORONA_VIRUS_DATA_PATH = os.path.join(DATA_DIR, "covid_19_data.csv")