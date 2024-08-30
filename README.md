# rdf-embedder

`rdf-embedder` is a Python tool that processes Turtle files to add embeddings for long text fields. It uses `rdflib` for handling RDF data and `sentence-transformers` to generate embeddings for text fields that exceed a specified character length.

## Features

- Reads RDF data from a Turtle file.
- Identifies text fields in the RDF graph that exceed a specified character length.
- Generates embeddings for these text fields using a Sentence Transformer model.
- Adds the generated embeddings to the RDF graph as new nodes.
- Outputs the modified RDF graph to a new Turtle file.

## Installation

1. Clone the repository:

```bash
   git clone https://github.com/david4096/rdf-embedder
   cd rdf-embedder
```

Install the required dependencies:

```bash

pip install -r requirements.txt
```

Alternatively, you can use setup.py to install:

```bash

    pip install .

```

## Usage

After installation, you can use the rdf-embedder command-line tool:

```bash

rdf-embedder input_file.ttl output_file.ttl --model sentence-transformers/all-MiniLM-L6-v2 --char-threshold 100
```

Command-line Arguments


    input_file: Path to the input Turtle file containing RDF data.
    output_file: Path to the output Turtle file where the modified RDF data will be saved.
    --model: (Optional) The Sentence Transformer model to use for generating embeddings. Default is sentence-transformers/all-MiniLM-L6-v2.
    --char-threshold: (Optional) The character length threshold for creating embeddings. Text fields with a length greater than this value will be processed. Default is 100.

Example

To process a Turtle file named example.ttl and save the output to output.ttl, using the default model and a character threshold of 100:

```bash

rdf-embedder example.ttl output.ttl

```

To use a different model and a different character threshold:

```bash

rdf-embedder example.ttl output.ttl --model sentence-transformers/paraphrase-MiniLM-L6-v2 --char-threshold 50

```

## Development

To contribute to the development of this tool, clone the repository and install the dependencies in a virtual environment.

```bash

git clone https://github.com/yourusername/embedding_processor.git
cd embedding_processor
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

```

## License

This project is licensed under the MIT License. See the LICENSE file for details.