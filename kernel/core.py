# -*- coding: utf-8 -*-

import os
from pathlib import Path
root_path = Path(__file__).parent.parent
if __name__ == '__main__':
    os.chdir(root_path)
from kernel.crawler.information import company_info as c_i

class Core:
    
    def __init__(self):
        company_infos = c_i.read_from_db()
        
        pass

if __name__ == '__main__':
    c = Core()