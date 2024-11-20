# Fast Api Crud With JWT

Url demo [Here](https://fastapi-example-zkqn.onrender.com/docs)

This is to get the token or you can create a new user:
<p>email: vlzdavid12@outlook.com</p>
<p>password: 123456</p>

<p>For the app to work correctly, it is necessary to insert products with their category and brand.</p>

## Brand Body
```
{
  "name": "Toto"
}

```
## Category Body
```
{
  "name": "Accesorios"
}
```
## Product Body
<p>Please remember to insert the products as required. Keep in mind that since this is a free server, the provider periodically deletes temporary data stored in the SQLite database.</p>

```
{
  "name": "Maleta Totto",
  "description": "Esta es una linda maleta totto",
  "category_id": 1,
  "brand_id": 1,
  "price": 2.5,
  "rating": 2.5
}
```




## Set Up a Virtual Environment
```
pip install virtualenv

# On Linux/macOS
python3 -m venv venv

# On Windows
python -m venv venv

```
## Activate the virtual environment:

```
# On Linux/macOS
source venv/bin/activate

# On Windows
venv\Scripts\activate
```

## Install Dependencies

```
pip install -r requirements.txt
```

## Run
```
uvicorn main:app --reload
```
