# setMyName

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.set_my_name
:::

## Usage

### As bot method

``` 
result: bool = await bot.set_my_name(...)
```

### Method as object

Imports:

-   `from aiogram.methods.set_my_name import SetMyName`
-   alias: `from aiogram.methods import SetMyName`

#### With specific bot

``` python
result: bool = await bot(SetMyName(...))
```

#### As reply into Webhook in handler

``` python
return SetMyName(...)
```
