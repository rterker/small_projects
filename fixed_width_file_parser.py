import pandas as pd
from pathlib import Path


file_path = Path.home().joinpath('Desktop'). joinpath('working_dir')

col_widths = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 40, 20, 20, 20]
col_names = ['client_id', 'acct_name', 'cust_acct_id', 'accrued_income_base', 'acq_date', 'bank_id', 'book_value_base', 'book_value_local', 'cost_base', 'cross_curr', 'curr_base', 'cusip', 'exchange_rate', 'isin', 'issue_dt', 'location', 'lng_sht_ind', 'port_value', 'market_value_base', 'mat_date', 'original_face', 'price_base', 'price_type', 'price_src', 'put_call_ind', 'quantity', 'quantity_multiplier', 'record_type', 'sedol', 'symbol', 'uc_base', 'uc_local', 'acct_type', 'description', 'marketvalue', 'accrued_income_local', 'price']

def build_and_write_output_file(file_path: Path, col_widths: list, col_names: list, file=None):
    if file == None:
        list_of_dfs = []
        custody_codes = []
        for file in file_path.iterdir():
            if file.suffix == '.HLD':
                data_frame = pd.read_fwf(file, widths=col_widths)
                data_frame.columns = col_names
                custody_codes.append(file.name[0:12])
                list_of_dfs.append(data_frame) 
        data_frame = pd.concat(list_of_dfs)        
        data_frame.to_excel(file_path.joinpath("_".join(custody_codes) + '.xlsx'), index=False)
    else: 
        data_frame = pd.read_fwf(file, widths=col_widths)
        data_frame.columns = col_names
        data_frame.to_excel(file_path.joinpath(file.name + '.xlsx'), index=False)

def main():
    # You can include a kwarg 'file' if you want to input a single file, instead of iterating over all files in the working_dir.
    # file_name = 'XXXXXXXXXX'
    build_and_write_output_file(file_path, col_widths, col_names)#, file=file_path.joinpath(file_name))

if __name__ == '__main__':
    main()

