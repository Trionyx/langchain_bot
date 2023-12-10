# setMyDefaultAdministratorRights

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_my_default_administrator_rights
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_my_default_administrator_rights(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_my_default_administrator_rights import SetMyDefaultAdministratorRights`
-   alias: `from aiogram.methods import SetMyDefaultAdministratorRights`

#### With specific bot

``` python
result: bool = await bot(SetMyDefaultAdministratorRights(...))
```

#### As reply into Webhook in handler

``` python
return SetMyDefaultAdministratorRights(...)
```
