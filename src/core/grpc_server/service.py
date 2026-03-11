from google.protobuf.timestamp_pb2 import Timestamp
from kirt08_contracts.movie import movie_pb2

from src.movie.shemas import MovieDatabase

def dto_movie_to_proto_movie_pb2(movie: MovieDatabase) -> movie_pb2.Movie:
    ts = None

    if movie.release_date:
        ts = Timestamp()
        ts.FromDatetime(movie.release_date)

    return movie_pb2.Movie(
        id=str(movie.id),
        title=movie.title,
        slug=movie.slug,
        poster=movie.poster,
        rating_age=movie.rating_age,
        release_date=ts,
    )

def dto_movie_to_proto_movie_details_pb2(movie: MovieDatabase) -> movie_pb2.MovieDetails:
    ts = None

    if movie.release_date:
        ts = Timestamp()
        ts.FromDatetime(movie.release_date)

    return movie_pb2.MovieDetails(
        id=str(movie.id),
        title=movie.title,
        slug=movie.slug,
        description=movie.description,
        poster=movie.poster,
        banner=movie.banner,
        duration=movie.duration,
        rating_age=movie.rating_age,
        country=movie.country,
        release_date=ts,
    )