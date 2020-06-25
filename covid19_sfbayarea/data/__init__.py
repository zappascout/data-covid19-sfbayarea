from typing import Dict, Any
from . import alameda
from . import san_francisco
from . import san_mateo

scrapers: Dict[str, Any] = {
    'alameda': alameda,
    # 'contra_costa': None,
    # 'marin': None,
    # 'napa': None,
    'san_francisco': san_francisco,
    'san_mateo': san_mateo,
    # 'santa_clara': None,
    # 'solano': None,
    # 'sonoma': None,
}
