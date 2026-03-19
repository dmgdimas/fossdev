.PHONY: another-app
# might be correct, but "build" and "app" are difference
build:
	gcc main.c -o app
# correct no Phony
app: main.c
	gcc main.c -o app
# incorrect: listed in phony
another-app: main.c
	gcc main.c -o another-app
