[![DOI](https://zenodo.org/badge/794177493.svg)](https://zenodo.org/doi/10.5281/zenodo.11094042)

# Elastic Search

## Project overview

This is the repository for a minimal producible solution of a elastic search setup. 

The aim of this exercise is to improve a minimum viable search engine, such that it returns the right documents for predefined user queries.

## Data

The data contains around 25.000 crawled Wikipedia pages of English-speaking movies from 2000 until today. The data has been collected by the code found in the [wiki](ir_exercise/wiki) folder.

The sample-data provided in the ir_exercise directory shows the artificially created sample data.

## Start the search engine system

### Prerequisites

You need an elasticsearch up and running on your machine. For details about how to install, set up and start elasticsearch, see [here](ES_SETUP.md).

You have to install the necessary python packages. For details, see [here](PYTHON_SETUP.md).

### Download the data

Use the [preprocessor](ir_exercise/preprocessor.py) code to download and save the data onto your machine.

```bash
# With downloading the data
python ir_exercise/preprocessor.py -d

# Without downloading the data
python ir_exercise/preprocessor.py
```

This creates a [data](data) folder with a [data.json](data/data.json) file in it, which serves as input for the [indexer](ir_exercise/indexer.py).

### Run the indexer

Run the [indexer](ir_exercise/indexer.py) code to create and populate an elasticsearch index.

```bash
# If we want to delete and recreate the indices
python ir_exercise/indexer.py -r

# If you only want to update the indices
python ir_exercise/indexer.py
```

### Start the search engine

You can start the service from terminal. Leave this service running and execute the other commands from a new terminal.

```bash
python ir_exercise/search_service.py
```

You can send request via `curl`, e.g.:
```bash
# Linux
curl -X GET http://localhost:6000/ir-search-service -H "Content-Type: application/json" -d '{"text": "test queary", "size": 5}'

# Windows
curl -X GET http://localhost:6000/ir-search-service -H "Content-Type: application/json" -d "{\"text\": \"test queary\", \"size\": 5}"
```

### (Optional) Start frontend

We also provide a simple `streamlit` frontend that prints the top 10 hits for a search query.

```bash
streamlit run ir_exercise/frontend.py
```

The website will be automatically opened in your browser, or you can reach it manually under http://localhost:8501/. 

## Debug Elasticsearch with Kibana Dev Tools

Kibana provides a quick way of querying your elasticsearch cluster. For details about how to setup and use it, see [here](KIBANA.md).

It is recommended to use Kibana.

## Run tests

The test can be found in the [test](ir_exercise/test) folder. They can be executed from command line, or if you are using an IDE (e.g. PyCharm), you can also execute them within the IDE (in case of PyCharm by clicking the green play buttons).

Failed tests come with detailed logs, i.e. the query sent to the server and the documents retrieved by the server. You can copy and paste these queries to kibana and play around with modifications.

### All tests

```bash
pytest
```

### Pre-task

```bash
pytest ir_exercise/test/test_pre_task.py
```

### Milestone 1

```bash
pytest ir_exercise/test/test_milestone_1.py
```

### Milestone 2

```bash
# Only milestone 2 tests
pytest ir_exercise/test/test_milestone_2.py

# But beware, for milestone 2, all tests will be assessed
pytest ir_exercise/test/test_milestone_*.py
````

### Specific tests

```bash
# All tests from a test class
pytest ir_exercise/test/test_milestone_1.py -k TroyTest

# Only one test
pytest ir_exercise/test/test_milestone_1.py::TroyTest::test_top_1
```

## Troubleshooting

If you encounter some troubles with elasticsearch, check [this](TROUBLESHOOTING.md) document for possible solutions.

## (Optional) Code formatting

The requirements also install [black](https://github.com/psf/black), a common python code formatter.

Possible usages (you can do none or also all of them):
- Run it manually from the console by calling `black .` from the root folder or to a specific file.
- Set your IDE to format your code by using black.
  - e.g. for PyCharm: 
    - Settings -> Tools -> External Tools -> click the "+" icon
    - Name: `Black`
    - Description: `Black in PyCharm configuration`
    - Program: `<path_to_black>`, you can find it out by calling `which black`
    - Arguments: `--config pyproject.toml $FilePath$`
    - Working directory: `$ProjectFileDir$`
- Set up a pre-commit hook by calling `pre-commit install`. This creates the `.git/hooks/pre-commit` file, which automatically reformats all the modified files prior to any commit.
