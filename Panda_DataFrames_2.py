import pandas as pd
data = {
    "calories" : [400, 490, 370],
    "duration" : [300, 320, 290]

}
myvar = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(myvar)