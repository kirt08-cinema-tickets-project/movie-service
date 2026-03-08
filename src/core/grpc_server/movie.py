

class gRPC_Movie_Server:
    def __init__(self):
        pass

    async def ListMovies(self, request, context):
        """
        request.category: string
        request.random:   bool
        request.limit:    int32
        response -> list[Movies]
        """
        pass

    async def GetMovie(self, request, context):
        """
        oneof key {
            id:   str
            slug: str
        }
        response -> Movie
        """
        pass