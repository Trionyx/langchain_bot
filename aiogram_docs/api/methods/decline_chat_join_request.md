# declineChatJoinRequest

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.decline_chat_join_request
:::

## Usage

### As bot method

``` 
result: bool = await bot.decline_chat_join_request(...)
```

### Method as object

Imports:

-   `from aiogram.methods.decline_chat_join_request import DeclineChatJoinRequest`
-   alias: `from aiogram.methods import DeclineChatJoinRequest`

#### With specific bot

``` python
result: bool = await bot(DeclineChatJoinRequest(...))
```

#### As reply into Webhook in handler

``` python
return DeclineChatJoinRequest(...)
```

### As shortcut from received object

-   `aiogram.types.chat_join_request.ChatJoinRequest.decline`{.interpreted-text
    role="meth"}
