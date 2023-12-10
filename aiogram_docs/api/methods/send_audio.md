# sendAudio

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_audio
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_audio(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_audio import SendAudio`
-   alias: `from aiogram.methods import SendAudio`

#### With specific bot

``` python
result: Message = await bot(SendAudio(...))
```

#### As reply into Webhook in handler

``` python
return SendAudio(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_audio`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_audio`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_audio`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_audio_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_audio`{.interpreted-text
    role="meth"}
