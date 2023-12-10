# unhideGeneralForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unhide_general_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.unhide_general_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unhide_general_forum_topic import UnhideGeneralForumTopic`
-   alias: `from aiogram.methods import UnhideGeneralForumTopic`

#### With specific bot

``` python
result: bool = await bot(UnhideGeneralForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return UnhideGeneralForumTopic(...)
```
