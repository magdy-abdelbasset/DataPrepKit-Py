from app import DataPrepKit as dpk
import os;
opj_dpk_json = dpk(os.getcwd()+"/src/to_read/test.json")
# opj_dpk_csv = dpk("to_read/test.csv")
# opj_dpk_xlsx = dpk("to_read/test.xlsx",sheet_name = 1, index_col = 0)
# print(opj_dpk_json.get_data())
# print(opj_dpk_csv.get_data())

# example get data
# print(opj_dpk_json.get_data())
# most frequent FOR all value
print(f"most frequent value is : {opj_dpk_json.most_frequent()}")
# most frequent by specify columns
print(f"most frequent value is : {opj_dpk_json.most_frequent('Duration','Pulse')}")

# Avarge FOR all value
print(f"avrage value is : {opj_dpk_json.average()}")
# Avarge by specify columns
print(f"avarge value is : {opj_dpk_json.average('Duration','Pulse')}")