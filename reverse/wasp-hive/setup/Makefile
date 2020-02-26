all: compile

compile:
	emcc -s WASM=1  -s EXPORTED_FUNCTIONS="['_check']" -o static/validator.js *.c -s EXTRA_EXPORTED_RUNTIME_METHODS='["ccall", "cwrap"]'