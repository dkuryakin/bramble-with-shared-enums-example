build-patched-bramble:
	git clone git@github.com:dkuryakin/bramble.git patched-bramble || true && \
	cd patched-bramble && \
	git pull && \
	docker build -t bramble .

up:
	docker-compose up --build --remove-orphans --force-recreate -d

down:
	docker-compose down

test1:
	curl -sX POST http://localhost:8080/query \
     -H "Content-Type: application/json" \
     -d '{"query": "{ permission1 }"}' | jq

test2:
	curl -sX POST http://localhost:8080/query \
     -H "Content-Type: application/json" \
     -d '{"query": "{ permission2 }"}' | jq

test: up test1 test2 down