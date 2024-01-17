import pandas as pd
import numpy as np
ExRates = pd.read_json("ExRates.csv")
ExRates_df = pd.DataFrame(1/ExRates).astype(object)

ExRates_final_df = ExRates_df