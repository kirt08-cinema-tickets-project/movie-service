from kirt08_contracts.movie import movie_pb2

from src.movie import Movie

from src.core.grpc_server.service import to_proto


class gRPC_Movie_Server:
    def __init__(self, movie: Movie):
        self._movie: Movie = movie

    async def ListMovies(self, request, context):
        """
        request.category: string
        request.random:   bool
        request.limit:    int32
        response -> list[Movies]
        """
        res = await self._movie.list_movies(
            category = request.category,
            random = request.random,
            limit = request.limit
        )
        response = movie_pb2.ListMoviesResponse(
            movies=[to_proto(m) for m in res]
        )
        return response

    async def GetMovie(self, request, context):
        """
        oneof key {
            id:   str
            slug: str
        }
        response -> Movie
        """
        pass