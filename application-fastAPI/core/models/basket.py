from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


from .base import Base
from ..mixins.int_id_pk import IntIdPkMixin

if TYPE_CHECKING:
    from .user import User
    from .product import Product


class Basket(IntIdPkMixin, Base):
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    user: Mapped["User"] = relationship(back_populates="basket")
    product: Mapped["Product"] = relationship(back_populates="basket")
