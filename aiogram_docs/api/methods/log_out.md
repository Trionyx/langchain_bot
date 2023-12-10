# logOut

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.log_out
:::

## Usage

### As bot method

``` 
result: bool = await bot.log_out(...)
```

### Method as object

Imports:

-   `from aiogram.methods.log_out import LogOut`
-   alias: `from aiogram.methods import LogOut`

#### With specific bot

``` python
result: bool = await bot(LogOut(...))
```

#### As reply into Webhook in handler

``` python
return LogOut(...)
```
