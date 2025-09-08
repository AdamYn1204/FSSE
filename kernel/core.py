# -*- coding: utf-8 -*-

import os
from pathlib import Path
root_path = Path(__file__).parent.parent
if __name__ == '__main__':
    os.chdir(root_path)
from kernel.crawler.information import info

class Core:
    
    def __init__(self):
        pass

if __name__ == '__main__':
    c = Core()