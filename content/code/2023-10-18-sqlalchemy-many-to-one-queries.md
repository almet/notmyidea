---
title: Using DISTINCT in Parent-Child Relationships
headline: How to get parent and most-recent child in a one-to-many relationship
tags: SQL, SQLAlchemy, Python
---

Let's say you have a model defined like this, with a Parent and a Child table:

```python

class Parent(Base):
    __tablename__ = "parent"
    id: Mapped[int] = mapped_column(primary_key=True)

    childs: Mapped[List["Child"]] = relationship(back_populates="parent")


class Child(Base):
    __tablename__ = "child"
    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey("parent.id"))
    parent: Mapped["Parent"] = relationship(back_populates="children")

    born_at: Mapped[datetime] = mapped_column()
```

I've tried many ways, with complex subqueries and the like, before finding out [the DISTINCT SQL statement](https://www.sqlitetutorial.net/sqlite-distinct/).

So, if you want to retrieve the parent with it's more recent child, you can do it like this:

```python

results = (
    db.query(Parent, Child)
    .join(Child)
    .distinct(Parent.id)
    .order_by(Parent.id, desc(Child.born_at))
    .all()
)
```