from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base import Base
from ..mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .basket import Basket


class Product(IntIdPkMixin, Base):
    product_name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[str] = mapped_column(String(20))
    quantity: Mapped[int]

    basket: Mapped[list["Basket"]] = relationship(back_populates="product")
