# editMessageLiveLocation

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_message_live_location
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.edit_message_live_location(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_message_live_location import EditMessageLiveLocation`
-   alias: `from aiogram.methods import EditMessageLiveLocation`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(EditMessageLiveLocation(...))
```

#### As reply into Webhook in handler

``` python
return EditMessageLiveLocation(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.edit_live_location`{.interpreted-text
    role="meth"}
