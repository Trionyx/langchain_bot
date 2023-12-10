# MagicData

## Usage

1.  `MagicData(F.event.from_user.id == F.config.admin_id)` (Note that
    `config` should be passed from middleware)

## Explanation

::: {.autoclass members="" member-order="bysource" undoc-members="False"}
aiogram.filters.magic_data.MagicData
:::

Can be imported:

-   `from aiogram.filters import MagicData`

## Allowed handlers

Allowed update types for this filter:

-   `message`
-   `edited_message`
-   `channel_post`
-   `edited_channel_post`
-   `inline_query`
-   `chosen_inline_result`
-   `callback_query`
-   `shipping_query`
-   `pre_checkout_query`
-   `poll`
-   `poll_answer`
-   `my_chat_member`
-   `chat_member`
-   `chat_join_request`
-   `error`
