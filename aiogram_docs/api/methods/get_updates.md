# getUpdates

Returns: `List[Update]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.get_updates
:::

## Usage

### As bot method

``` 
result: List[Update] = await bot.get_updates(...)
```

### Method as object

Imports:

-   `from aiogram.methods.get_updates import GetUpdates`
-   alias: `from aiogram.methods import GetUpdates`

#### With specific bot

``` python
result: List[Update] = await bot(GetUpdates(...))
```
