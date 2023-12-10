# sendVoice

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_voice
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_voice(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_voice import SendVoice`
-   alias: `from aiogram.methods import SendVoice`

#### With specific bot

``` python
result: Message = await bot(SendVoice(...))
```

#### As reply into Webhook in handler

``` python
return SendVoice(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_voice`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_voice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_voice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_voice_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_voice`{.interpreted-text
    role="meth"}
