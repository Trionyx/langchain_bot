# Documentation helper bot
It will help you find the right answer based on your documentation.

1. Install poetry:

```python
pip install poetry
```

2. Install dependencies:

```python
poetry install
```

3. Add your OpenAI key to your environment variables

4. Create the Chroma DB:

```python
python create_database.py
```

5. Ask bot a question about your documentation in the console:

```python
python main.py
```

TODO: 
1. add aiogram examples from documentation to the database
2. add TG bot to not use console
