## MariaDB

Lên [https://mariadb.org/](https://mariadb.org/) xem hướng dẫn cài + chạy

Sau khi chạy được, import SQL file ở 'db/db.sql' vào database

chạy mariadbd.exe --console

## Tạo virtual env + chạy server

Mở cmd ở 'WebTimViec' chạy lần lượt

```bash
1> python -m venv jobsite-server
2> cd jobsite-server
```

Trên Windows chạy

```bash
3> Scripts\activate.bat
```

Trên Linux chạy 

```bash
3> source bin\activate
```

Tiếp tục chạy

```bash
4> pip install -r requirements.txt
5> cd jobsite
5> python manage.py runserver
```

## APIs

Login Google

```http
http://localhost:8000/api/login-google
```

- Method:             POST

- Payload:             Google Oauth2.0 response

- Response:          { 'token' : <token>, 'user_info' : <info> }

Test Login Google

```http
http://localhost:8000/api/test-auth
```

- Method:             GET

- Authorization:   token lấy bằng API bên trên

- Response:          text

Register

```http
http://localhost:8000/api/register
```

+ Method: POST

+ 

+ Response: giống với Google login bên trên
