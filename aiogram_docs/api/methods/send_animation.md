# sendAnimation

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_animation
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_animation(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_animation import SendAnimation`
-   alias: `from aiogram.methods import SendAnimation`

#### With specific bot

``` python
result: Message = await bot(SendAnimation(...))
```

#### As reply into Webhook in handler

``` python
return SendAnimation(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_animation`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_animation`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_animation`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_animation_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_animation`{.interpreted-text
    role="meth"}
