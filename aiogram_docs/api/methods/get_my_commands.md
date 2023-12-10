# getMyCommands

Returns: `List[BotCommand]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_my_commands
:::

## Usage

### As bot method

``` 
result: List[BotCommand] = await bot.get_my_commands(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_my_commands import GetMyCommands`
-   alias: `from aiogram.methods import GetMyCommands`

#### With specific bot

``` python
result: List[BotCommand] = await bot(GetMyCommands(...))
```
