from typing import List, Optional

import attr


@attr.dataclass
class Issue:
    title: str = None
    author: str = None
    id: Optional[int] = None
    status: Optional[bool] = False
