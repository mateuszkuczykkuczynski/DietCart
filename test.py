import pandas as pd
#
file = "C:\\Users\\pyron\\Downloads\\en.openfoodfacts.org.products.csv"
chunksize = 10 ** 3
# with pd.read_csv(file, chunksize=chunksize, sep='	') as reader:
#     for chunk in reader:
#         print(chunk)
# data = pd.read_csv(file, chunksize=10 ** 2, sep='	')
# print(data)

data = pd.read_csv(file, nrows=10, sep='	')
for d in data:
    print(d)
