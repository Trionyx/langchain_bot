# Callback answer

Helper for callback query handlers, can be useful in bots with a lot of
callback handlers to automatically take answer to all requests.

# Simple usage

For use, it is enough to register the inner middleware
`aiogram.utils.callback_answer.CallbackAnswerMiddleware`{.interpreted-text
role="class"} in dispatcher or specific router:

``` python
dispatcher.callback_query.middleware(CallbackAnswerMiddleware())
```

After that all handled callback queries will be answered automatically
after processing the handler.

# Advanced usage

In some cases you need to have some non-standard response parameters,
this can be done in several ways:

## Global defaults

Change default parameters while initializing middleware, for example
change answer to [pre]{.title-ref} mode and text \"OK\":

``` python
dispatcher.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text="OK"))
```

Look at
`aiogram.utils.callback_answer.CallbackAnswerMiddleware`{.interpreted-text
role="class"} to get all available parameters

## Handler specific

By using `flags <flags>`{.interpreted-text role="ref"} you can change
the behavior for specific handler

``` python
@router.callback_query(<filters>)
@flags.callback_answer(text="Thanks", cache_time=30)
async def my_handler(query: CallbackQuery):
    ...
```

Flag arguments is the same as in
`aiogram.utils.callback_answer.CallbackAnswerMiddleware`{.interpreted-text
role="class"} with additional one `disabled` to disable answer.

## A special case

It is not always correct to answer the same in every case, so there is
an option to change the answer inside the handler. You can get an
instance of
`aiogram.utils.callback_answer.CallbackAnswer`{.interpreted-text
role="class"} object inside handler and change whatever you want.

::: danger
::: title
Danger
:::

Note that is impossible to change callback answer attributes when you
use `pre=True` mode.
:::

``` python
@router.callback_query(<filters>)
async def my_handler(query: CallbackQuery, callback_answer: CallbackAnswer):
    ...
    if <everything is ok>:
        callback_answer.text = "All is ok"
    else:
        callback_answer.text = "Something wrong"
        callback_answer.cache_time = 10
```

## Combine that all at once

For example you want to answer in most of cases before handler with text
\"🤔\" but at some cases need to answer after the handler with custom
text, so you can do it:

``` python
dispatcher.callback_query.middleware(CallbackAnswerMiddleware(pre=True, text="🤔"))

@router.callback_query(<filters>)
@flags.callback_answer(pre=False, cache_time=30)
async def my_handler(query: CallbackQuery):
    ...
    if <everything is ok>:
        callback_answer.text = "All is ok"
```

# Description of objects

::: {.autoclass show-inheritance="" member-order="bysource" special-members="__init__" members=""}
aiogram.utils.callback_answer.CallbackAnswerMiddleware
:::

::: {.autoclass show-inheritance="" member-order="bysource" special-members="__init__" members=""}
aiogram.utils.callback_answer.CallbackAnswer
:::
