# answerInlineQuery

Returns: `bool`{.interpreted-text role="obj"}

::: {.automodule members="" member-order="bysource" undoc-members="True" exclude-members="model_config,model_fields"}
aiogram.methods.answer_inline_query
:::

## Usage

### As bot method

``` 
result: bool = await bot.answer_inline_query(...)
```

### Method as object

Imports:

-   `from aiogram.methods.answer_inline_query import AnswerInlineQuery`
-   alias: `from aiogram.methods import AnswerInlineQuery`

#### With specific bot

``` python
result: bool = await bot(AnswerInlineQuery(...))
```

#### As reply into Webhook in handler

``` python
return AnswerInlineQuery(...)
```

### As shortcut from received object

-   `aiogram.types.inline_query.InlineQuery.answer`{.interpreted-text
    role="meth"}
