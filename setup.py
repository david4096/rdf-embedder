from setuptools import setup, find_packages

setup(
    name='embedding_processor',
    version='0.1',
    description='A tool for processing Turtle files and adding embeddings for long text fields.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'rdflib>=6.0.0',
        'sentence-transformers>=2.0.0',
    ],
    entry_points={
        'console_scripts': [
            'rdf-embedder=rdf_embedder.embedding_processor:main',
        ],
    },
    python_requires='>=3.6',
)