# leaveChat

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.leave_chat
:::

## Usage

### As bot method

``` 
result: bool = await bot.leave_chat(...)
```

### Method as object

Imports:

-   `from aiogram.methods.leave_chat import LeaveChat`
-   alias: `from aiogram.methods import LeaveChat`

#### With specific bot

``` python
result: bool = await bot(LeaveChat(...))
```

#### As reply into Webhook in handler

``` python
return LeaveChat(...)
```

### As shortcut from received object

-   `aiogram.types.chat.Chat.leave`{.interpreted-text role="meth"}
