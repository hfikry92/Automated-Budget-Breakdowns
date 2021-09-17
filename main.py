import tabula
import os
file = "jeffords-rules.pdf"
tables = tabula.read_pdf(file, pages="all")
# save them in a folder
folder_name = "tables"
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)
# iterate over extracted tables and export as excel individually
for i, table in enumerate(tables, start=1):
    table.to_csv(os.path.join(folder_name, f"table_{i}.csv"), index=False)