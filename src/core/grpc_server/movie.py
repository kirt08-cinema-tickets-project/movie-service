from kirt08_contracts.movie import movie_pb2

from src.movie import Movie

from src.core.grpc_server.service import (
    dto_movie_to_proto_movie_pb2,
    dto_movie_to_proto_movie_details_pb2,
)

from src.movie.exceptions import (
    InvalidDataException,
)


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
            movies=[dto_movie_to_proto_movie_pb2(m) for m in res]
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
        key = request.WhichOneof("key")
        try:
            if key == "id":
                movie = await self._movie.get_movie_by_id(id = request.id)
            else: # if key == "slug"
                movie = await self._movie.get_movie_by_slug(slug = request.slug)
        except InvalidDataException:
            await context.abort(InvalidDataException.grpc_status, InvalidDataException.default_message)
        movie_details = dto_movie_to_proto_movie_details_pb2(movie)
        response = movie_pb2.GetMovieResponse(movie=movie_details)
        return response