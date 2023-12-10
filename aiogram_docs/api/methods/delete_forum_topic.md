# deleteForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_forum_topic import DeleteForumTopic`
-   alias: `from aiogram.methods import DeleteForumTopic`

#### With specific bot

``` python
result: bool = await bot(DeleteForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return DeleteForumTopic(...)
```
