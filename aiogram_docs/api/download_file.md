# How to download file?

## Download file manually

First, you must get the [file_id]{.title-ref} of the file you want to
download. Information about files sent to the bot is contained in
[Message](types/message.html).

For example, download the document that came to the bot.

``` 
file_id = message.document.file_id
```

Then use the [getFile](methods/get_file.html) method to get
[file_path]{.title-ref}.

``` 
file = await bot.get_file(file_id)
file_path = file.file_path
```

After that, use the [download_file](#download-file) method from the bot
object.

### download_file(\...)

Download file by [file_path]{.title-ref} to destination.

If you want to automatically create destination
(`io.BytesIO`{.interpreted-text role="obj"}) use default value of
destination and handle result of this method.

::: automethod
aiogram.client.bot.Bot.download_file
:::

There are two options where you can download the file: to **disk** or to
**binary I/O object**.

### Download file to disk

To download file to disk, you must specify the file name or path where
to download the file. In this case, the function will return nothing.

``` 
await bot.download_file(file_path, "text.txt")
```

### Download file to binary I/O object

To download file to binary I/O object, you must specify an object with
the `typing.BinaryIO`{.interpreted-text role="obj"} type or use the
default (`None`{.interpreted-text role="obj"}) value.

In the first case, the function will return your object:

``` 
my_object = MyBinaryIO()
result: MyBinaryIO = await bot.download_file(file_path, my_object)
# print(result is my_object)  # True
```

If you leave the default value, an `io.BytesIO`{.interpreted-text
role="obj"} object will be created and returned.

``` 
result: io.BytesIO = await bot.download_file(file_path)
```

## Download file in short way

Getting [file_path]{.title-ref} manually every time is boring, so you
should use the [download](#download) method.

### download(\...)

Download file by [file_id]{.title-ref} or [Downloadable]{.title-ref}
object to destination.

If you want to automatically create destination
(`io.BytesIO`{.interpreted-text role="obj"}) use default value of
destination and handle result of this method.

::: automethod
aiogram.client.bot.Bot.download
:::

It differs from [download_file](#download-file) **only** in that it
accepts [file_id]{.title-ref} or an [Downloadable]{.title-ref} object
(object that contains the [file_id]{.title-ref} attribute) instead of
[file_path]{.title-ref}.

You can download a file to [disk](#download-file-to-disk) or to a
[binary I/O](#download-file-to-binary-io-object) object in the same way.

Example:

``` 
document = message.document
await bot.download(document)
```
