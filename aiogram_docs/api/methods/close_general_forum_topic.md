# closeGeneralForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.close_general_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.close_general_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.close_general_forum_topic import CloseGeneralForumTopic`
-   alias: `from aiogram.methods import CloseGeneralForumTopic`

#### With specific bot

``` python
result: bool = await bot(CloseGeneralForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return CloseGeneralForumTopic(...)
```
