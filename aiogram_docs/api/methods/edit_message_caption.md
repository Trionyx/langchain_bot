# editMessageCaption

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_message_caption
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.edit_message_caption(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_message_caption import EditMessageCaption`
-   alias: `from aiogram.methods import EditMessageCaption`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(EditMessageCaption(...))
```

#### As reply into Webhook in handler

``` python
return EditMessageCaption(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.edit_caption`{.interpreted-text
    role="meth"}
