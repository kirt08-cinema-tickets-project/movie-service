import grpc
import logging

from kirt08_contracts.movie import movie_pb2, movie_pb2_grpc

from src.movie.handler import Movie

from src.core.config import settings

from src.core.db import service_insert_all_data_from_seed, db

from src.core.grpc_server.movie import gRPC_Movie_Server


log = logging.getLogger(__name__)

async def serve():
    """
    async function to start up grpc server
    """
    
    log.info("gRPC server starting up...")

    movie = Movie(db)

    server = grpc.aio.server()

    movie_pb2_grpc.add_MovieServiceServicer_to_server(
        gRPC_Movie_Server(movie),
        server
    )

    url = f"{settings.grpc.host}:{settings.grpc.port}"
    server.add_insecure_port(url)
    await server.start()
    
    log.info("Server successfully started!")
    
    async with db.session() as session:
        await service_insert_all_data_from_seed(session = session)

    await server.wait_for_termination()

