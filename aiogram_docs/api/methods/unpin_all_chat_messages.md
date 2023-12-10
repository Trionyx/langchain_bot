# unpinAllChatMessages

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unpin_all_chat_messages
:::

## Usage

### As bot method

``` 
result: bool = await bot.unpin_all_chat_messages(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unpin_all_chat_messages import UnpinAllChatMessages`
-   alias: `from aiogram.methods import UnpinAllChatMessages`

#### With specific bot

``` python
result: bool = await bot(UnpinAllChatMessages(...))
```

#### As reply into Webhook in handler

``` python
return UnpinAllChatMessages(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.unpin_all_messages`{.interpreted-text
    role="meth"}
