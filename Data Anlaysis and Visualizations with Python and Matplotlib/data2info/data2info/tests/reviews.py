import pandas, opencv
from utilities.csv_read import readCSV

data=readCSV("tests/reviews.csv",False)


print(data.hist('Rating'))
