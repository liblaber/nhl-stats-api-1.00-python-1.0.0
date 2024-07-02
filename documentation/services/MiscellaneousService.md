# MiscellaneousService

A list of all methods in the `MiscellaneousService` service. Click on the method name to view detailed information about that method.

| Methods                                                     | Description                                                                           |
| :---------------------------------------------------------- | :------------------------------------------------------------------------------------ |
| [get_configuration](#get_configuration)                     | Retrieve configuration information.                                                   |
| [ping_server](#ping_server)                                 | Ping the server to check connectivity.                                                |
| [get_country_information](#get_country_information)         | Retrieve country information. Returns list of all countries with a hockey presence(?) |
| [get_shift_charts](#get_shift_charts)                       | Retrieve shift charts for a specific game.                                            |
| [get_glossary](#get_glossary)                               | Retrieve the glossary for a specific language.                                        |
| [get_content_module](#get_content_module)                   | Retrieve content module information.                                                  |
| [get_content_module_metadata](#get_content_module_metadata) | Retrieve metadata for content modules.                                                |

## get_configuration

Retrieve configuration information.

- HTTP Method: `GET`
- Endpoint: `/{lang}/config`

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

result = sdk.miscellaneous.get_configuration(lang="lang")

print(result)
```

## ping_server

Ping the server to check connectivity.

- HTTP Method: `GET`
- Endpoint: `/ping`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.miscellaneous.ping_server()

print(result)
```

## get_country_information

Retrieve country information. Returns list of all countries with a hockey presence(?)

- HTTP Method: `GET`
- Endpoint: `/{lang}/country`

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

result = sdk.miscellaneous.get_country_information(lang="lang")

print(result)
```

## get_shift_charts

Retrieve shift charts for a specific game.

- HTTP Method: `GET`
- Endpoint: `/{lang}/shiftcharts`

**Parameters**

| Name        | Type | Required | Description   |
| :---------- | :--- | :------- | :------------ |
| lang        | str  | ✅       | Language code |
| cayenne_exp | str  | ✅       | Required      |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.miscellaneous.get_shift_charts(
    lang="lang",
    cayenne_exp="cayenneExp"
)

print(result)
```

## get_glossary

Retrieve the glossary for a specific language.

- HTTP Method: `GET`
- Endpoint: `/{lang}/glossary`

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

result = sdk.miscellaneous.get_glossary(lang="lang")

print(result)
```

## get_content_module

Retrieve content module information.

- HTTP Method: `GET`
- Endpoint: `/{lang}/content/module`

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

result = sdk.miscellaneous.get_content_module(lang="lang")

print(result)
```

## get_content_module_metadata

Retrieve metadata for content modules.

- HTTP Method: `GET`
- Endpoint: `/content/module/meta`

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.miscellaneous.get_content_module_metadata()

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->