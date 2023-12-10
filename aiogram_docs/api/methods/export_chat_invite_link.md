# exportChatInviteLink

Returns: `str`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.export_chat_invite_link
:::

## Usage

### As bot method

``` 
result: str = await bot.export_chat_invite_link(...)
```

### Method as object

Imports:

-   `from aiogram.methods.export_chat_invite_link import ExportChatInviteLink`
-   alias: `from aiogram.methods import ExportChatInviteLink`

#### With specific bot

``` python
result: str = await bot(ExportChatInviteLink(...))
```

#### As reply into Webhook in handler

``` python
return ExportChatInviteLink(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.export_invite_link`{.interpreted-text
    role="meth"}
