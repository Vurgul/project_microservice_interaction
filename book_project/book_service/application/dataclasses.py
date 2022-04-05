from typing import List, Optional

import attr


@attr.dataclass
class Book:
    title: str = None
    author: str = None
    id: Optional[int] = None
    status: Optional[bool] = False
