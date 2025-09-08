# -*- coding: utf-8 -*-
from pydantic import BaseModel

class BondInfo(BaseModel):
    date: str # time
    st_id: str # code
    name: str # name
    bond_code: str 
    bond_type: str
    series_number: str
    start: str
    end: str
    money: int # 發行總額
    outstanding_amount: int
    coupon_rate: float
    bond_name: str
    put_option_date: str
    put_option_price: float
    underwriter: str
    trustee: str
    guaranteed: str # 擔保有無
    exchangeprice: str # 轉換價格
    
    
class CompanyInfo(BaseModel):
    company_code: str  # 公司代號
    company_name: str  # 公司名稱
    short_name: str  # 公司簡稱
    market_type: str # 上市櫃
    industry_category: str  # 產業別
    address: str  # 住址
    chairman: str  # 董事長
    establishment_date: str  # 成立日期
    listing_date: str  # 上市日期
    par_value_per_share: str  # 普通股每股面額
    paid_in_capital: int  # 實收資本額
    private_placement_shares: int  # 私募股數
    special_shares: int  # 特別股
    financial_report_type: str  # 編制財務報表類型
    stock_transfer_agent: str  # 股票過戶機構
    issued_common_shares: int  # 已發行普通股數或TDR原股發行股數
    