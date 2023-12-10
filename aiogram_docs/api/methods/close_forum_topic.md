# closeForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.close_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.close_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.close_forum_topic import CloseForumTopic`
-   alias: `from aiogram.methods import CloseForumTopic`

#### With specific bot

``` python
result: bool = await bot(CloseForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return CloseForumTopic(...)
```
