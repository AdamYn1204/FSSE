# -*- coding: utf-8 -*-
import queue
import requests
import threading
import os
from pathlib import Path
root_path = Path(__file__).parent.parent
if __name__ == '__main__':
    os.chdir(root_path)
from kernel.crawler.models import CompanyInfo

class Information:
    
    def __init__(self):
        pass
    
    def parse_company_information(self):
        'get company info'
        def fetch_data_1(result_queue):
            '上市'
            try:
                req = requests.get('https://openapi.twse.com.tw/v1/opendata/t187ap03_L')
                data_dict = req.json()
                key_mapping = {
                        "公司代號": "stock_id",
                        "公司名稱": "company_name",
                        "公司簡稱": "short_name",
                        "產業別": "industry_category",
                        "住址": "address",
                        "董事長": "chairman",
                        "成立日期": "establishment_date",
                        "上市日期": "listing_date",
                        "普通股每股面額": "par_value_per_share",
                        "實收資本額": "paid_in_capital",
                        "私募股數": "private_placement_shares",
                        "特別股": "special_shares",
                        "股票過戶機構": "stock_transfer_agent",
                        "已發行普通股數或TDR原股發行股數": "issued_common_shares"}
                parsed_data = [
                        {key_mapping.get(k, k): v for k, v in item.items() if key_mapping.get(k) in CompanyInfo.__fields__}
                        for item in data_dict]
                for i in parsed_data:
                    i['market_type'] = '上市'
                print(parsed_data[0])
                result_queue.put(("One", parsed_data))
            except Exception as e:
                result_queue.put(("One", f"錯誤: {str(e)}"))
        
        def fetch_data_2(result_queue):
            '上櫃'
            try:
                req = requests.get('https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap03_O')
                data_dict = req.json()
                key_mapping = {
                        "SecuritiesCompanyCode": "stock_id",
                        "CompanyName": "company_name",
                        "CompanyAbbreviation": "short_name",
                        "SecuritiesIndustryCode": "industry_category",
                        "Address": "address",
                        "Chairman": "chairman",
                        "DateOfIncorporation": "establishment_date",
                        "DateOfListing": "listing_date",
                        "ParValueOfCommonStock": "par_value_per_share",
                        "Paidin.Capital.NTDollars": "paid_in_capital",
                        "PrivateStock.shares": "private_placement_shares",
                        "PreferredStock.shares": "special_shares",
                        # "PreparationOfFinancialReportType": "financial_report_type",
                        "StockTransferAgent": "stock_transfer_agent",
                        "IssueShares": "issued_common_shares"
                    }
                
                parsed_data = [{key_mapping.get(k, k): v for k, v in item.items() if key_mapping.get(k) in CompanyInfo.__fields__}
                        for item in data_dict]
                for t in parsed_data:
                    t['market_type'] = '上櫃'
                print(parsed_data[0])
                result_queue.put(("Two", parsed_data))
            except Exception as e:
                result_queue.put(("Two", f"錯誤: {str(e)}"))
        
        result_queue = queue.Queue()
        t1 = threading.Thread(target=fetch_data_1, args=(result_queue,))
        t2 = threading.Thread(target=fetch_data_2, args=(result_queue,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        results = []
        while not result_queue.empty():
            source, data = result_queue.get()
            if type(data) != list:
                print(data)
            results.extend(data)
        
        return results   
    
info = Information()