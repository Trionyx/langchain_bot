# setMyCommands

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_my_commands
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_my_commands(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_my_commands import SetMyCommands`
-   alias: `from aiogram.methods import SetMyCommands`

#### With specific bot

``` python
result: bool = await bot(SetMyCommands(...))
```

#### As reply into Webhook in handler

``` python
return SetMyCommands(...)
```
