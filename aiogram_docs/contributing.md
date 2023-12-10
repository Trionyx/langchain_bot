# Contributing

You\'re welcome to contribute to aiogram!

*aiogram* is an open-source project, and anyone can contribute to it in
any possible way

## Developing

Before making any changes in the framework code, it is necessary to fork
the project and clone the project to your PC and know how to do a
pull-request.

How to work with pull-request you can read in the [GitHub
docs](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

Also in due to this project is written in Python, you will need Python
to be installed (is recommended to use latest Python versions, but any
version starting from 3.8 can be used)

### Use virtualenv

You can create a virtual environment in a directory using `venv` module
(it should be pre-installed by default):

``` bash
python -m venv .venv
```

This action will create a `.venv` directory with the Python binaries and
then you will be able to install packages into that isolated
environment.

### Activate the environment

Linux / macOS:

``` bash
source .venv/bin/activate
```

Windows cmd

``` text
.\.venv\Scripts\activate
```

Windows PowerShell

``` powershell
.\.venv\Scripts\activate.ps1
```

To check it worked, use described command, it should show the `pip`
version and location inside the isolated environment

``` 
pip -V
```

Also make sure you have the latest pip version in your virtual
environment to avoid errors on next steps:

``` 
python -m pip install --upgrade pip
```

### Setup project

After activating the environment install [aiogram]{.title-ref} from
sources and their dependencies.

Linux / macOS:

``` bash
pip install -e ."[dev,test,docs,fast,redis,proxy,i18n]"
```

Windows:

``` bash
pip install -e .[dev,test,docs,fast,redis,proxy,i18n]
```

It will install `aiogram` in editable mode into your virtual environment
and all dependencies.

### Making changes in code

At this point you can make any changes in the code that you want, it can
be any fixes, implementing new features or experimenting.

### Format the code (code-style)

Note that this project is Black-formatted, so you should follow that
code-style, too be sure You\'re correctly doing this let\'s reformat the
code automatically:

``` bash
black aiogram tests examples
isort aiogram tests examples
```

### Run tests

All changes should be tested:

``` bash
pytest tests
```

Also if you are doing something with Redis-storage, you will need to
test everything works with Redis:

``` bash
pytest --redis redis://<host>:<port>/<db> tests
```

### Docs

We are using [Sphinx]{.title-ref} to render docs in different languages,
all sources located in [docs]{.title-ref} directory, you can change the
sources and to test it you can start live-preview server and look what
you are doing:

``` bash
sphinx-autobuild --watch aiogram/ docs/ docs/_build/
```

### Docs translations

Translation of the documentation is very necessary and cannot be done
without the help of the community from all over the world, so you are
welcome to translate the documentation into different languages.

Before start, let\'s up to date all texts:

``` bash
cd docs
make gettext
sphinx-intl update -p _build/gettext -l <language_code>
```

Change the `<language_code>` in example below to the target language
code, after that you can modify texts inside
`docs/locale/<language_code>/LC_MESSAGES` as `*.po` files by using any
text-editor or specialized utilites for GNU Gettext, for example via
[poedit](https://poedit.net/).

To view results:

``` bash
sphinx-autobuild --watch aiogram/ docs/ docs/_build/ -D language=<language_code>
```

### Describe changes

Describe your changes in one or more sentences so that bot developers
know what\'s changed in their favorite framework - create
[\<code\>.\<category\>.rst]{.title-ref} file and write the description.

`<code>` is Issue or Pull-request number, after release link to this
issue will be published to the *Changelog* page.

`<category>` is a changes category marker, it can be one of:

-   `feature` - when you are implementing new feature
-   `bugfix` - when you fix a bug
-   `doc` - when you improve the docs
-   `removal` - when you remove something from the framework
-   `misc` - when changed something inside the Core or project
    configuration

If you have troubles with changing category feel free to ask
Core-contributors to help with choosing it.

### Complete

After you have made all your changes, publish them to the repository and
create a pull request as mentioned at the beginning of the article and
wait for a review of these changes.

## Star on GitHub

You can \"star\" repository on GitHub -
<https://github.com/aiogram/aiogram> (click the star button at the top
right)

Adding stars makes it easier for other people to find this project and
understand how useful it is.

## Guides

You can write guides how to develop Bots on top of aiogram and publish
it into YouTube, Medium, GitHub Books, any Courses platform or any other
platform that you know.

This will help more people learn about the framework and learn how to
use it

## Take answers

The developers is always asks for any question in our chats or any other
platforms like GitHub Discussions, StackOverflow and others, feel free
to answer to this questions.

## Funding

The development of the project is free and not financed by commercial
organizations, it is my personal initiative
([\@JRootJunior](https://t.me/JRootJunior)) and I am engaged in the
development of the project in my free time.

So, if you want to financially support the project, or, for example,
give me a pizza or a beer, you can do it on
[OpenCollective](https://opencollective.com/aiogram).
