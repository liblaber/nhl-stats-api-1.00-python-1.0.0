# This file was generated by liblab | https://liblab.com/

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..models.utils.cast_models import cast_models


class MiscellaneousService(BaseService):

    @cast_models
    def get_configuration(self, lang: str) -> dict:
        """Retrieve configuration information.

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
            Serializer(f"{self.base_url}/{{lang}}/config", self.get_default_headers())
            .add_path("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def ping_server(self) -> dict:
        """Ping the server to check connectivity.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: dict
        """

        serialized_request = (
            Serializer(f"{self.base_url}/ping", self.get_default_headers())
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_country_information(self, lang: str) -> dict:
        """Retrieve country information. Returns list of all countries with a hockey presence(?)

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
            Serializer(f"{self.base_url}/{{lang}}/country", self.get_default_headers())
            .add_path("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_shift_charts(self, lang: str, cayenne_exp: str) -> dict:
        """Retrieve shift charts for a specific game.

        :param lang: Language code
        :type lang: str
        :param cayenne_exp: Required
        :type cayenne_exp: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: dict
        """

        Validator(str).validate(lang)
        Validator(str).validate(cayenne_exp)

        serialized_request = (
            Serializer(
                f"{self.base_url}/{{lang}}/shiftcharts", self.get_default_headers()
            )
            .add_path("lang", lang)
            .add_query("cayenneExp", cayenne_exp)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_glossary(self, lang: str) -> dict:
        """Retrieve the glossary for a specific language.

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
            Serializer(f"{self.base_url}/{{lang}}/glossary", self.get_default_headers())
            .add_path("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_content_module(self, lang: str) -> dict:
        """Retrieve content module information.

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
            Serializer(
                f"{self.base_url}/{{lang}}/content/module", self.get_default_headers()
            )
            .add_path("lang", lang)
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response

    @cast_models
    def get_content_module_metadata(self) -> dict:
        """Retrieve metadata for content modules.

        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: Successful response
        :rtype: dict
        """

        serialized_request = (
            Serializer(
                f"{self.base_url}/content/module/meta", self.get_default_headers()
            )
            .serialize()
            .set_method("GET")
        )

        response = self.send_request(serialized_request)

        return response
