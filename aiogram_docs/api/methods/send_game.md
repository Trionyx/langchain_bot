# sendGame

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_game
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_game(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_game import SendGame`
-   alias: `from aiogram.methods import SendGame`

#### With specific bot

``` python
result: Message = await bot(SendGame(...))
```

#### As reply into Webhook in handler

``` python
return SendGame(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_game`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_game`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_game`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_game_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_game`{.interpreted-text
    role="meth"}
