# unpinAllForumTopicMessages

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unpin_all_forum_topic_messages
:::

## Usage

### As bot method

``` 
result: bool = await bot.unpin_all_forum_topic_messages(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unpin_all_forum_topic_messages import UnpinAllForumTopicMessages`
-   alias: `from aiogram.methods import UnpinAllForumTopicMessages`

#### With specific bot

``` python
result: bool = await bot(UnpinAllForumTopicMessages(...))
```

#### As reply into Webhook in handler

``` python
return UnpinAllForumTopicMessages(...)
```
