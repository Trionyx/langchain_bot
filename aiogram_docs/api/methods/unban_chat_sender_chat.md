# unbanChatSenderChat

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.unban_chat_sender_chat
:::

## Usage

### As bot method

``` 
result: bool = await bot.unban_chat_sender_chat(...)
```

### Method as object

Imports:

-   `from aiogram.methods.unban_chat_sender_chat import UnbanChatSenderChat`
-   alias: `from aiogram.methods import UnbanChatSenderChat`

#### With specific bot

``` python
result: bool = await bot(UnbanChatSenderChat(...))
```

#### As reply into Webhook in handler

``` python
return UnbanChatSenderChat(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.unban_sender_chat`{.interpreted-text
    role="meth"}
