# GameService

A list of all methods in the `GameService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                 |
| :-------------------------------------------- | :-------------------------- |
| [get_game_information](#get_game_information) | Retrieve game information.  |
| [get_game_metadata](#get_game_metadata)       | Retrieve metadata for game. |

## get_game_information

Retrieve game information.

- HTTP Method: `GET`
- Endpoint: `/{lang}/game`

**Parameters**

| Name | Type | Required | Description   |
| :--- | :--- | :------- | :------------ |
| lang | str  | ✅       | Language code |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.game.get_game_information(lang="lang")

print(result)
```

## get_game_metadata

Retrieve metadata for game.

- HTTP Method: `GET`
- Endpoint: `/{lang}/game/meta`

**Parameters**

| Name | Type | Required | Description   |
| :--- | :--- | :------- | :------------ |
| lang | str  | ✅       | Language code |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.game.get_game_metadata(lang="lang")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
