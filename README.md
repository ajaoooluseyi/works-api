# Works-api
Its the backend structure for an Arist database.

## Description
it has Clent(User), Artist and Work tables in the database. The links to access the APIs are:

* http://127.0.0.1:8000/api/works : To access all objects in the Work table. 
* http://127.0.0.1:8000/api/works?artist=[Artist Name] : To search database throught Artist name.
* http://127.0.0.1:8000/api/works?work_type=Youtube or pk of YouTube : To search database throught Work type.
* http://127.0.0.1:8000/api/register : To register a new user.

### Dependencies
* Django
* Django rest framework 
* Windows 10
* Python version 3.10.6 


### Executing program

* In the projects' working directory execute the below command to create a virtual environment for our project. Virtual environments make it easier to manage packages for various projects separately.

 
```python
$ py -m venv venv
```

To activate the virtual environment, execute the below command.

```python
$ source venv/Scripts/activate
```
Clone this repository in the projects' working directory by executing the command below.

```python
$ git clone https://github.com/ajaoooluseyi/works-api.git
$ cd works_api
```

* Install all the required dependencies
```python
$ pip install -r requirements.txt
```

This api uses restframework.permissions for Authentication.
* Superuser
 username = admin
 password = admin

* Sample User login
username = testuser
password = pass123123
```

