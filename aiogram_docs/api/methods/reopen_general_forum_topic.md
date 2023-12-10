# reopenGeneralForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.reopen_general_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.reopen_general_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.reopen_general_forum_topic import ReopenGeneralForumTopic`
-   alias: `from aiogram.methods import ReopenGeneralForumTopic`

#### With specific bot

``` python
result: bool = await bot(ReopenGeneralForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return ReopenGeneralForumTopic(...)
```
