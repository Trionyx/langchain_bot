# editChatInviteLink

Returns: `ChatInviteLink`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_chat_invite_link
:::

## Usage

### As bot method

``` 
result: ChatInviteLink = await bot.edit_chat_invite_link(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_chat_invite_link import EditChatInviteLink`
-   alias: `from aiogram.methods import EditChatInviteLink`

#### With specific bot

``` python
result: ChatInviteLink = await bot(EditChatInviteLink(...))
```

#### As reply into Webhook in handler

``` python
return EditChatInviteLink(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.edit_invite_link`{.interpreted-text
    role="meth"}
