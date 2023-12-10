# setPassportDataErrors

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_passport_data_errors
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_passport_data_errors(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_passport_data_errors import SetPassportDataErrors`
-   alias: `from aiogram.methods import SetPassportDataErrors`

#### With specific bot

``` python
result: bool = await bot(SetPassportDataErrors(...))
```

#### As reply into Webhook in handler

``` python
return SetPassportDataErrors(...)
```
