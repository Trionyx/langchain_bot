# deleteMyCommands

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.delete_my_commands
:::

## Usage

### As bot method

``` 
result: bool = await bot.delete_my_commands(...)
```

### Method as object

Imports:

-   `from aiogram.methods.delete_my_commands import DeleteMyCommands`
-   alias: `from aiogram.methods import DeleteMyCommands`

#### With specific bot

``` python
result: bool = await bot(DeleteMyCommands(...))
```

#### As reply into Webhook in handler

``` python
return DeleteMyCommands(...)
```
