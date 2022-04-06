from typing import List, Optional

import attr
from datetime import datetime


@attr.dataclass
class Issue:
    action: str
    object_type: str
    object_id: int
    id: Optional[int] = None
    # data:  Optional[datetime] = datetime.now()
