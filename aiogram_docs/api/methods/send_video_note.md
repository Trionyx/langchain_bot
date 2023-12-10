# sendVideoNote

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_video_note
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_video_note(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_video_note import SendVideoNote`
-   alias: `from aiogram.methods import SendVideoNote`

#### With specific bot

``` python
result: Message = await bot(SendVideoNote(...))
```

#### As reply into Webhook in handler

``` python
return SendVideoNote(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_video_note`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_video_note`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_video_note`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_video_note_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_video_note`{.interpreted-text
    role="meth"}
