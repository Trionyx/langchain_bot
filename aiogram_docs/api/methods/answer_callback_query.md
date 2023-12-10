# answerCallbackQuery

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.answer_callback_query
:::

## Usage

### As bot method

``` 
result: bool = await bot.answer_callback_query(...)
```

### Method as object

Imports:

-   `from aiogram.methods.answer_callback_query import AnswerCallbackQuery`
-   alias: `from aiogram.methods import AnswerCallbackQuery`

#### With specific bot

``` python
result: bool = await bot(AnswerCallbackQuery(...))
```

#### As reply into Webhook in handler

``` python
return AnswerCallbackQuery(...)
```

### As shortcut from received object

-   `aiogram.types.callback_query.CallbackQuery.answer`{.interpreted-text
    role="meth"}
