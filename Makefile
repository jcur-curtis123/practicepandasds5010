# Reference for make: https://www.gnu.org/software/make/

# Use this .PHONY line if have a directory named "data" and you want to use "make data"
# Ref: https://www.gnu.org/software/make/manual/html_node/Phony-Targets.html

figure: pull_data
	python3 src/driver.py

figure_verbose: pull_data
	python3 src/driver.py verbose

pull_data:
	mkdir -p data
	cd data && curl -LO https://github.com/ds5110/rdata/raw/main/data/Wage.csv

clean:
	rm data/Wage.csv
	rmdir data


boxplot:
	python3 src/driver.py box

# added scatterplot for makefile
scatterplot:
	python3 src/driver.py scatter
# added line plot for makefile 
lineplot:
	python3 src/driver.py line

reset: clean
	rm figures/*.png

setup_prereqs:
	pip install --upgrade pip
	pip install -r requirements.txt

set_up: setup_prereqs
	echo "done"
