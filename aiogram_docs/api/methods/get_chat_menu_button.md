# getChatMenuButton

Returns:
`Union[MenuButtonDefault, MenuButtonWebApp, MenuButtonCommands]`{.interpreted-text
role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_chat_menu_button
:::

## Usage

### As bot method

``` 
result: Union[MenuButtonDefault, MenuButtonWebApp, MenuButtonCommands] = await bot.get_chat_menu_button(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_chat_menu_button import GetChatMenuButton`
-   alias: `from aiogram.methods import GetChatMenuButton`

#### With specific bot

``` python
result: Union[MenuButtonDefault, MenuButtonWebApp, MenuButtonCommands] = await bot(GetChatMenuButton(...))
```
