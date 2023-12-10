# reopenForumTopic

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.reopen_forum_topic
:::

## Usage

### As bot method

``` 
result: bool = await bot.reopen_forum_topic(...)
```

### Method as object

Imports:

-   `from aiogram.methods.reopen_forum_topic import ReopenForumTopic`
-   alias: `from aiogram.methods import ReopenForumTopic`

#### With specific bot

``` python
result: bool = await bot(ReopenForumTopic(...))
```

#### As reply into Webhook in handler

``` python
return ReopenForumTopic(...)
```
