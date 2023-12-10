# sendDice

Returns: `Message`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.send_dice
:::

## Usage

### As bot method

``` 
result: Message = await bot.send_dice(...)
```

### Method as object

Imports:

-   `from aiogram.methods.send_dice import SendDice`
-   alias: `from aiogram.methods import SendDice`

#### With specific bot

``` python
result: Message = await bot(SendDice(...))
```

#### As reply into Webhook in handler

``` python
return SendDice(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.answer_dice`{.interpreted-text
    role="meth"}
-   `aiogram.types.message.Message.reply_dice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_dice`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_join_request.ChatJoinRequest.answer_dice_pm`{.interpreted-text
    role="meth"}
-   `aiogram.types.chat_member_updated.ChatMemberUpdated.answer_dice`{.interpreted-text
    role="meth"}
