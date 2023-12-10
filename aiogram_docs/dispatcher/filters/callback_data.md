# Callback Data Factory & Filter {#Callback data factory}

::: {.autoclass members="" member-order="bysource" undoc-members="False" exclude-members="model_config,model_fields"}
aiogram.filters.callback_data.CallbackData
:::

## Usage

Create subclass of `CallbackData`:

``` python
class MyCallback(CallbackData, prefix="my"):
    foo: str
    bar: int
```

After that you can generate any callback based on this class, for
example:

``` python
cb1 = MyCallback(foo="demo", bar=42)
cb1.pack()  # returns 'my:demo:42'
cb1.unpack('my:demo:42')  # returns <MyCallback(foo="demo", bar=42)>
```

So\... Now you can use this class to generate any callbacks with defined
structure

``` python
...
# Pass it into the markup
InlineKeyboardButton(
    text="demo",
    callback_data=MyCallback(foo="demo", bar="42").pack()  # value should be packed to string
)
...
```

\... and handle by specific rules

``` python
# Filter callback by type and value of field :code:`foo`
@router.callback_query(MyCallback.filter(F.foo == "demo"))
async def my_callback_foo(query: CallbackQuery, callback_data: MyCallback):
    await query.answer(...)
    ...
    print("bar =", callback_data.bar)
```

Also can be used in
`Keyboard builder </utils/keyboard>`{.interpreted-text role="doc"}:

``` python
builder = InlineKeyboardBuilder()
builder.button(
    text="demo",
    callback_data=MyCallback(foo="demo", bar="42")  # Value can be not packed to string inplace, because builder knows what to do with callback instance
)
```

Another abstract example:

``` python
class Action(str, Enum):
    ban = "ban"
    kick = "kick"
    warn = "warn"

class AdminAction(CallbackData, prefix="adm"):
    action: Action
    chat_id: int
    user_id: int

...
# Inside handler
builder = InlineKeyboardBuilder()
for action in Action:
    builder.button(
        text=action.value.title(),
        callback_data=AdminAction(action=action, chat_id=chat_id, user_id=user_id),
    )
await bot.send_message(
    chat_id=admins_chat,
    text=f"What do you want to do with {html.quote(name)}",
    reply_markup=builder.as_markup(),
)
...

@router.callback_query(AdminAction.filter(F.action == Action.ban))
async def ban_user(query: CallbackQuery, callback_data: AdminAction, bot: Bot):
    await bot.ban_chat_member(
        chat_id=callback_data.chat_id,
        user_id=callback_data.user_id,
        ...
    )
```

## Known limitations

Allowed types and their subclasses:

-   `str`
-   `int`
-   `bool`
-   `float`
-   `Decimal` (`from decimal import Decimal`)
-   `Fraction` (`from fractions import Fraction`)
-   `UUID` (`from uuid import UUID`)
-   `Enum` (`from enum import Enum`, only for string enums)
-   `IntEnum` (`from enum import IntEnum`, only for int enums)

::: note
::: title
Note
:::

Note that the integer Enum\'s should be always is subclasses of
`IntEnum` in due to parsing issues.
:::
