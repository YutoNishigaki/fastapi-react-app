COMPOSE := docker-compose -f docker-compose.yml

.PHONY: build up rebuild

build:
	$(COMPOSE) build

up:
	$(COMPOSE) up -d

down:
	$(COMPOSE) down

# コンテナ再作成
rebuild: down build up
