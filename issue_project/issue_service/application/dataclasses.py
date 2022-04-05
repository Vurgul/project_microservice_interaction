from typing import List, Optional

import attr
from datetime import datetime


@attr.dataclass
class Issue:
    action: str
    id: Optional[int]
    user_id: Optional[int]
    book_id: Optional[int]
    data:  Optional[datetime] = datetime.now()
