from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base import Base
from ..mixins.int_id_pk import IntIdPkMixin


if TYPE_CHECKING:
    from .basket import Basket


class Profile(IntIdPkMixin, Base):
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(30))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
