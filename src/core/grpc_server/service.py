from google.protobuf.timestamp_pb2 import Timestamp
from kirt08_contracts.movie import movie_pb2

from src.movie.shemas import MovieDatabase

def to_proto(movie: MovieDatabase) -> movie_pb2.Movie:
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