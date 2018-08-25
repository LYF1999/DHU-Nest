### DHU NEST
东华小窝

启动

#### Start

- pipenv 安装 https://pipenv.readthedocs.io/en/latest/install/
- docker 安装 https://docs.docker.com/


- `pipenv install`
- `docker-compose -f  docker-compose.dev.yaml up`
- `pipenv run python manage.py migrate` 数据库建表(只在当数据库变动的时候需要运行)
- `pipenv run python manage.py runserver` 启动
