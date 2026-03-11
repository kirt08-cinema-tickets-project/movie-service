from kirt08_contracts.category import category_pb2

from src.categories import Category

from src.core.grpc_server.service import (
    dto_category_to_proto_category_pb2,
)


class gRPC_Category_Server:
    def __init__(self, category: Category):
        self._category: Category = category

    async def GetAllCategories(self, request, context):
        """
        request: Empty
        response: repeated Category categories; Category(id, title, slug)
        """
        categories = await self._category.get_all_categories()
        response = category_pb2.GetAllCategoriesResponse(
            categories = [dto_category_to_proto_category_pb2(category) for category in categories]
        )
        return response
        