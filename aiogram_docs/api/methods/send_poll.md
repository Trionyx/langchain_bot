# sendPoll

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_poll
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_poll(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_poll import SendPoll`
-   alias: `from aiogram.methods import SendPoll`

#### With specific bot

``` python
result: Message = await bot(SendPoll(...))
```

#### As reply into Webhook in handler

``` python
return SendPoll(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_poll`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_poll`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_poll`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_poll_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_poll`{.interpreted-text
    role="meth"}
