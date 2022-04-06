from typing import List, Optional

import attr
from datetime import datetime


@attr.dataclass
class Issue:
    action: str
    object_type: str
    object_id: int
    id: Optional[int] = None
    #user_id: Optional[int]
    #book_id: Optional[int]
    #data:  Optional[datetime] = datetime.now()
