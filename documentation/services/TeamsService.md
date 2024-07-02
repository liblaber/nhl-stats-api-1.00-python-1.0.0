# TeamsService

A list of all methods in the `TeamsService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                                |
| :------------------------------------------------------ | :----------------------------------------- |
| [get_team_information](#get_team_information)           | Retrieve list of all teams.                |
| [get_team_stats](#get_team_stats)                       | Retrieve team stats for a specific report. |
| [get_franchise_information](#get_franchise_information) | Retrieve list of all franchises.           |

## get_team_information

Retrieve list of all teams.

- HTTP Method: `GET`
- Endpoint: `/{lang}/team`

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

result = sdk.teams.get_team_information(lang="lang")

print(result)
```

## get_team_stats

Retrieve team stats for a specific report.

- HTTP Method: `GET`
- Endpoint: `/{lang}/team/{report}`

**Parameters**

| Name             | Type | Required | Description                                            |
| :--------------- | :--- | :------- | :----------------------------------------------------- |
| report           | str  | ✅       | Team report                                            |
| lang             | str  | ✅       | Language code                                          |
| is_aggregate     | bool | ❌       | Optional                                               |
| is_game          | bool | ❌       | Optional                                               |
| fact_cayenne_exp | str  | ❌       | Optional                                               |
| include          | str  | ❌       | Optional                                               |
| exclude          | str  | ❌       | Optional                                               |
| cayenne_exp      | str  | ❌       | Optional                                               |
| sort             | str  | ❌       | Optional                                               |
| dir              | str  | ❌       | Optional                                               |
| start            | int  | ❌       | Optional                                               |
| limit            | int  | ❌       | Optional (Note: a limit of -1 will return all results) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from nhl_stats import NhlStats, Environment

sdk = NhlStats(
    base_url=Environment.DEFAULT.value
)

result = sdk.teams.get_team_stats(
    report="report",
    lang="lang",
    is_aggregate=False,
    is_game=False,
    fact_cayenne_exp="factCayenneExp",
    include="include",
    exclude="exclude",
    cayenne_exp="cayenneExp",
    sort="sort",
    dir="dir",
    start=8,
    limit=1
)

print(result)
```

## get_franchise_information

Retrieve list of all franchises.

- HTTP Method: `GET`
- Endpoint: `/{lang}/franchise`

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

result = sdk.teams.get_franchise_information(lang="lang")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->