from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base import Base
from ..mixins.int_id_pk import IntIdPkMixin


if TYPE_CHECKING:
    from .basket import Basket


class User(IntIdPkMixin, Base):
    username: Mapped[str] = mapped_column(unique=True)

    basket: Mapped[list["Basket"]] = relationship(back_populates="user")

