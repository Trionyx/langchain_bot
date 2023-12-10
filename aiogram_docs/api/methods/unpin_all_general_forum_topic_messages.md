# unpinAllGeneralForumTopicMessages

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unpin_all_general_forum_topic_messages
:::

## Usage

### As bot method

``` 
result: bool = await bot.unpin_all_general_forum_topic_messages(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unpin_all_general_forum_topic_messages import UnpinAllGeneralForumTopicMessages`
-   alias:
    `from aiogram.methods import UnpinAllGeneralForumTopicMessages`

#### With specific bot

``` python
result: bool = await bot(UnpinAllGeneralForumTopicMessages(...))
```

#### As reply into Webhook in handler

``` python
return UnpinAllGeneralForumTopicMessages(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.unpin_all_general_forum_topic_messages`{.interpreted-text
    role="meth"}
