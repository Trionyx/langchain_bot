# createChatInviteLink

Returns: `ChatInviteLink`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.create_chat_invite_link
:::

## Usage

### As bot method

``` 
result: ChatInviteLink = await bot.create_chat_invite_link(...)
```

### Method as object

Imports:

-   `from aiogram.methods.create_chat_invite_link import CreateChatInviteLink`
-   alias: `from aiogram.methods import CreateChatInviteLink`

#### With specific bot

``` python
result: ChatInviteLink = await bot(CreateChatInviteLink(...))
```

#### As reply into Webhook in handler

``` python
return CreateChatInviteLink(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.create_invite_link`{.interpreted-text
    role="meth"}
