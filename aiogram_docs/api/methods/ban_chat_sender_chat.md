# banChatSenderChat

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.ban_chat_sender_chat
:::

## Usage

### As bot method

``` 
result: bool = await bot.ban_chat_sender_chat(...)
```

### Method as object

Imports:

-   `from aiogram.methods.ban_chat_sender_chat import BanChatSenderChat`
-   alias: `from aiogram.methods import BanChatSenderChat`

#### With specific bot

``` python
result: bool = await bot(BanChatSenderChat(...))
```

#### As reply into Webhook in handler

``` python
return BanChatSenderChat(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.ban_sender_chat`{.interpreted-text
    role="meth"}
