# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class PlayersService(BaseService):

    @cast_models
    def get_player_information(self, lang: str) -> dict:
        """Retrieve player information. Currently seems to return a truncated list with a total.

        :param lang: Language code
        :type lang: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: dict
        """

        Validator(str).validate(lang)

        serialized_request = (
            Serializer(f"{self.base_url}/{{lang}}/players", self.get_default_headers())
            .add_path("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response