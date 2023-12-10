# Keyboard builder {#Keyboard builder}

Keyboard builder helps to dynamically generate markup.

::: note
::: title
Note
:::

Note that if you have static markup, it\'s best to define it explicitly
rather than using builder, but if you have dynamic markup configuration,
feel free to use builder as you wish.
:::

## Usage example

For example you want to generate inline keyboard with 10 buttons

``` python
builder = InlineKeyboardBuilder()

for index in range(1, 11):
    builder.button(text=f"Set {index}", callback_data=f"set:{index}")
```

then adjust this buttons to some grid, for example first line will have
3 buttons, the next lines will have 2 buttons

``` 
builder.adjust(3, 2)
```

also you can attach another builder to this one

``` python
another_builder = InlineKeyboardBuilder(...)...  # Another builder with some buttons
builder.attach(another_builder)
```

or you can attach some already generated markup

``` python
markup = InlineKeyboardMarkup(inline_keyboard=[...])  # Some markup
builder.attach(InlineKeyboardBuilder.from_markup(markup))
```

and finally you can export this markup to use it in your message

``` python
await message.answer("Some text here", reply_markup=builder.as_markup())
```

Reply keyboard builder has the same interface

::: warning
::: title
Warning
:::

Note that you can\'t attach reply keyboard builder to inline keyboard
builder and vice versa
:::

## Inline Keyboard

::: {.autoclass members="__init__, buttons, copy, export, add, row, adjust, from_markup, attach"}
aiogram.utils.keyboard.InlineKeyboardBuilder

::: {.method noindex=""}
button(text: str, url: Optional\[str\] = None, login_url:
Optional\[LoginUrl\] = None, callback_data: Optional\[Union\[str,
CallbackData\]\] = None, switch_inline_query: Optional\[str\] = None,
switch_inline_query_current_chat: Optional\[str\] = None, callback_game:
Optional\[CallbackGame\] = None, pay: Optional\[bool\] = None,
\*\*kwargs: Any) -\> aiogram.utils.keyboard.InlineKeyboardBuilder

Add new inline button to markup
:::

::: {.method noindex=""}
as_markup() -\>
aiogram.types.inline_keyboard_markup.InlineKeyboardMarkup

Construct an InlineKeyboardMarkup
:::
:::

## Reply Keyboard

::: {.autoclass members="__init__, buttons, copy, export, add, row, adjust, from_markup, attach"}
aiogram.utils.keyboard.ReplyKeyboardBuilder

::: {.method noindex=""}
button(text: str, request_contact: Optional\[bool\] = None,
request_location: Optional\[bool\] = None, request_poll:
Optional\[KeyboardButtonPollType\] = None, \*\*kwargs: Any) -\>
aiogram.utils.keyboard.ReplyKeyboardBuilder

Add new button to markup
:::

::: {.method noindex=""}
as_markup() -\> aiogram.types.reply_keyboard_markup.ReplyKeyboardMarkup

Construct an ReplyKeyboardMarkup
:::
:::
