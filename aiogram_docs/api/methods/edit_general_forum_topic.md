# editGeneralForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_general_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.edit_general_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_general_forum_topic import EditGeneralForumTopic`
-   alias: `from aiogram.methods import EditGeneralForumTopic`

#### With specific bot

``` python
result: bool = await bot(EditGeneralForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return EditGeneralForumTopic(...)
```
