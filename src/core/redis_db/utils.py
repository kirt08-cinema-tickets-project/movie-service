class MovieCacheKeys:
    @classmethod
    def all(cls, category: str, random: bool, limit: int):
        return ":".join(
            [
                "movies",
                "list",
                "all" if not category else category,
                "random" if random else "ordered",
                "nolimit" if not limit else str(limit)
            ]
        )

    @classmethod
    def bySlug(cls, slug: str):
        return f"movies:slug:{slug}"
    
    @classmethod
    def byId(cls, id: str):
        return f"movies:id:{id}"
