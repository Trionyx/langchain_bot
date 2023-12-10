# stopMessageLiveLocation

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.stop_message_live_location
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.stop_message_live_location(...)
```

### Method as object

Imports:

-   `from aiogram.methods.stop_message_live_location import StopMessageLiveLocation`
-   alias: `from aiogram.methods import StopMessageLiveLocation`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(StopMessageLiveLocation(...))
```

#### As reply into Webhook in handler

``` python
return StopMessageLiveLocation(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.stop_live_location`{.interpreted-text
    role="meth"}
