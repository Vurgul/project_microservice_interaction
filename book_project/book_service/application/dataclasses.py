from typing import Optional

import attr


@attr.dataclass
class Book:
    title: str = None
    author: str = None
    id: Optional[int] = None
    status: Optional[bool] = True
