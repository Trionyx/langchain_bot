# getMyName

Returns: `BotName`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_my_name
:::

## Usage

### As bot method

``` 
result: BotName = await bot.get_my_name(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_my_name import GetMyName`
-   alias: `from aiogram.methods import GetMyName`

#### With specific bot

``` python
result: BotName = await bot(GetMyName(...))
```
