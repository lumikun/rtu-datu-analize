import pandas

data_array = "dati_masiviem.xlsx"

data = pandas.read_excel(data_array)
print(data)
print(data.shape)
print(f"row: {data.shape[0]}")
print(f"col: {data.shape[1]}")
print(data.columns)

data2 = pandas.read_excel(data_array, sheet_name="Sheet1")
print(data2.shape)

info_concat = pandas.concat([data, data2])
print(info_concat.shape)
sorted = info_concat.sort_values("Nr.p.k.")
print(sorted)
sorted_index = sorted.reset_index(drop=True)
print(sorted_index) 
deduplicate = sorted_index.drop_duplicates().reset_index(drop=True)
print(deduplicate)

file = pandas.ExcelFile(data_array)
pages = []
print(file.sheet_names)

for sheet in file.sheet_names:
    pages.append(file.parse(sheet))

# darbs ar tabulu. un neliels uzdevums
print(pages)
pages[0]["Cena gab"] =  round(pages[0]["Pašizmaksa"] * 1.3 * 1.2, 2)
pages[0]["Uzcenojums"] = round(pages[0]["Pašizmaksa"] * 1.3, 2)
pages[0]["Vietas izmaksas"] = round(pages[0]["Skaits"] * 0.1, 2)
pages[0]["Kopā"] = round(pages[0]["Cena gab"] * pages[0]["Skaits"])
pages[0]["Algas"] = round(pages[0]["Kopā"] * 0.05, 3)
pages[0]["Peļņa"] = round(pages[0]["Kopā"] - (pages[0]["Cena gab"] * 0.2) - pages[0]["Pašizmaksa"] - pages[0]["Vietas izmaksas"] - pages[0]["Algas"])
print(pages[0])

# jauna lapa

pages.append(pages[0])
print(len(pages))

insert_row = pages[1][['Skaits', 'Pašizmaksa',
       'Cena gab', 'Uzcenojums', 'Vietas izmaksas', 'Algas', 'Kopā', 'Peļņa']].sum()
print(insert_row) # dati parādas vertikāli
transposed_row = pandas.DataFrame(data = insert_row).T
print(transposed_row)
pages[1] = pages[1].fillna(0)
pages[1] = pandas.concat([pages[1], transposed_row])
print(pages[1])

grouped_data = pages[0][["Datums", "Skaits", "Kopā"]].groupby("Datums").sum().reset_index()
print(grouped_data)
pages.append(grouped_data)

found = pages[2]["Datums"] == "2020-10-20"
print(pages[2][found])
print(pages[2][~found])
found = (pages[0]["Skaits"] < 10) & (pages[0]["Pašizmaksa"]  < 4)
print(pages[0][found])

page_no = 1

with pandas.ExcelWriter("gramatnica.xlsx") as fp:
    for page in pages:
        page.to_excel(fp, sheet_name = "Sheet"+str(page_no), index=False)
        print(f"Sheet{page_no} done!")
        page_no += 1
print("All Done!")

