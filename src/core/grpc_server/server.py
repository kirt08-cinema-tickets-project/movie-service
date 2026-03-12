import grpc
import logging

from kirt08_contracts.movie import movie_pb2_grpc
from kirt08_contracts.category import category_pb2_grpc

from src.movie import Movie
from src.categories import Category

from src.core.config import settings

from src.core.db import service_insert_all_data_from_seed, db
from src.core.redis_db import get_redis, RedisService

from src.core.grpc_server.movie import gRPC_Movie_Server
from src.core.grpc_server.category import gRPC_Category_Server


log = logging.getLogger(__name__)

async def serve():
    """
    async function to start up grpc server
    """
    
    log.info("gRPC server starting up...")

    redis: RedisService = await get_redis()
    movie = Movie(db, redis)
    category = Category(db)

    server = grpc.aio.server()

    movie_pb2_grpc.add_MovieServiceServicer_to_server(
        gRPC_Movie_Server(movie = movie),
        server = server
    )

    category_pb2_grpc.add_CategoryServiceServicer_to_server(
        gRPC_Category_Server(category = category),
        server = server
    )

    url = f"{settings.grpc.host}:{settings.grpc.port}"
    server.add_insecure_port(url)
    await server.start()
    
    log.info("Server successfully started!")
    
    async with db.session() as session:
        await service_insert_all_data_from_seed(session = session)

    await server.wait_for_termination()

