# approveChatJoinRequest

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.approve_chat_join_request
:::

## Usage

### As bot method

``` 
result: bool = await bot.approve_chat_join_request(...)
```

### Method as object

Imports:

-   `from aiogram.methods.approve_chat_join_request import ApproveChatJoinRequest`
-   alias: `from aiogram.methods import ApproveChatJoinRequest`

#### With specific bot

``` python
result: bool = await bot(ApproveChatJoinRequest(...))
```

#### As reply into Webhook in handler

``` python
return ApproveChatJoinRequest(...)
```

### As shortcut from received object

-   `aiogram.types.chat_join_request.ChatJoinRequest.approve`{.interpreted-text
    role="meth"}
