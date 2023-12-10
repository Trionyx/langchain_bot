# sendVideo

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_video
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_video(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_video import SendVideo`
-   alias: `from aiogram.methods import SendVideo`

#### With specific bot

``` python
result: Message = await bot(SendVideo(...))
```

#### As reply into Webhook in handler

``` python
return SendVideo(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_video`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_video`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_video`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_video_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_video`{.interpreted-text
    role="meth"}
