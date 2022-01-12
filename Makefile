environment = development
development_env_file = environment/development.env
production_env_file = environment/production.env

.PHONY: \
	build \
	run \
	env \
	check-envs \
	check-env

run: check-env
	@docker-compose build --no-cache --force-rm nginx
	@if [ "$(shell readlink .env)" = "$(production_env_file)" ]; then\
		docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d;\
	else\
		docker-compose up -d;\
	fi

build:
	python3 build.py
	@echo "Successfully built"

env: check-envs
	@if [ "$(environment)" = "development" -o "$(environment)" = "production" ]; then\
		cat environment/$(environment).env > .env;\
		echo "Environment set up as $(environment)";\
		exit 0;\
	else\
		echo "Usage: make env environment=[development|production]";\
		exit 1;\
	fi

check-envs:
	@if [ ! -f $(production_env_file) ] || [ ! -f $(development_env_file) ]; then\
		echo "One or more environment files are absent. Chech 'environment/' directory.";\
		exit 1;\
	fi

check-env:
	@if [ ! -f .env ] ; then\
		echo "File .env doesn't exist. Run 'make env environment=<your_environment>' first.";\
		exit 1;\
	fi
