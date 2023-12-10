# Media group builder

This module provides a builder for media groups, it can be used to build
media groups for
`aiogram.types.input_media_photo.InputMediaPhoto`{.interpreted-text
role="class"},
`aiogram.types.input_media_video.InputMediaVideo`{.interpreted-text
role="class"},
`aiogram.types.input_media_document.InputMediaDocument`{.interpreted-text
role="class"} and
`aiogram.types.input_media_audio.InputMediaAudio`{.interpreted-text
role="class"}.

::: warning
::: title
Warning
:::

`aiogram.types.input_media_animation.InputMediaAnimation`{.interpreted-text
role="class"} is not supported yet in the Bot API to send as media
group.
:::

## Usage

``` python
media_group = MediaGroupBuilder(caption="Media group caption")

# Add photo
media_group.add_photo(media="https://picsum.photos/200/300")
# Dynamically add photo with known type without using separate method
media_group.add(type="photo", media="https://picsum.photos/200/300")
# ... or video
media_group.add(type="video", media=FSInputFile("media/video.mp4"))
```

To send media group use
`aiogram.methods.send_media_group.SendMediaGroup`{.interpreted-text
role="meth"} method, but when you use
`aiogram.utils.media_group.MediaGroupBuilder`{.interpreted-text
role="class"} you should pass `media` argument as `media_group.build()`.

If you specify `caption` in
`aiogram.utils.media_group.MediaGroupBuilder`{.interpreted-text
role="class"} it will be used as `caption` for first media in group.

``` python
await bot.send_media_group(chat_id=chat_id, media=media_group.build())
```

## References

::: {.autoclass members=""}
aiogram.utils.media_group.MediaGroupBuilder
:::
