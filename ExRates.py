from os import rename
import pandas as pd

ExRates = pd.read_json("ExRates.csv")
# result_df = pd.read_json(result)
ExRates_df = pd.DataFrame(1/ExRates).astype(object)

ExRates_df.loc['UnixTimestamp'] = ExRates_df.columns.astype('int64') // 10**9
ExRates_final_df = ExRates_df.loc[['UnixTimestamp','EUR','GBP','CHF','AUD','CAD', 'JPY', 'CNY']]