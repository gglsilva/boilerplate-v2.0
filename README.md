# boilerplate-v2.0

## Run Development config
- .env
> DJANGO_SETTINGS_MODULE=config.settings.development
- docker 
> docker-compose up --build


## Run Production config
- .env
> DJANGO_SETTINGS_MODULE=config.settings.production
- docker
> docker-compose -f docker-compose.prod.yml up --build
