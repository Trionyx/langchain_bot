# editMessageMedia

Returns: `Union[Message, bool]`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.edit_message_media
:::

## Usage

### As bot method

``` 
result: Union[Message, bool] = await bot.edit_message_media(...)
```

### Method as object

Imports:

-   `from aiogram.methods.edit_message_media import EditMessageMedia`
-   alias: `from aiogram.methods import EditMessageMedia`

#### With specific bot

``` python
result: Union[Message, bool] = await bot(EditMessageMedia(...))
```

#### As reply into Webhook in handler

``` python
return EditMessageMedia(...)
```

### As shortcut from received object

-   `aiogram.types.message.Message.edit_media`{.interpreted-text
    role="meth"}
