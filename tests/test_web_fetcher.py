import warnings
warnings.simplefilter("ignore", DeprecationWarning)

import os
import sys
from pathlib import Path
import asyncio

root = str(Path(__file__).resolve().parents[1])
sys.path.append(root)

from src.tools.web_fetcher import WebFetcherTool
from src.models import model_manager

if __name__ == "__main__":
    model_manager.init_models(use_local_proxy=False)
    
    fetcher = WebFetcherTool()
    url = "https://www.scientistsforxr.earth/2023-ipcc"
    content = asyncio.run(fetcher.forward(url))
    print(content)