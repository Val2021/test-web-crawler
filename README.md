
# 🚀 Web Crawler Project URL Given

Project elaborated with the objective to make a crawler in a given url and in the other urls associated to the initial url making a crawler to a certain depth. This depth is used as a stop criteria  to the crawler.
<br>
The version of python used for development was Python 3.8
<br>
The version of docker used for development was Docker 20.10.12

## 🛠 Preparing the project
### Prerequisites::
- [Python 3.8](https://www.python.org/)
- [Docker version 20.10.12](https://www.docker.com/)

### Cloning the repository
    https://github.com/Val2021/test-web-crawler.git


### Running application (Linux):
    make

### Creating virtual environment (Windows):
    python3 -m venv virtual_environment_name

### Activate virtual environment  (Windows):

    virtual_environment_name\Scripts\ActivateDependencies

### Install project dependencies with the command (Windows):
    pip install -r requirements.txt

### Running application (Windows):
    docker-compose up --build

### Running tests:
    pytest

### Running lint:
    pre-commit run -a
    

## 🎲 Running the back end (server)
    ...

### Features
- [x] web crawler of a certain site

## 🚀 Deploy
    Docker
    
## Database tool:
   Dbeaver
##

👀 Note:
    If you are using Dbeaver as database tool or other one, use  these setting:
    <br>
    url => varchar(1000)
<div align="center">
    <img src="https://user-images.githubusercontent.com/63678413/199476593-d934cf79-d10f-467d-ba30-dbff6df837ab.png" width=1000px" />
</div>
<br>
The "visited" field receives the boolean value equals false:
<div align="center">
    <img src="https://user-images.githubusercontent.com/63678413/199476437-9f8eacb5-bda0-47d2-bb63-bcf21c35da63.png" width=1000px" />
</div>
<br>
Use the query to clear the table:
<div align="center">
    <img src="https://user-images.githubusercontent.com/63678413/199476502-b25cf6a1-b760-48bb-ae60-8b6bc901b3c8.png" width=1000px" />
</div>
<br>
Contributors:
<table>
  <tr>
    <td align="center">
        <a href="https://github.com/Val2021">
        <img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63678413?v=4" width="100px;" alt=""/>
        <br /><sub><b>Val Araújo</b></sub></a><br />
    </td>
  </tr>
</table>
