# editForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.edit_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_forum_topic import EditForumTopic`
-   alias: `from aiogram.methods import EditForumTopic`

#### With specific bot

``` python
result: bool = await bot(EditForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return EditForumTopic(...)
```
