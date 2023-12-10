# setChatMenuButton

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_chat_menu_button
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_chat_menu_button(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_chat_menu_button import SetChatMenuButton`
-   alias: `from aiogram.methods import SetChatMenuButton`

#### With specific bot

``` python
result: bool = await bot(SetChatMenuButton(...))
```

#### As reply into Webhook in handler

``` python
return SetChatMenuButton(...)
```
