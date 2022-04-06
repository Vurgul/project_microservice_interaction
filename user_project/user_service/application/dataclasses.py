from typing import Optional

import attr


@attr.dataclass
class User:
    name: str = None
    age: int = None
    id: Optional[int] = None
