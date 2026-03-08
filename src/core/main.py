import logging
import asyncio

from src.core.config import settings

from src.core.grpc_server import serve

logging.basicConfig(
        format=settings.logger.format, 
        level=settings.logger.log_level   
    )

async def main():
    await serve()

if __name__ == "__main__":
    asyncio.run(main())