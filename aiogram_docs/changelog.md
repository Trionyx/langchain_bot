::: {#aiogram_changes}
# Changelog

::: towncrier-draft-entries
\[UNRELEASED DRAFT\]
:::

## 3.2.0 (2023-11-24)

### Features

-   Introduced Scenes feature that helps you to simplify user
    interactions using Finite State Machine. Read more about 👉
    `Scenes <Scenes>`{.interpreted-text role="ref"}.
    [#1280](https://github.com/aiogram/aiogram/issues/1280)
-   Added the new FSM strategy `CHAT_TOPIC`, which sets the state for
    the entire topic in the chat, also works in private messages and
    regular groups without topics.
    [#1343](https://github.com/aiogram/aiogram/issues/1343)

### Bugfixes

-   Fixed `parse_mode` argument in the in `Message.send_copy` shortcut.
    Disable by default.
    [#1332](https://github.com/aiogram/aiogram/issues/1332)
-   Added ability to get handler flags from filters.
    [#1360](https://github.com/aiogram/aiogram/issues/1360)
-   Fixed a situation where a `CallbackData` could not be parsed without
    a default value.
    [#1368](https://github.com/aiogram/aiogram/issues/1368)

### Improved Documentation

-   Corrected grammatical errors, improved sentence structures,
    translation for migration 2.x-3.x
    [#1302](https://github.com/aiogram/aiogram/issues/1302)
-   Minor typo correction, specifically in module naming + some grammar.
    [#1340](https://github.com/aiogram/aiogram/issues/1340)
-   Added [CITATION.cff]{.title-ref} file for automatic academic
    citation generation. Now you can copy citation from the GitHub page
    and paste it into your paper.
    [#1351](https://github.com/aiogram/aiogram/issues/1351)
-   Minor typo correction in middleware docs.
    [#1353](https://github.com/aiogram/aiogram/issues/1353)

### Misc

-   Fixed ResourceWarning in the tests, reworked `RedisEventsIsolation`
    fixture to use Redis connection from `RedisStorage`
    [#1320](https://github.com/aiogram/aiogram/issues/1320)

-   Updated dependencies, bumped minimum required version:

    -   `magic-filter` - fixed [.resolve]{.title-ref} operation
    -   `pydantic` - fixed compatibility (broken in 2.4)
    -   `aiodns` - added new dependency to the `fast` extras
        (`pip install aiogram[fast]`)

    \- *others\...*
    [#1327](https://github.com/aiogram/aiogram/issues/1327)

-   Prevent update handling task pointers from being garbage collected,
    backport from 2.x
    [#1331](https://github.com/aiogram/aiogram/issues/1331)

-   Updated `typing-extensions` package version range in dependencies to
    fix compatibility with `FastAPI`
    [#1347](https://github.com/aiogram/aiogram/issues/1347)

-   Introduce Python 3.12 support
    [#1354](https://github.com/aiogram/aiogram/issues/1354)

-   Speeded up CallableMixin processing by caching references to nested
    objects and simplifying kwargs assembly.
    [#1357](https://github.com/aiogram/aiogram/issues/1357)

-   Added `pydantic` v2.5 support.
    [#1361](https://github.com/aiogram/aiogram/issues/1361)

-   Updated `thumbnail` fields type to `InputFile` only
    [#1372](https://github.com/aiogram/aiogram/issues/1372)

## 3.1.1 (2023-09-25)

### Bugfixes

-   Fixed [pydantic]{.title-ref} version \<2.4, since 2.4 has breaking
    changes. [#1322](https://github.com/aiogram/aiogram/issues/1322)

## 3.1.0 (2023-09-22)

### Features

-   Added support for custom encoders/decoders for payload (and also for
    deep-linking).
    [#1262](https://github.com/aiogram/aiogram/issues/1262)
-   Added
    `aiogram.utils.input_media.MediaGroupBuilder`{.interpreted-text
    role="class"} for media group construction.
    [#1293](https://github.com/aiogram/aiogram/issues/1293)
-   Added full support of [Bot API
    6.9](https://core.telegram.org/bots/api-changelog#september-22-2023)
    [#1319](https://github.com/aiogram/aiogram/issues/1319)

### Bugfixes

-   Added actual param hints for [InlineKeyboardBuilder]{.title-ref} and
    [ReplyKeyboardBuilder]{.title-ref}.
    [#1303](https://github.com/aiogram/aiogram/issues/1303)
-   Fixed priority of events isolation, now user state will be loaded
    only after lock is acquired
    [#1317](https://github.com/aiogram/aiogram/issues/1317)

## 3.0.0 (2023-09-01)

### Bugfixes

-   Replaced `datetime.datetime` with [DateTime]{.title-ref} type
    wrapper across types to make dumped JSONs object more compatible
    with data that is sent by Telegram.
    [#1277](https://github.com/aiogram/aiogram/issues/1277)
-   Fixed magic `.as_(...)` operation for values that can be interpreted
    as [False]{.title-ref} (e.g. [0]{.title-ref}).
    [#1281](https://github.com/aiogram/aiogram/issues/1281)
-   Italic markdown from utils now uses correct decorators
    [#1282](https://github.com/aiogram/aiogram/issues/1282)
-   Fixed method `Message.send_copy` for stickers.
    [#1284](https://github.com/aiogram/aiogram/issues/1284)
-   Fixed `Message.send_copy` method, which was not working properly
    with stories, so not you can copy stories too (forwards messages).
    [#1286](https://github.com/aiogram/aiogram/issues/1286)
-   Fixed error overlapping when validation error is caused by
    remove_unset root validator in base types and methods.
    [#1290](https://github.com/aiogram/aiogram/issues/1290)

## 3.0.0rc2 (2023-08-18)

### Bugfixes

-   Fixed missing message content types (`ContentType.USER_SHARED`,
    `ContentType.CHAT_SHARED`)
    [#1252](https://github.com/aiogram/aiogram/issues/1252)
-   Fixed nested hashtag, cashtag and email message entities not being
    parsed correctly when these entities are inside another entity.
    [#1259](https://github.com/aiogram/aiogram/issues/1259)
-   Moved global filters check placement into router to add chance to
    pass context from global filters into handlers in the same way as it
    possible in other places
    [#1266](https://github.com/aiogram/aiogram/issues/1266)

### Improved Documentation

-   Added error handling example
    [examples/error_handling.py]{.title-ref}
    [#1099](https://github.com/aiogram/aiogram/issues/1099)
-   Added a few words about skipping pending updates
    [#1251](https://github.com/aiogram/aiogram/issues/1251)
-   Added a section on Dependency Injection technology
    [#1253](https://github.com/aiogram/aiogram/issues/1253)
-   This update includes the addition of a multi-file bot example to the
    repository. [#1254](https://github.com/aiogram/aiogram/issues/1254)
-   Refactored examples code to use aiogram enumerations and enhanced
    chat messages with markdown beautification\'s for a more
    user-friendly display.
    [#1256](https://github.com/aiogram/aiogram/issues/1256)
-   Supplemented \"Finite State Machine\" section in Migration FAQ
    [#1264](https://github.com/aiogram/aiogram/issues/1264)
-   Removed extra param in docstring of TelegramEventObserver\'s filter
    method and fixed typo in I18n documentation.
    [#1268](https://github.com/aiogram/aiogram/issues/1268)

### Misc

-   Enhanced the warning message in dispatcher to include a JSON dump of
    the update when update type is not known.
    [#1269](https://github.com/aiogram/aiogram/issues/1269)
-   Added support for [Bot API
    6.8](https://core.telegram.org/bots/api-changelog#august-18-2023)
    [#1275](https://github.com/aiogram/aiogram/issues/1275)

## 3.0.0rc1 (2023-08-06)

### Features

-   Added Currency enum. You can use it like this:

    ``` python
    from aiogram.enums import Currency

    await bot.send_invoice(
        ...,
        currency=Currency.USD,
        ...
    )
    ```

    [#1194](https://github.com/aiogram/aiogram/issues/1194)

-   Updated keyboard builders with new methods for integrating buttons
    and keyboard creation more seamlessly. Added functionality to create
    buttons from existing markup and attach another builder. This
    improvement aims to make the keyboard building process more
    user-friendly and flexible.
    [#1236](https://github.com/aiogram/aiogram/issues/1236)

-   Added support for message_thread_id in ChatActionSender
    [#1249](https://github.com/aiogram/aiogram/issues/1249)

### Bugfixes

-   Fixed polling startup when \"bot\" key is passed manually into
    dispatcher workflow data
    [#1242](https://github.com/aiogram/aiogram/issues/1242)

-   Added codegen configuration for lost shortcuts:

    -   ShippingQuery.answer
    -   PreCheckoutQuery.answer

    \- Message.delete_reply_markup
    [#1244](https://github.com/aiogram/aiogram/issues/1244)

### Improved Documentation

-   Added documentation for webhook and polling modes.
    [#1241](https://github.com/aiogram/aiogram/issues/1241)

### Misc

-   Reworked InputFile reading, removed `__aiter__` method, added [bot:
    Bot]{.title-ref} argument to the `.read(...)` method, so, from now
    URLInputFile can be used without specifying bot instance.
    [#1238](https://github.com/aiogram/aiogram/issues/1238)
-   Code-generated `__init__` typehints in types and methods to make IDE
    happy without additional pydantic plugin
    [#1245](https://github.com/aiogram/aiogram/issues/1245)

## 3.0.0b9 (2023-07-30)

### Features

-   Added new shortcuts for
    `aiogram.types.chat_member_updated.ChatMemberUpdated`{.interpreted-text
    role="class"} to send message to chat that member joined/left.
    [#1234](https://github.com/aiogram/aiogram/issues/1234)
-   Added new shortcuts for
    `aiogram.types.chat_join_request.ChatJoinRequest`{.interpreted-text
    role="class"} to make easier access to sending messages to users who
    wants to join to chat.
    [#1235](https://github.com/aiogram/aiogram/issues/1235)

### Bugfixes

-   Fixed bot assignment in the `Message.send_copy` shortcut
    [#1232](https://github.com/aiogram/aiogram/issues/1232)
-   Added model validation to remove UNSET before field validation. This
    change was necessary to correctly handle parse_mode where \'UNSET\'
    is used as a sentinel value. Without the removal of \'UNSET\', it
    would create issues when passed to model initialization from
    Bot.method_name. \'UNSET\' was also added to typing.
    [#1233](https://github.com/aiogram/aiogram/issues/1233)
-   Updated pydantic to 2.1 with few bugfixes

### Improved Documentation

-   Improved docs, added basic migration guide (will be expanded later)
    [#1143](https://github.com/aiogram/aiogram/issues/1143)

### Deprecations and Removals

-   Removed the use of the context instance (Bot.get_current) from all
    placements that were used previously. This is to avoid the use of
    the context instance in the wrong place.
    [#1230](https://github.com/aiogram/aiogram/issues/1230)

## 3.0.0b8 (2023-07-17)

### Features

-   Added possibility to use custom events in routers (If router does
    not support custom event it does not break and passes it to included
    routers). [#1147](https://github.com/aiogram/aiogram/issues/1147)

-   Added support for FSM in Forum topics.

    The strategy can be changed in dispatcher:

    ``` python
    from aiogram.fsm.strategy import FSMStrategy
    ...
    dispatcher = Dispatcher(
        fsm_strategy=FSMStrategy.USER_IN_TOPIC,
        storage=...,  # Any persistent storage
    )
    ```

    ::: note
    ::: title
    Note
    :::

    If you have implemented you own storages you should extend record
    key generation with new one attribute - `thread_id`
    :::

    [#1161](https://github.com/aiogram/aiogram/issues/1161)

-   Improved CallbackData serialization.

    -   Minimized UUID (hex without dashes)

    \- Replaced bool values with int (true=1, false=0)
    [#1163](https://github.com/aiogram/aiogram/issues/1163)

-   Added a tool to make text formatting flexible and easy. More details
    on the
    `corresponding documentation page <formatting-tool>`{.interpreted-text
    role="ref"} [#1172](https://github.com/aiogram/aiogram/issues/1172)

-   Added `X-Telegram-Bot-Api-Secret-Token` header check
    [#1173](https://github.com/aiogram/aiogram/issues/1173)

-   Made `allowed_updates` list to revolve automatically in
    start_polling method if not set explicitly.
    [#1178](https://github.com/aiogram/aiogram/issues/1178)

-   Added possibility to pass custom headers to
    `URLInputFile`{.interpreted-text role="class"} object
    [#1191](https://github.com/aiogram/aiogram/issues/1191)

### Bugfixes

-   Change type of result in InlineQueryResult enum for
    `InlineQueryResultCachedMpeg4Gif` and `InlineQueryResultMpeg4Gif` to
    more correct according to documentation.

    Change regexp for entities parsing to more correct
    (`InlineQueryResultType.yml`).
    [#1146](https://github.com/aiogram/aiogram/issues/1146)

-   Fixed signature of startup/shutdown events to include the
    `**dispatcher.workflow_data` as the handler arguments.
    [#1155](https://github.com/aiogram/aiogram/issues/1155)

-   Added missing `FORUM_TOPIC_EDITED` value to content_type property
    [#1160](https://github.com/aiogram/aiogram/issues/1160)

-   Fixed compatibility with Python 3.8-3.9 (from previous release)
    [#1162](https://github.com/aiogram/aiogram/issues/1162)

-   Fixed the markdown spoiler parser.
    [#1176](https://github.com/aiogram/aiogram/issues/1176)

-   Fixed workflow data propagation
    [#1196](https://github.com/aiogram/aiogram/issues/1196)

-   Fixed the serialization error associated with nested subtypes like
    InputMedia, ChatMember, etc.

    The previously generated code resulted in an invalid schema under
    pydantic v2, which has stricter type parsing. Hence, subtypes
    without the specification of all subtype unions were generating an
    empty object. This has been rectified now.
    [#1213](https://github.com/aiogram/aiogram/issues/1213)

### Improved Documentation

-   Changed small grammar typos for `upload_file`
    [#1133](https://github.com/aiogram/aiogram/issues/1133)

### Deprecations and Removals

-   Removed text filter in due to is planned to remove this filter few
    versions ago.

    Use `F.text` instead
    [#1170](https://github.com/aiogram/aiogram/issues/1170)

### Misc

-   Added full support of [Bot API
    6.6](https://core.telegram.org/bots/api-changelog#march-9-2023)

    ::: danger
    ::: title
    Danger
    :::

    Note that this issue has breaking changes described in in the Bot
    API changelog, this changes is not breaking in the API but breaking
    inside aiogram because Beta stage is not finished.
    :::

    [#1139](https://github.com/aiogram/aiogram/issues/1139)

-   Added full support of [Bot API
    6.7](https://core.telegram.org/bots/api-changelog#april-21-2023)

    ::: warning
    ::: title
    Warning
    :::

    Note that arguments *switch_pm_parameter* and *switch_pm_text* was
    deprecated and should be changed to *button* argument as described
    in API docs.
    :::

    [#1168](https://github.com/aiogram/aiogram/issues/1168)

-   Updated [Pydantic to V2](https://docs.pydantic.dev/2.0/migration/)

    ::: warning
    ::: title
    Warning
    :::

    Be careful, not all libraries is already updated to using V2
    :::

    [#1202](https://github.com/aiogram/aiogram/issues/1202)

-   Added global defaults `disable_web_page_preview` and
    `protect_content` in addition to `parse_mode` to the Bot instance,
    reworked internal request builder mechanism.
    [#1142](https://github.com/aiogram/aiogram/issues/1142)

-   Removed bot parameters from storages
    [#1144](https://github.com/aiogram/aiogram/issues/1144)

-   Replaced ContextVar\'s with a new feature called [Validation
    Context](https://docs.pydantic.dev/latest/usage/validators/#validation-context)
    in Pydantic to improve the clarity, usability, and versatility of
    handling the Bot instance within method shortcuts.

    ::: danger
    ::: title
    Danger
    :::

    **Breaking**: The \'bot\' argument now is required in
    [URLInputFile]{.title-ref}
    :::

    [#1210](https://github.com/aiogram/aiogram/issues/1210)

-   Updated magic-filter with new features

    -   Added hint for `len(F)` error

    \- Added not in operation
    [#1221](https://github.com/aiogram/aiogram/issues/1221)

## 3.0.0b7 (2023-02-18)

::: warning
::: title
Warning
:::

Note that this version has incompatibility with Python 3.8-3.9 in case
when you create an instance of Dispatcher outside of the any coroutine.

Sorry for the inconvenience, it will be fixed in the next version.

This code will not work:

``` python
dp = Dispatcher()

def main():
    ...
    dp.run_polling(...)

main()
```

But if you change it like this it should works as well:

``` python
router = Router()

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    ...
    dp.start_polling(...)

asyncio.run(main())
```
:::

### Features

-   Added missing shortcuts, new enums, reworked old stuff

    **Breaking** All previously added enums is re-generated in new
    place - [aiogram.enums]{.title-ref} instead of
    [aiogram.types]{.title-ref}

    **Added enums:** `aiogram.enums.bot_command_scope_type.BotCommandScopeType`{.interpreted-text role="class"},

    :   `aiogram.enums.chat_action.ChatAction`{.interpreted-text
        role="class"},
        `aiogram.enums.chat_member_status.ChatMemberStatus`{.interpreted-text
        role="class"},
        `aiogram.enums.chat_type.ChatType`{.interpreted-text
        role="class"},
        `aiogram.enums.content_type.ContentType`{.interpreted-text
        role="class"},
        `aiogram.enums.dice_emoji.DiceEmoji`{.interpreted-text
        role="class"},
        `aiogram.enums.inline_query_result_type.InlineQueryResultType`{.interpreted-text
        role="class"},
        `aiogram.enums.input_media_type.InputMediaType`{.interpreted-text
        role="class"},
        `aiogram.enums.mask_position_point.MaskPositionPoint`{.interpreted-text
        role="class"},
        `aiogram.enums.menu_button_type.MenuButtonType`{.interpreted-text
        role="class"},
        `aiogram.enums.message_entity_type.MessageEntityType`{.interpreted-text
        role="class"},
        `aiogram.enums.parse_mode.ParseMode`{.interpreted-text
        role="class"},
        `aiogram.enums.poll_type.PollType`{.interpreted-text
        role="class"},
        `aiogram.enums.sticker_type.StickerType`{.interpreted-text
        role="class"},
        `aiogram.enums.topic_icon_color.TopicIconColor`{.interpreted-text
        role="class"},
        `aiogram.enums.update_type.UpdateType`{.interpreted-text
        role="class"},

    **Added shortcuts**:

    -   

        *Chat* `aiogram.types.chat.Chat.get_administrators`{.interpreted-text role="meth"},

        :   `aiogram.types.chat.Chat.delete_message`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.revoke_invite_link`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.edit_invite_link`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.create_invite_link`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.export_invite_link`{.interpreted-text
            role="meth"}, `aiogram.types.chat.Chat.do`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.delete_sticker_set`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_sticker_set`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.get_member`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.get_member_count`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.leave`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.unpin_all_messages`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.unpin_message`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.pin_message`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_administrator_custom_title`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_permissions`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.promote`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.restrict`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.unban`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.ban`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_description`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_title`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.delete_photo`{.interpreted-text
            role="meth"},
            `aiogram.types.chat.Chat.set_photo`{.interpreted-text
            role="meth"},

    -   

        *Sticker*: `aiogram.types.sticker.Sticker.set_position_in_set`{.interpreted-text role="meth"},

        :   `aiogram.types.sticker.Sticker.delete_from_set`{.interpreted-text
            role="meth"},

    \- *User*:
    `aiogram.types.user.User.get_profile_photos`{.interpreted-text
    role="meth"} [#952](https://github.com/aiogram/aiogram/issues/952)

-   Added `callback answer <callback-answer-util>`{.interpreted-text
    role="ref"} feature
    [#1091](https://github.com/aiogram/aiogram/issues/1091)

-   Added a method that allows you to compactly register routers
    [#1117](https://github.com/aiogram/aiogram/issues/1117)

### Bugfixes

-   Check status code when downloading file
    [#816](https://github.com/aiogram/aiogram/issues/816)
-   Fixed [ignore_case]{.title-ref} parameter in
    `aiogram.filters.command.Command`{.interpreted-text role="obj"}
    filter [#1106](https://github.com/aiogram/aiogram/issues/1106)

### Misc

-   Added integration with new code-generator named
    [Butcher](https://github.com/aiogram/butcher)
    [#1069](https://github.com/aiogram/aiogram/issues/1069)

-   Added full support of [Bot API
    6.4](https://core.telegram.org/bots/api-changelog#december-30-2022)
    [#1088](https://github.com/aiogram/aiogram/issues/1088)

-   Updated package metadata, moved build internals from Poetry to
    Hatch, added contributing guides.
    [#1095](https://github.com/aiogram/aiogram/issues/1095)

-   Added full support of [Bot API
    6.5](https://core.telegram.org/bots/api-changelog#february-3-2023)

    ::: danger
    ::: title
    Danger
    :::

    Note that
    `aiogram.types.chat_permissions.ChatPermissions`{.interpreted-text
    role="obj"} is updated without backward compatibility, so now this
    object has no `can_send_media_messages` attribute
    :::

    [#1112](https://github.com/aiogram/aiogram/issues/1112)

-   Replaced error
    `TypeError: TelegramEventObserver.__call__() got an unexpected keyword argument '<name>'`
    with a more understandable one for developers and with a link to the
    documentation.
    [#1114](https://github.com/aiogram/aiogram/issues/1114)

-   Added possibility to reply into webhook with files
    [#1120](https://github.com/aiogram/aiogram/issues/1120)

-   Reworked graceful shutdown. Added method to stop polling. Now
    polling started from dispatcher can be stopped by signals gracefully
    without errors (on Linux and Mac).
    [#1124](https://github.com/aiogram/aiogram/issues/1124)

## 3.0.0b6 (2022-11-18)

### Features

-   (again) Added possibility to combine filters with an *and*/*or*
    operations.

    Read more in
    \"`Combining filters <combining-filters>`{.interpreted-text
    role="ref"}\" documentation section
    [#1018](https://github.com/aiogram/aiogram/issues/1018)

-   Added following methods to `Message` class:

    -   `Message.forward(...)`
    -   `Message.edit_media(...)`
    -   `Message.edit_live_location(...)`
    -   `Message.stop_live_location(...)`
    -   `Message.pin(...)`

    \- `Message.unpin()`
    [#1030](https://github.com/aiogram/aiogram/issues/1030)

-   Added following methods to `User` class:

    -   `User.mention_markdown(...)`

    \- `User.mention_html(...)`
    [#1049](https://github.com/aiogram/aiogram/issues/1049)

-   Added full support of [Bot API
    6.3](https://core.telegram.org/bots/api-changelog#november-5-2022)
    [#1057](https://github.com/aiogram/aiogram/issues/1057)

### Bugfixes

-   Fixed `Message.send_invoice` and `Message.reply_invoice`, added
    missing arguments
    [#1047](https://github.com/aiogram/aiogram/issues/1047)

-   Fixed copy and forward in:

    -   `Message.answer(...)`

    \- `Message.copy_to(...)`
    [#1064](https://github.com/aiogram/aiogram/issues/1064)

### Improved Documentation

-   Fixed UA translations in index.po
    [#1017](https://github.com/aiogram/aiogram/issues/1017)
-   Fix typehints for `Message`, `reply_media_group` and
    `answer_media_group` methods
    [#1029](https://github.com/aiogram/aiogram/issues/1029)
-   Removed an old now non-working feature
    [#1060](https://github.com/aiogram/aiogram/issues/1060)

### Misc

-   Enabled testing on Python 3.11
    [#1044](https://github.com/aiogram/aiogram/issues/1044)
-   Added a mandatory dependency `certifi` in due to in some cases on
    systems that doesn\'t have updated ca-certificates the requests to
    Bot API fails with reason
    `[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain`
    [#1066](https://github.com/aiogram/aiogram/issues/1066)

## 3.0.0b5 (2022-10-02)

### Features

-   Add PyPy support and run tests under PyPy
    [#985](https://github.com/aiogram/aiogram/issues/985)
-   Added message text to aiogram exceptions representation
    [#988](https://github.com/aiogram/aiogram/issues/988)
-   Added warning about using magic filter from
    [magic_filter]{.title-ref} instead of [aiogram]{.title-ref}\'s ones.
    Is recommended to use [from aiogram import F]{.title-ref} instead of
    [from magic_filter import F]{.title-ref}
    [#990](https://github.com/aiogram/aiogram/issues/990)
-   Added more detailed error when server response can\'t be
    deserialized. This feature will help to debug unexpected responses
    from the Server
    [#1014](https://github.com/aiogram/aiogram/issues/1014)

### Bugfixes

-   Reworked error event, introduced
    `aiogram.types.error_event.ErrorEvent`{.interpreted-text
    role="class"} object.
    [#898](https://github.com/aiogram/aiogram/issues/898)
-   Fixed escaping markdown in [aiogram.utils.markdown]{.title-ref}
    module [#903](https://github.com/aiogram/aiogram/issues/903)
-   Fixed polling crash when Telegram Bot API raises HTTP 429
    status-code. [#995](https://github.com/aiogram/aiogram/issues/995)
-   Fixed empty mention in command parsing, now it will be None instead
    of an empty string
    [#1013](https://github.com/aiogram/aiogram/issues/1013)

### Improved Documentation

-   Initialized Docs translation (added Ukrainian language)
    [#925](https://github.com/aiogram/aiogram/issues/925)

### Deprecations and Removals

-   Removed filters factory as described in corresponding issue.
    [#942](https://github.com/aiogram/aiogram/issues/942)

### Misc

-   Now Router/Dispatcher accepts only keyword arguments.
    [#982](https://github.com/aiogram/aiogram/issues/982)

## 3.0.0b4 (2022-08-14)

### Features

-   Add class helper ChatAction for constants that Telegram BotAPI uses
    in sendChatAction request. In my opinion, this will help users and
    will also improve compatibility with 2.x version where similar class
    was called \"ChatActions\".
    [#803](https://github.com/aiogram/aiogram/issues/803)

-   Added possibility to combine filters or invert result

    Example:

    ``` python
    Text(text="demo") | Command(commands=["demo"])
    MyFilter() & AnotherFilter()
    ~StateFilter(state='my-state')
    ```

    [#894](https://github.com/aiogram/aiogram/issues/894)

-   Fixed type hints for redis TTL params.
    [#922](https://github.com/aiogram/aiogram/issues/922)

-   Added [full_name]{.title-ref} shortcut for [Chat]{.title-ref} object
    [#929](https://github.com/aiogram/aiogram/issues/929)

### Bugfixes

-   Fixed false-positive coercing of Union types in API methods
    [#901](https://github.com/aiogram/aiogram/issues/901)

-   Added 3 missing content types:

    -   proximity_alert_triggered
    -   supergroup_chat_created

    \* channel_chat_created
    [#906](https://github.com/aiogram/aiogram/issues/906)

-   Fixed the ability to compare the state, now comparison to copy of
    the state will return [True]{.title-ref}.
    [#927](https://github.com/aiogram/aiogram/issues/927)

-   Fixed default lock kwargs in RedisEventIsolation.
    [#972](https://github.com/aiogram/aiogram/issues/972)

### Misc

-   Restrict including routers with strings
    [#896](https://github.com/aiogram/aiogram/issues/896)

-   Changed CommandPatterType to CommandPatternType in
    [aiogram/dispatcher/filters/command.py]{.title-ref}
    [#907](https://github.com/aiogram/aiogram/issues/907)

-   Added full support of [Bot API
    6.1](https://core.telegram.org/bots/api-changelog#june-20-2022)
    [#936](https://github.com/aiogram/aiogram/issues/936)

-   **Breaking!** More flat project structure

    These packages was moved, imports in your code should be fixed:

    -   `aiogram.dispatcher.filters` -\> `aiogram.filters`
    -   `aiogram.dispatcher.fsm` -\> `aiogram.fsm`
    -   `aiogram.dispatcher.handler` -\> `aiogram.handler`
    -   `aiogram.dispatcher.webhook` -\> `aiogram.webhook`

    \- `aiogram.dispatcher.flags/*` -\> `aiogram.dispatcher.flags`
    (single module instead of package)
    [#938](https://github.com/aiogram/aiogram/issues/938)

-   Removed deprecated `router.<event>_handler` and
    `router.register_<event>_handler` methods.
    [#941](https://github.com/aiogram/aiogram/issues/941)

-   Deprecated filters factory. It will be removed in next Beta (3.0b5)
    [#942](https://github.com/aiogram/aiogram/issues/942)

-   [MessageEntity]{.title-ref} method [get_text]{.title-ref} was
    removed and [extract]{.title-ref} was renamed to
    [extract_from]{.title-ref}
    [#944](https://github.com/aiogram/aiogram/issues/944)

-   Added full support of [Bot API
    6.2](https://core.telegram.org/bots/api-changelog#august-12-2022)
    [#975](https://github.com/aiogram/aiogram/issues/975)

## 3.0.0b3 (2022-04-19)

### Features

-   Added possibility to get command magic result as handler argument
    [#889](https://github.com/aiogram/aiogram/issues/889)
-   Added full support of [Telegram Bot API
    6.0](https://core.telegram.org/bots/api-changelog#april-16-2022)
    [#890](https://github.com/aiogram/aiogram/issues/890)

### Bugfixes

-   Fixed I18n lazy-proxy. Disabled caching.
    [#839](https://github.com/aiogram/aiogram/issues/839)
-   Added parsing of spoiler message entity
    [#865](https://github.com/aiogram/aiogram/issues/865)
-   Fixed default [parse_mode]{.title-ref} for
    [Message.copy_to()]{.title-ref} method.
    [#876](https://github.com/aiogram/aiogram/issues/876)
-   Fixed CallbackData factory parsing IntEnum\'s
    [#885](https://github.com/aiogram/aiogram/issues/885)

### Misc

-   Added automated check that pull-request adds a changes description
    to **CHANGES** directory
    [#873](https://github.com/aiogram/aiogram/issues/873)
-   Changed `Message.html_text` and `Message.md_text` attributes
    behaviour when message has no text. The empty string will be used
    instead of raising error.
    [#874](https://github.com/aiogram/aiogram/issues/874)
-   Used [redis-py]{.title-ref} instead of [aioredis]{.title-ref}
    package in due to this packages was merged into single one
    [#882](https://github.com/aiogram/aiogram/issues/882)
-   Solved common naming problem with middlewares that confusing too
    much developers
    \- now you can\'t see the [middleware]{.title-ref} and
    [middlewares]{.title-ref} attributes at the same point because this
    functionality encapsulated to special interface.
    [#883](https://github.com/aiogram/aiogram/issues/883)

## 3.0.0b2 (2022-02-19)

### Features

-   Added possibility to pass additional arguments into the aiohttp
    webhook handler to use this arguments inside handlers as the same as
    it possible in polling mode.
    [#785](https://github.com/aiogram/aiogram/issues/785)

-   Added possibility to add handler flags via decorator (like
    [pytest.mark]{.title-ref} decorator but [aiogram.flags]{.title-ref})
    [#836](https://github.com/aiogram/aiogram/issues/836)

-   Added `ChatActionSender` utility to automatically sends chat action
    while long process is running.

    It also can be used as message middleware and can be customized via
    `chat_action` flag.
    [#837](https://github.com/aiogram/aiogram/issues/837)

### Bugfixes

-   Fixed unexpected behavior of sequences in the StateFilter.
    [#791](https://github.com/aiogram/aiogram/issues/791)
-   Fixed exceptions filters
    [#827](https://github.com/aiogram/aiogram/issues/827)

### Misc

-   Logger name for processing events is changed to `aiogram.events`.
    [#830](https://github.com/aiogram/aiogram/issues/830)
-   Added full support of Telegram Bot API 5.6 and 5.7
    [#835](https://github.com/aiogram/aiogram/issues/835)
-   **BREAKING** Events isolation mechanism is moved from FSM storages
    to standalone managers
    [#838](https://github.com/aiogram/aiogram/issues/838)

## 3.0.0b1 (2021-12-12)

### Features

-   Added new custom operation for MagicFilter named `as_`

    Now you can use it to get magic filter result as handler argument

    ``` python
    from aiogram import F

    ...

    @router.message(F.text.regexp(r"^(\d+)$").as_("digits"))
    async def any_digits_handler(message: Message, digits: Match[str]):
        await message.answer(html.quote(str(digits)))


    @router.message(F.photo[-1].as_("photo"))
    async def download_photos_handler(message: Message, photo: PhotoSize, bot: Bot):
        content = await bot.download(photo)
    ```

    [#759](https://github.com/aiogram/aiogram/issues/759)

### Bugfixes

-   Fixed: Missing `ChatMemberHandler` import in
    `aiogram/dispatcher/handler`
    [#751](https://github.com/aiogram/aiogram/issues/751)

### Misc

-   Check `destiny` in case of no `with_destiny` enabled in RedisStorage
    key builder [#776](https://github.com/aiogram/aiogram/issues/776)
-   Added full support of [Bot API
    5.5](https://core.telegram.org/bots/api-changelog#december-7-2021)
    [#777](https://github.com/aiogram/aiogram/issues/777)
-   Stop using feature from #336. From now settings of client-session
    should be placed as initializer arguments instead of changing
    instance attributes.
    [#778](https://github.com/aiogram/aiogram/issues/778)
-   Make TelegramAPIServer files wrapper in local mode bi-directional
    (server-client, client-server) Now you can convert local path to
    server path and server path to local path.
    [#779](https://github.com/aiogram/aiogram/issues/779)

## 3.0.0a18 (2021-11-10)

### Features

-   Breaking: Changed the signature of the session middlewares Breaking:
    Renamed AiohttpSession.make_request method parameter from call to
    method to match the naming in the base class Added middleware for
    logging outgoing requests
    [#716](https://github.com/aiogram/aiogram/issues/716)

-   Improved description of filters resolving error. For example when
    you try to pass wrong type of argument to the filter but don\'t know
    why filter is not resolved now you can get error like this:

    ``` python3
    aiogram.exceptions.FiltersResolveError: Unknown keyword filters: {'content_types'}
      Possible cases:
      - 1 validation error for ContentTypesFilter
        content_types
          Invalid content types {'42'} is not allowed here (type=value_error)
    ```

    [#717](https://github.com/aiogram/aiogram/issues/717)

-   **Breaking internal API change** Reworked FSM Storage record keys
    propagation [#723](https://github.com/aiogram/aiogram/issues/723)

-   Implemented new filter named `MagicData(magic_data)` that helps to
    filter event by data from middlewares or other filters

    For example your bot is running with argument named `config` that
    contains the application config then you can filter event by value
    from this config:

    ``` python3
    @router.message(magic_data=F.event.from_user.id == F.config.admin_id)
    ...
    ```

    [#724](https://github.com/aiogram/aiogram/issues/724)

### Bugfixes

-   Fixed I18n context inside error handlers
    [#726](https://github.com/aiogram/aiogram/issues/726)
-   Fixed bot session closing before emit shutdown
    [#734](https://github.com/aiogram/aiogram/issues/734)
-   Fixed: bound filter resolving does not require children routers
    [#736](https://github.com/aiogram/aiogram/issues/736)

### Misc

-   Enabled testing on Python 3.10 Removed [async_lru]{.title-ref}
    dependency (is incompatible with Python 3.10) and replaced usage
    with protected property
    [#719](https://github.com/aiogram/aiogram/issues/719)

-   Converted README.md to README.rst and use it as base file for docs
    [#725](https://github.com/aiogram/aiogram/issues/725)

-   Rework filters resolving:

    -   Automatically apply Bound Filters with default values to
        handlers

    \- Fix data transfer from parent to included routers filters
    [#727](https://github.com/aiogram/aiogram/issues/727)

-   Added full support of Bot API 5.4
    <https://core.telegram.org/bots/api-changelog#november-5-2021>
    [#744](https://github.com/aiogram/aiogram/issues/744)

## 3.0.0a17 (2021-09-24)

### Misc

-   Added `html_text` and `md_text` to Message object
    [#708](https://github.com/aiogram/aiogram/issues/708)
-   Refactored I18n, added context managers for I18n engine and current
    locale [#709](https://github.com/aiogram/aiogram/issues/709)

## 3.0.0a16 (2021-09-22)

### Features

-   Added support of local Bot API server files downloading

    When Local API is enabled files can be downloaded via
    [bot.download]{.title-ref}/[bot.download_file]{.title-ref} methods.
    [#698](https://github.com/aiogram/aiogram/issues/698)

-   Implemented I18n & L10n support
    [#701](https://github.com/aiogram/aiogram/issues/701)

### Misc

-   Covered by tests and docs KeyboardBuilder util
    [#699](https://github.com/aiogram/aiogram/issues/699)

-   **Breaking!!!**. Refactored and renamed exceptions.

    -   Exceptions module was moved from `aiogram.utils.exceptions` to
        `aiogram.exceptions`

    \- Added prefix [Telegram]{.title-ref} for all error classes
    [#700](https://github.com/aiogram/aiogram/issues/700)

-   Replaced all `pragma: no cover` marks via global `.coveragerc`
    config [#702](https://github.com/aiogram/aiogram/issues/702)

-   Updated dependencies.

    **Breaking for framework developers** Now all optional dependencies
    should be installed as extra: [poetry install -E fast -E redis -E
    proxy -E i18n -E docs]{.title-ref}
    [#703](https://github.com/aiogram/aiogram/issues/703)

## 3.0.0a15 (2021-09-10)

### Features

-   Ability to iterate over all states in StatesGroup. Aiogram already
    had in check for states group so this is relative feature.
    [#666](https://github.com/aiogram/aiogram/issues/666)

### Bugfixes

-   Fixed incorrect type checking in the
    `aiogram.utils.keyboard.KeyboardBuilder`{.interpreted-text
    role="class"} [#674](https://github.com/aiogram/aiogram/issues/674)

### Misc

-   Disable ContentType filter by default
    [#668](https://github.com/aiogram/aiogram/issues/668)
-   Moved update type detection from Dispatcher to Update object
    [#669](https://github.com/aiogram/aiogram/issues/669)
-   Updated **pre-commit** config
    [#681](https://github.com/aiogram/aiogram/issues/681)
-   Reworked **handlers_in_use** util. Function moved to Router as
    method **.resolve_used_update_types()**
    [#682](https://github.com/aiogram/aiogram/issues/682)

## 3.0.0a14 (2021-08-17)

### Features

-   add aliases for edit/delete reply markup to Message
    [#662](https://github.com/aiogram/aiogram/issues/662)
-   Reworked outer middleware chain. Prevent to call many times the
    outer middleware for each nested router
    [#664](https://github.com/aiogram/aiogram/issues/664)

### Bugfixes

-   Prepare parse mode for InputMessageContent in AnswerInlineQuery
    method [#660](https://github.com/aiogram/aiogram/issues/660)

### Improved Documentation

-   Added integration with `towncrier`
    [#602](https://github.com/aiogram/aiogram/issues/602)

### Misc

-   Added [.editorconfig]{.title-ref}
    [#650](https://github.com/aiogram/aiogram/issues/650)
-   Redis storage speedup globals
    [#651](https://github.com/aiogram/aiogram/issues/651)
-   add allow_sending_without_reply param to Message reply aliases
    [#663](https://github.com/aiogram/aiogram/issues/663)
:::

.. Copy-pasted and reformatted from GitHub releases page

## 2.14.3 (2021-07-21)

-   Fixed `ChatMember` type detection via adding customizable object
    serialization mechanism
    ([#624](https://github.com/aiogram/aiogram/issues/624),
    [#623](https://github.com/aiogram/aiogram/issues/623))

## 2.14.2 (2021-07-26)

-   Fixed `MemoryStorage` cleaner
    ([#619](https://github.com/aiogram/aiogram/issues/619))
-   Fixed unused default locale in `I18nMiddleware`
    ([#562](https://github.com/aiogram/aiogram/issues/562),
    [#563](https://github.com/aiogram/aiogram/issues/563))

## 2.14 (2021-07-27)

-   Full support of Bot API 5.3
    ([#610](https://github.com/aiogram/aiogram/issues/610),
    [#614](https://github.com/aiogram/aiogram/issues/614))
-   Fixed `Message.send_copy` method for polls
    ([#603](https://github.com/aiogram/aiogram/issues/603))
-   Updated pattern for `GroupDeactivated` exception
    ([#549](https://github.com/aiogram/aiogram/issues/549)
-   Added `caption_entities` field in `InputMedia` base class
    ([#583](https://github.com/aiogram/aiogram/issues/583))
-   Fixed HTML text decorations for tag `pre`
    ([#597](https://github.com/aiogram/aiogram/issues/597) fixes issues
    [#596](https://github.com/aiogram/aiogram/issues/596) and
    [#481](https://github.com/aiogram/aiogram/issues/481))
-   Fixed `Message.get_full_command` method for messages with caption
    ([#576](https://github.com/aiogram/aiogram/issues/576))
-   Improved `MongoStorage`: remove documents with empty data from
    `aiogram_data` collection to save memory.
    ([#609](https://github.com/aiogram/aiogram/issues/609))

## 2.13 (2021-04-28)

-   Added full support of Bot API 5.2
    ([#572](https://github.com/aiogram/aiogram/issues/572))
-   Fixed usage of `provider_data` argument in `sendInvoice` method call
-   Fixed builtin command filter args
    ([#556](https://github.com/aiogram/aiogram/issues/556))
    ([#558](https://github.com/aiogram/aiogram/issues/558))
-   Allowed to use State instances FSM storage directly
    ([#542](https://github.com/aiogram/aiogram/issues/542))
-   Added possibility to get i18n locale without User instance
    ([#546](https://github.com/aiogram/aiogram/issues/546))
-   Fixed returning type of `Bot.*_chat_invite_link()` methods
    [#548](https://github.com/aiogram/aiogram/issues/548)
    ([#549](https://github.com/aiogram/aiogram/issues/549))
-   Fixed deep-linking util
    ([#569](https://github.com/aiogram/aiogram/issues/569))
-   Small changes in documentation - describe limits in docstrings
    corresponding to the current limit.
    ([#565](https://github.com/aiogram/aiogram/issues/565))
-   Fixed internal call to deprecated \'is_private\' method
    ([#553](https://github.com/aiogram/aiogram/issues/553))
-   Added possibility to use `allowed_updates` argument in Polling mode
    ([#564](https://github.com/aiogram/aiogram/issues/564))

## 2.12.1 (2021-03-22)

-   Fixed `TypeError: Value should be instance of 'User' not 'NoneType'`
    ([#527](https://github.com/aiogram/aiogram/issues/527))
-   Added missing `Chat.message_auto_delete_time` field
    ([#535](https://github.com/aiogram/aiogram/issues/535))
-   Added `MediaGroup` filter
    ([#528](https://github.com/aiogram/aiogram/issues/528))
-   Added `Chat.delete_message` shortcut
    ([#526](https://github.com/aiogram/aiogram/issues/526))
-   Added mime types parsing for `aiogram.types.Document`
    ([#431](https://github.com/aiogram/aiogram/issues/431))
-   Added warning in `TelegramObject.__setitem__` when Telegram adds a
    new field ([#532](https://github.com/aiogram/aiogram/issues/532))
-   Fixed `examples/chat_type_filter.py`
    ([#533](https://github.com/aiogram/aiogram/issues/533))
-   Removed redundant definitions in framework code
    ([#531](https://github.com/aiogram/aiogram/issues/531))

## 2.12 (2021-03-14)

-   Full support for Telegram Bot API 5.1
    ([#519](https://github.com/aiogram/aiogram/issues/519))
-   Fixed sending playlist of audio files and documents
    ([#465](https://github.com/aiogram/aiogram/issues/465),
    [#468](https://github.com/aiogram/aiogram/issues/468))
-   Fixed `FSMContextProxy.setdefault` method
    ([#491](https://github.com/aiogram/aiogram/issues/491))
-   Fixed `Message.answer_location` and `Message.reply_location` unable
    to send live location
    ([#497](https://github.com/aiogram/aiogram/issues/497))
-   Fixed `user_id` and `chat_id` getters from the context at Dispatcher
    `check_key`, `release_key` and `throttle` methods
    ([#520](https://github.com/aiogram/aiogram/issues/520))
-   Fixed `Chat.update_chat` method and all similar situations
    ([#516](https://github.com/aiogram/aiogram/issues/516))
-   Fixed `MediaGroup` attach methods
    ([#514](https://github.com/aiogram/aiogram/issues/514))
-   Fixed state filter for inline keyboard query callback in groups
    ([#508](https://github.com/aiogram/aiogram/issues/508),
    [#510](https://github.com/aiogram/aiogram/issues/510))
-   Added missing `ContentTypes.DICE`
    ([#466](https://github.com/aiogram/aiogram/issues/466))
-   Added missing vcard argument to `InputContactMessageContent`
    constructor ([#473](https://github.com/aiogram/aiogram/issues/473))
-   Add missing exceptions: `MessageIdInvalid`, `CantRestrictChatOwner`
    and `UserIsAnAdministratorOfTheChat`
    ([#474](https://github.com/aiogram/aiogram/issues/474),
    [#512](https://github.com/aiogram/aiogram/issues/512))
-   Added `answer_chat_action` to the `Message` object
    ([#501](https://github.com/aiogram/aiogram/issues/501))
-   Added dice to `message.send_copy` method
    ([#511](https://github.com/aiogram/aiogram/issues/511))
-   Removed deprecation warning from `Message.send_copy`
-   Added an example of integration between externally created aiohttp
    Application and aiogram
    ([#433](https://github.com/aiogram/aiogram/issues/433))
-   Added `split_separator` argument to `safe_split_text`
    ([#515](https://github.com/aiogram/aiogram/issues/515))
-   Fixed some typos in docs and examples
    ([#489](https://github.com/aiogram/aiogram/issues/489),
    [#490](https://github.com/aiogram/aiogram/issues/490),
    [#498](https://github.com/aiogram/aiogram/issues/498),
    [#504](https://github.com/aiogram/aiogram/issues/504),
    [#514](https://github.com/aiogram/aiogram/issues/514))

## 2.11.2 (2021-11-10)

-   Fixed default parse mode
-   Added missing \"supports_streaming\" argument to answer_video method
    [#462](https://github.com/aiogram/aiogram/issues/462)

## 2.11.1 (2021-11-10)

-   Fixed files URL template
-   Fix MessageEntity serialization for API calls
    [#457](https://github.com/aiogram/aiogram/issues/457)
-   When entities are set, default parse_mode become disabled
    ([#461](https://github.com/aiogram/aiogram/issues/461))
-   Added parameter supports_streaming to reply_video, remove redundant
    docstrings ([#459](https://github.com/aiogram/aiogram/issues/459))
-   Added missing parameter to promoteChatMember alias
    ([#458](https://github.com/aiogram/aiogram/issues/458))

## 2.11 (2021-11-08)

-   Added full support of Telegram Bot API 5.0
    ([#454](https://github.com/aiogram/aiogram/issues/454))

-   

    Added possibility to more easy specify custom API Server (example)

    :   -   WARNING: API method `close` was named in Bot class as
            close_bot in due to Bot instance already has method with the
            same name. It will be changed in `aiogram 3.0`

-   Added alias to Message object `Message.copy_to` with deprecation of
    `Message.send_copy`

-   `ChatType.SUPER_GROUP` renamed to `ChatType.SUPERGROUP`
    ([#438](https://github.com/aiogram/aiogram/issues/438))

## 2.10.1 (2021-09-14)

-   Fixed critical bug with getting asyncio event loop in executor.
    ([#424](https://github.com/aiogram/aiogram/issues/424))
    `AttributeError: 'NoneType' object has no attribute 'run_until_complete'`

## 2.10 (2021-09-13)

-   Breaking change: Stop using \_MainThread event loop in
    bot/dispatcher instances
    ([#397](https://github.com/aiogram/aiogram/issues/397))
-   Breaking change: Replaced aiomongo with motor
    ([#368](https://github.com/aiogram/aiogram/issues/368),
    [#380](https://github.com/aiogram/aiogram/issues/380))
-   Fixed: TelegramObject\'s aren\'t destroyed after update handling
    [#307](https://github.com/aiogram/aiogram/issues/307)
    ([#371](https://github.com/aiogram/aiogram/issues/371))
-   Add setting current context of Telegram types
    ([#369](https://github.com/aiogram/aiogram/issues/369))
-   Fixed markdown escaping issues
    ([#363](https://github.com/aiogram/aiogram/issues/363))
-   Fixed HTML characters escaping
    ([#409](https://github.com/aiogram/aiogram/issues/409))
-   Fixed italic and underline decorations when parse entities to
    Markdown
-   Fixed [#413](https://github.com/aiogram/aiogram/issues/413): parse
    entities positioning
    ([#414](https://github.com/aiogram/aiogram/issues/414))
-   Added missing thumb parameter
    ([#362](https://github.com/aiogram/aiogram/issues/362))
-   Added public methods to register filters and middlewares
    ([#370](https://github.com/aiogram/aiogram/issues/370))
-   Added ChatType builtin filter
    ([#356](https://github.com/aiogram/aiogram/issues/356))
-   Fixed IDFilter checking message from channel
    ([#376](https://github.com/aiogram/aiogram/issues/376))
-   Added missed answer_poll and reply_poll
    ([#384](https://github.com/aiogram/aiogram/issues/384))
-   Added possibility to ignore message caption in commands filter
    ([#383](https://github.com/aiogram/aiogram/issues/383))
-   Fixed addStickerToSet method
-   Added preparing thumb in send_document method
    ([#391](https://github.com/aiogram/aiogram/issues/391))
-   Added exception MessageToPinNotFound
    ([#404](https://github.com/aiogram/aiogram/issues/404))
-   Fixed handlers parameter-spec solving
    ([#408](https://github.com/aiogram/aiogram/issues/408))
-   Fixed CallbackQuery.answer() returns nothing
    ([#420](https://github.com/aiogram/aiogram/issues/420))
-   CHOSEN_INLINE_RESULT is a correct API-term
    ([#415](https://github.com/aiogram/aiogram/issues/415))
-   Fixed missing attributes for Animation class
    ([#422](https://github.com/aiogram/aiogram/issues/422))
-   Added missed emoji argument to reply_dice
    ([#395](https://github.com/aiogram/aiogram/issues/395))
-   Added is_chat_creator method to ChatMemberStatus
    ([#394](https://github.com/aiogram/aiogram/issues/394))
-   Added missed ChatPermissions to \_\_all\_\_
    ([#393](https://github.com/aiogram/aiogram/issues/393))
-   Added is_forward method to Message
    ([#390](https://github.com/aiogram/aiogram/issues/390))
-   Fixed usage of deprecated is_private function
    ([#421](https://github.com/aiogram/aiogram/issues/421))

and many others documentation and examples changes:

-   Updated docstring of RedisStorage2
    ([#423](https://github.com/aiogram/aiogram/issues/423))
-   Updated I18n example (added docs and fixed typos)
    ([#419](https://github.com/aiogram/aiogram/issues/419))
-   A little documentation revision
    ([#381](https://github.com/aiogram/aiogram/issues/381))
-   Added comments about correct errors_handlers usage
    ([#398](https://github.com/aiogram/aiogram/issues/398))
-   Fixed typo rexex -\> regex
    ([#386](https://github.com/aiogram/aiogram/issues/386))
-   Fixed docs Quick start page code blocks
    ([#417](https://github.com/aiogram/aiogram/issues/417))
-   fixed type hints of callback_data
    ([#400](https://github.com/aiogram/aiogram/issues/400))
-   Prettify readme, update downloads stats badge
    ([#406](https://github.com/aiogram/aiogram/issues/406))

## 2.9.2 (2021-06-13)

-   Fixed `Message.get_full_command()`
    [#352](https://github.com/aiogram/aiogram/issues/352)
-   Fixed markdown util
    [#353](https://github.com/aiogram/aiogram/issues/353)

## 2.9 (2021-06-08)

-   Added full support of Telegram Bot API 4.9
-   Fixed user context at poll_answer update
    ([#322](https://github.com/aiogram/aiogram/issues/322))
-   Fix Chat.set_description
    ([#325](https://github.com/aiogram/aiogram/issues/325))
-   Add lazy session generator
    ([#326](https://github.com/aiogram/aiogram/issues/326))
-   Fix text decorations
    ([#315](https://github.com/aiogram/aiogram/issues/315),
    [#316](https://github.com/aiogram/aiogram/issues/316),
    [#328](https://github.com/aiogram/aiogram/issues/328))
-   Fix missing `InlineQueryResultPhoto` `parse_mode` field
    ([#331](https://github.com/aiogram/aiogram/issues/331))
-   Fix fields from parent object in `KeyboardButton`
    ([#344](https://github.com/aiogram/aiogram/issues/344) fixes
    [#343](https://github.com/aiogram/aiogram/issues/343))
-   Add possibility to get bot id without calling `get_me`
    ([#296](https://github.com/aiogram/aiogram/issues/296))

## 2.8 (2021-04-26)

-   Added full support of Bot API 4.8
-   Added `Message.answer_dice` and `Message.reply_dice` methods
    ([#306](https://github.com/aiogram/aiogram/issues/306))

## 2.7 (2021-04-07)

-   Added full support of Bot API 4.7
    ([#294](https://github.com/aiogram/aiogram/issues/294)
    [#289](https://github.com/aiogram/aiogram/issues/289))
-   Added default parse mode for send_animation method
    ([#293](https://github.com/aiogram/aiogram/issues/293)
    [#292](https://github.com/aiogram/aiogram/issues/292))
-   Added new API exception when poll requested in public chats
    ([#270](https://github.com/aiogram/aiogram/issues/270))
-   Make correct User and Chat get_mention methods
    ([#277](https://github.com/aiogram/aiogram/issues/277))
-   Small changes and other minor improvements

## 2.6.1 (2021-01-25)

-   Fixed reply `KeyboardButton` initializer with `request_poll`
    argument ([#266](https://github.com/aiogram/aiogram/issues/266))
-   Added helper for poll types (`aiogram.types.PollType`)
-   Changed behavior of Telegram_object `.as_*` and `.to_*` methods. It
    will no more mutate the object.
    ([#247](https://github.com/aiogram/aiogram/issues/247))

## 2.6 (2021-01-23)

-   Full support of Telegram Bot API v4.6 (Polls 2.0)
    [#265](https://github.com/aiogram/aiogram/issues/265)
-   Aded new filter - IsContactSender (commit)
-   Fixed proxy extra dependencies version
    [#262](https://github.com/aiogram/aiogram/issues/262)

## 2.5.3 (2021-01-05)

-   [#255](https://github.com/aiogram/aiogram/issues/255) Updated
    CallbackData factory validity check. More correct for non-latin
    symbols
-   [#256](https://github.com/aiogram/aiogram/issues/256) Fixed
    `renamed_argument` decorator error
-   [#257](https://github.com/aiogram/aiogram/issues/257) One more fix
    of CommandStart filter

## 2.5.2 (2021-01-01)

-   Get back `quote_html` and `escape_md` functions

## 2.5.1 (2021-01-01)

-   Hot-fix of `CommandStart` filter

## 2.5 (2021-01-01)

-   Added full support of Telegram Bot API 4.5
    ([#250](https://github.com/aiogram/aiogram/issues/250),
    [#251](https://github.com/aiogram/aiogram/issues/251))
-   [#239](https://github.com/aiogram/aiogram/issues/239) Fixed
    `check_token` method
-   [#238](https://github.com/aiogram/aiogram/issues/238),
    [#241](https://github.com/aiogram/aiogram/issues/241): Added
    deep-linking utils
-   [#248](https://github.com/aiogram/aiogram/issues/248) Fixed support
    of aiohttp-socks
-   Updated setup.py. No more use of internal pip API
-   Updated links to documentations (<https://docs.aiogram.dev>)
-   Other small changes and minor improvements
    ([#223](https://github.com/aiogram/aiogram/issues/223) and
    others\...)

## 2.4 (2021-10-29)

-   Added Message.send_copy method (forward message without forwarding)
-   Safe close of aiohttp client session (no more exception when
    application is shutdown)
-   No more \"adWanced\" words in project
    [#209](https://github.com/aiogram/aiogram/issues/209)
-   Arguments user and chat is renamed to user_id and chat_id in
    Dispatcher.throttle method
    [#196](https://github.com/aiogram/aiogram/issues/196)
-   Fixed set_chat_permissions
    [#198](https://github.com/aiogram/aiogram/issues/198)
-   Fixed Dispatcher polling task does not process cancellation
    [#199](https://github.com/aiogram/aiogram/issues/199),
    [#201](https://github.com/aiogram/aiogram/issues/201)
-   Fixed compatibility with latest asyncio version
    [#200](https://github.com/aiogram/aiogram/issues/200)
-   Disabled caching by default for lazy_gettext method of
    I18nMiddleware [#203](https://github.com/aiogram/aiogram/issues/203)
-   Fixed HTML user mention parser
    [#205](https://github.com/aiogram/aiogram/issues/205)
-   Added IsReplyFilter
    [#210](https://github.com/aiogram/aiogram/issues/210)
-   Fixed send_poll method arguments
    [#211](https://github.com/aiogram/aiogram/issues/211)
-   Added OrderedHelper
    [#215](https://github.com/aiogram/aiogram/issues/215)
-   Fix incorrect completion order.
    [#217](https://github.com/aiogram/aiogram/issues/217)

## 2.3 (2021-08-16)

-   Full support of Telegram Bot API 4.4
-   Fixed [#143](https://github.com/aiogram/aiogram/issues/143)
-   Added new filters from issue
    [#151](https://github.com/aiogram/aiogram/issues/151):
    [#172](https://github.com/aiogram/aiogram/issues/172),
    [#176](https://github.com/aiogram/aiogram/issues/176),
    [#182](https://github.com/aiogram/aiogram/issues/182)
-   Added expire argument to RedisStorage2 and other storage fixes
    [#145](https://github.com/aiogram/aiogram/issues/145)
-   Fixed JSON and Pickle storages
    [#138](https://github.com/aiogram/aiogram/issues/138)
-   Implemented MongoStorage
    [#153](https://github.com/aiogram/aiogram/issues/153) based on
    aiomongo (soon motor will be also added)
-   Improved tests
-   Updated examples
-   Warning: Updated auth widget util.
    [#190](https://github.com/aiogram/aiogram/issues/190)
-   Implemented throttle decorator
    [#181](https://github.com/aiogram/aiogram/issues/181)

## 2.2 (2021-06-09)

-   Provides latest Telegram Bot API (4.3)
-   Updated docs for filters
-   Added opportunity to use different bot tokens from single bot
    instance (via context manager,
    [#100](https://github.com/aiogram/aiogram/issues/100))
-   IMPORTANT: Fixed Typo: `data` -\> `bucket` in `update_bucket` for
    RedisStorage2
    ([#132](https://github.com/aiogram/aiogram/issues/132))

## 2.1 (2021-04-18)

-   Implemented all new features from Telegram Bot API 4.2
-   `is_member` and `is_admin` methods of `ChatMember` and
    `ChatMemberStatus` was renamed to `is_chat_member` and
    `is_chat_admin`
-   Remover func filter
-   Added some useful Message edit functions (`Message.edit_caption`,
    `Message.edit_media`, `Message.edit_reply_markup`)
    ([#121](https://github.com/aiogram/aiogram/issues/121),
    [#103](https://github.com/aiogram/aiogram/issues/103),
    [#104](https://github.com/aiogram/aiogram/issues/104),
    [#112](https://github.com/aiogram/aiogram/issues/112))
-   Added requests timeout for all methods
    ([#110](https://github.com/aiogram/aiogram/issues/110))
-   Added `answer*` methods to `Message` object
    ([#112](https://github.com/aiogram/aiogram/issues/112))
-   Maked some improvements of `CallbackData` factory
-   Added deep-linking parameter filter to `CommandStart` filter
-   Implemented opportunity to use DNS over socks
    ([#97](https://github.com/aiogram/aiogram/issues/97) -\>
    [#98](https://github.com/aiogram/aiogram/issues/98))
-   Implemented logging filter for extending LogRecord attributes (Will
    be usefull with external logs collector utils like GrayLog, Kibana
    and etc.)
-   Updated `requirements.txt` and `dev_requirements.txt` files
-   Other small changes and minor improvements

## 2.0.1 (2021-12-31)

-   Implemented CallbackData factory
    ([example](https://github.com/aiogram/aiogram/blob/master/examples/callback_data_factory.py))
-   Implemented methods for answering to inline query from context and
    reply with animation to the messages.
    [#85](https://github.com/aiogram/aiogram/issues/85)
-   Fixed installation from tar.gz
    [#84](https://github.com/aiogram/aiogram/issues/84)
-   More exceptions (`ChatIdIsEmpty` and `NotEnoughRightsToRestrict`)

## 2.0 (2021-10-28)

This update will break backward compability with Python 3.6 and works
only with Python 3.7+: - contextvars (PEP-567); - New syntax for
annotations (PEP-563).

Changes: - Used contextvars instead of `aiogram.utils.context`; -
Implemented filters factory; - Implemented new filters mechanism; -
Allowed to customize command prefix in CommandsFilter; - Implemented
mechanism of passing results from filters (as dicts) as kwargs in
handlers (like fixtures in pytest); - Implemented states group
feature; - Implemented FSM storage\'s proxy; - Changed files uploading
mechanism; - Implemented pipe for uploading files from URL; -
Implemented I18n Middleware; - Errors handlers now should accept only
two arguments (current update and exception); - Used `aiohttp_socks`
instead of `aiosocksy` for Socks4/5 proxy; - types.ContentType was
divided to `types.ContentType` and `types.ContentTypes`; - Allowed to
use rapidjson instead of ujson/json; - `.current()` method in bot and
dispatcher objects was renamed to `get_current()`;

Full changelog - You can read more details about this release in
migration FAQ:
<https://aiogram.readthedocs.io/en/latest/migration_1_to_2.html>

## 1.4 (2021-08-03)

-   Bot API 4.0 ([#57](https://github.com/aiogram/aiogram/issues/57))

## 1.3.3 (2021-07-16)

-   Fixed markup-entities parsing;
-   Added more API exceptions;
-   Now InlineQueryResultLocation has live_period;
-   Added more message content types;
-   Other small changes and minor improvements.

## 1.3.2 (2021-05-27)

-   Fixed crashing of polling process. (i think)
-   Added parse_mode field into input query results according to Bot API
    Docs.
-   Added new methods for Chat object.
    ([#42](https://github.com/aiogram/aiogram/issues/42),
    [#43](https://github.com/aiogram/aiogram/issues/43))
-   **Warning**: disabled connections limit for bot aiohttp session.
-   **Warning**: Destroyed \"temp sessions\" mechanism.
-   Added new error types.
-   Refactored detection of error type.
-   Small fixes of executor util.
-   Fixed RethinkDBStorage

## 1.3.1 (2018-05-27)

## 1.3 (2021-04-22)

-   Allow to use Socks5 proxy (need manually install `aiosocksy`).
-   Refactored `aiogram.utils.executor` module.
-   **\[Warning\]** Updated requirements list.

## 1.2.3 (2018-04-14)

-   Fixed API errors detection
-   Fixed compability of `setup.py` with pip 10.0.0

## 1.2.2 (2018-04-08)

-   Added more error types.
-   Implemented method `InputFile.from_url(url: str)` for downloading
    files.
-   Implemented big part of API method tests.
-   Other small changes and mminor improvements.

## 1.2.1 (2018-03-25)

-   Fixed handling Venue\'s
    \[[#27](https://github.com/aiogram/aiogram/issues/27),
    [#26](https://github.com/aiogram/aiogram/issues/26)\]
-   Added parse_mode to all medias (Bot API 3.6 support)
    \[[#23](https://github.com/aiogram/aiogram/issues/23)\]
-   Now regexp filter can be used with callback query data
    \[[#19](https://github.com/aiogram/aiogram/issues/19)\]
-   Improvements in `InlineKeyboardMarkup` & `ReplyKeyboardMarkup`
    objects \[[#21](https://github.com/aiogram/aiogram/issues/21)\]
-   Other bug & typo fixes and minor improvements.

## 1.2 (2018-02-23)

-   Full provide Telegram Bot API 3.6
-   Fixed critical error:
    `Fatal Python error: PyImport_GetModuleDict: no module dictionary!`
-   Implemented connection pool in RethinkDB driver
-   Typo fixes of documentstion
-   Other bug fixes and minor improvements.

## 1.1 (2018-01-27)

-   Added more methods for data types (like `message.reply_sticker(...)`
    or `file.download(...)`
-   Typo fixes of documentstion
-   Allow to set default parse mode for messages
    (`Bot( ... , parse_mode='HTML')`)
-   Allowed to cancel event from the
    `Middleware.on_pre_process_<event type>`
-   Fixed sending files with correct names.
-   Fixed MediaGroup
-   Added RethinkDB storage for FSM
    (`aiogram.contrib.fsm_storage.rethinkdb`)

## 1.0.4 (2018-01-10)

## 1.0.3 (2018-01-07)

-   Added middlewares mechanism.
-   Added example for middlewares and throttling manager.
-   Added logging middleware
    (`aiogram.contrib.middlewares.logging.LoggingMiddleware`)
-   Fixed handling errors in async tasks (marked as \'async_task\')
-   Small fixes and other minor improvements.

## 1.0.2 (2017-11-29)

## 1.0.1 (2017-11-21)

-   Implemented `types.InputFile` for more easy sending local files
-   **Danger!** Fixed typo in word pooling. Now whatever all methods
    with that word marked as deprecated and original methods is renamed
    to polling. Check it in you\'r code before updating!
-   Fixed helper for chat actions (`types.ChatActions`)
-   Added
    [example](https://github.com/aiogram/aiogram/blob/master/examples/media_group.py)
    for media group.

## 1.0 (2017-11-19)

-   Remaked data types serialozation/deserialization mechanism (Speed
    up).
-   Fully rewrited all Telegram data types.
-   Bot object was fully rewritted (regenerated).
-   Full provide Telegram Bot API 3.4+ (with sendMediaGroup)
-   Warning: Now `BaseStorage.close()` is awaitable! (FSM)
-   Fixed compability with uvloop.
-   More employments for `aiogram.utils.context`.
-   Allowed to disable `ujson`.
-   Other bug fixes and minor improvements.
-   Migrated from Bitbucket to Github.

## 0.4.1 (2017-08-03)

## 0.4 (2017-08-05)

## 0.3.4 (2017-08-04)

## 0.3.3 (2017-07-05)

## 0.3.2 (2017-07-04)

## 0.3.1 (2017-07-04)

## 0.2b1 (2017-06-00)

## 0.1 (2017-06-03)
