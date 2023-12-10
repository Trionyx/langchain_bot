# How to upload file? {#sending-files}

As says [official Telegram Bot API
documentation](https://core.telegram.org/bots/api#sending-files) there
are three ways to send files (photos, stickers, audio, media, etc.):

If the file is already stored somewhere on the Telegram servers or file
is available by the URL, you don\'t need to reupload it.

But if you need to upload a new file just use subclasses of
[InputFile](types/input_file.html).

Here are the three different available builtin types of input file:

-   `aiogram.types.input_file.FSInputFile`{.interpreted-text
    role="class"} - [uploading from file
    system](#upload-from-file-system)
-   `aiogram.types.input_file.BufferedInputFile`{.interpreted-text
    role="class"} - [uploading from buffer](#upload-from-buffer)
-   `aiogram.types.input_file.URLInputFile`{.interpreted-text
    role="class"} - [uploading from URL](#upload-from-url)

::: warning
::: title
Warning
:::

**Be respectful with Telegram**

Instances of [InputFile]{.title-ref} are reusable. That\'s mean you can
create instance of InputFile and sent this file multiple times but
Telegram does not recommend to do that and when you upload file once
just save their [file_id]{.title-ref} and use it in next times.
:::

## Upload from file system

By first step you will need to import InputFile wrapper:

``` 
from aiogram.types import FSInputFile
```

Then you can use it:

``` 
cat = FSInputFile("cat.png")
agenda = FSInputFile("my-document.pdf", filename="agenda-2019-11-19.pdf")
```

::: {.autoclass members="__init__"}
aiogram.types.input_file.FSInputFile
:::

## Upload from buffer

Files can be also passed from buffer (For example you generate image
using [Pillow](https://pillow.readthedocs.io/en/stable/) and you want to
send it to Telegram):

Import wrapper:

``` 
from aiogram.types import BufferedInputFile
```

And then you can use it:

``` 
text_file = BufferedInputFile(b"Hello, world!", filename="file.txt")
```

::: {.autoclass members="__init__"}
aiogram.types.input_file.BufferedInputFile
:::

## Upload from url

If you need to upload a file from another server, but the direct link is
bound to your server\'s IP, or you want to bypass native [upload
limits](https://core.telegram.org/bots/api#sending-files) by URL, you
can use `aiogram.types.input_file.URLInputFile`{.interpreted-text
role="obj"}.

Import wrapper:

``` 
from aiogram.types import URLInputFile
```

And then you can use it:

``` 
image = URLInputFile(
    "https://www.python.org/static/community_logos/python-powered-h-140x182.png",
    filename="python-logo.png"
)
```

::: {.autoclass members=""}
aiogram.types.input_file.URLInputFile
:::
