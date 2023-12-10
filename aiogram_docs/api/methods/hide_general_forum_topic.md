# hideGeneralForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.hide_general_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.hide_general_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.hide_general_forum_topic import HideGeneralForumTopic`
-   alias: `from aiogram.methods import HideGeneralForumTopic`

#### With specific bot

``` python
result: bool = await bot(HideGeneralForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return HideGeneralForumTopic(...)
```
