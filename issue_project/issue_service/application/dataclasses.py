from datetime import datetime
from typing import List, Optional

import attr


@attr.dataclass
class Issue:
    action: str
    object_type: str
    object_id: int
    id: Optional[int] = None
    date:  Optional[datetime] = None
