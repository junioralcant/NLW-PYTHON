
from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreateController:
    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        return self.__format_response(path_from_tag)

    def __create_tag(self, product_code: str) -> str:
        barcode_handle = BarcodeHandler()
        path_from_tag = barcode_handle.create_barcode(product_code)
        return path_from_tag

    def __format_response(self, path_from_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_from_tag}.png'
            }
        }
    