# Formatting {#formatting-tool}

Make your message formatting flexible and simple

This instrument works on top of Message entities instead of using HTML
or Markdown markups, you can easily construct your message and sent it
to the Telegram without the need to remember tag parity (opening and
closing) or escaping user input.

## Usage

### Basic scenario

Construct your message and send it to the Telegram.

``` python
content = Text("Hello, ", Bold(message.from_user.full_name), "!")
await message.answer(**content.as_kwargs())
```

Is the same as the next example, but without usage markup

``` python
await message.answer(
    text=f"Hello, <b>{html.quote(message.from_user.full_name)}!",
    parse_mode=ParseMode.HTML
)
```

Literally when you execute `as_kwargs` method the Text object is
converted into text `Hello, Alex!` with entities list
`[MessageEntity(type='bold', offset=7, length=4)]` and passed into dict
which can be used as `**kwargs` in API call.

The complete list of elements is listed [on this page
below](#available-elements).

### Advanced scenario

On top of base elements can be implemented content rendering structures,
so, out of the box aiogram has a few already implemented functions that
helps you to format your messages:

::: autofunction
aiogram.utils.formatting.as_line
:::

::: autofunction
aiogram.utils.formatting.as_list
:::

::: autofunction
aiogram.utils.formatting.as_marked_list
:::

::: autofunction
aiogram.utils.formatting.as_numbered_list
:::

::: autofunction
aiogram.utils.formatting.as_section
:::

::: autofunction
aiogram.utils.formatting.as_marked_section
:::

::: autofunction
aiogram.utils.formatting.as_numbered_section
:::

::: autofunction
aiogram.utils.formatting.as_key_value
:::

and lets complete them all:

``` python
content = as_list(
    as_marked_section(
        Bold("Success:"),
        "Test 1",
        "Test 3",
        "Test 4",
        marker="✅ ",
    ),
    as_marked_section(
        Bold("Failed:"),
        "Test 2",
        marker="❌ ",
    ),
    as_marked_section(
        Bold("Summary:"),
        as_key_value("Total", 4),
        as_key_value("Success", 3),
        as_key_value("Failed", 1),
        marker="  ",
    ),
    HashTag("#test"),
    sep="\n\n",
)
```

Will be rendered into:

> **Success:**
>
> ✅ Test 1
>
> ✅ Test 3
>
> ✅ Test 4
>
> **Failed:**
>
> ❌ Test 2
>
> **Summary:**
>
> > **Total**: 4
> >
> > **Success**: 3
> >
> > **Failed**: 1
>
> #test

Or as HTML:

``` html
<b>Success:</b>
✅ Test 1
✅ Test 3
✅ Test 4

<b>Failed:</b>
❌ Test 2

<b>Summary:</b>
  <b>Total:</b> 4
  <b>Success:</b> 3
  <b>Failed:</b> 1

#test
```

## Available methods

::: {.autoclass members="" show-inheritance="" member-order="bysource" special-members="__init__"}
aiogram.utils.formatting.Text
:::

## Available elements

::: {.autoclass show-inheritance="" noindex=""}
aiogram.utils.formatting.Text
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.HashTag
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.CashTag
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.BotCommand
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Url
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Email
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.PhoneNumber
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Bold
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Italic
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Underline
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Strikethrough
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Spoiler
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Code
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.Pre
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.TextLink
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.TextMention
:::

::: {.autoclass show-inheritance=""}
aiogram.utils.formatting.CustomEmoji
:::
