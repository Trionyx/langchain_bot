# close

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.close
:::

## Usage

### As bot method

``` 
result: bool = await bot.close(...)
```

### Method as object

Imports:

-   `from aiogram.methods.close import Close`
-   alias: `from aiogram.methods import Close`

#### With specific bot

``` python
result: bool = await bot(Close(...))
```

#### As reply into Webhook in handler

``` python
return Close(...)
```
