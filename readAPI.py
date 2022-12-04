import requests
import os

# Fill in the start_date & end_date & symbols & separators accordingly 
url = "https://api.apilayer.com/exchangerates_data/timeseries?start_date=2021-11-17&end_date=2022-11-17&symbols=EUR,GBP,CHF,AUD,CAD,JPY,CNY&base=USD&separators=' '"

payload = {}
headers= {
  "apikey": os.environ.get('ExRatesAPI_KEY')
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.text
with open("ExRates.csv","w") as f:
  f.write(result)

# When updating the ExRates csv file, only leave "rates" keyword's values in the file, delete the rest of the keywords and afferent data. Use EXAMPLE_ExRates_FORMAT as format excample