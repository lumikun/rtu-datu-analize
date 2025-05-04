import pandas as pd
import numpy

f = "ikea_preces_2.xlsx"
data = pd.read_excel(f)
print(data.dtypes)
print(data.describe())

data["apr.sad."] =  data["apraksts"].str.split(",")

data["laiks"] = numpy.nan
data["izm1"] = numpy.nan
data["izm2"] = numpy.nan
data["izm3"] = numpy.nan
data["svars"] = numpy.nan
data["tilpums"] = numpy.nan

for row_num in range(data.shape[0]):
    print(data["apr.sad."].iloc[row_num])
    if isinstance(data["apr.sad."].iloc[row_num], list):
        # isinstance(ko pārbaudīt, datu tips)
        # pārbauda vai lieta atbilst datu tipam
        if len(data["apr.sad."][row_num]) > 0:
            if data["apr.sad."].iloc[row_num][-1][1].isdigit():
                temp = data["apr.sad."].iloc[row_num][-1]
                if not "/" in temp:
                    if temp.endswith("cm"):
                        if not "-" in temp:
                            if "x" in temp:
                                pass
                            else:
                                temp = temp.replace("cm", "")
                                temp = temp.replace(" ", "")
                                temp = float(temp)
                                data.at[row_num, "izm1"] = temp
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            # pass
    else:
        # print(data["apr.sad."].iloc[row_num])
        pass
print(data)

with pd.ExcelWriter("ikea_preces_3.xlsx") as f:
    data.to_excel(f, sheet_name="Sheet1", index=False)