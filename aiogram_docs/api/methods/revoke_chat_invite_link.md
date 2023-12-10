# revokeChatInviteLink

Returns: `ChatInviteLink`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.revoke_chat_invite_link
:::

## Usage

### As bot method

``` 
result: ChatInviteLink = await bot.revoke_chat_invite_link(...)
```

### Method as object

Imports:

-   `from aiogram.methods.revoke_chat_invite_link import RevokeChatInviteLink`
-   alias: `from aiogram.methods import RevokeChatInviteLink`

#### With specific bot

``` python
result: ChatInviteLink = await bot(RevokeChatInviteLink(...))
```

#### As reply into Webhook in handler

``` python
return RevokeChatInviteLink(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.revoke_invite_link`{.interpreted-text
    role="meth"}
