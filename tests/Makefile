all: tests

tests: test-init.test test-new.test

%.test: %.py
	python3 $^ && touch $@ 

clean:
	rm *.test
