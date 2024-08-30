import argparse
import logging
import rdflib
from rdflib.namespace import RDF, RDFS, XSD
from rdflib.term import Literal, BNode
from rdflib.collection import Collection
from sentence_transformers import SentenceTransformer

# URIs defined at the top of the file
EMBEDDING_URI = rdflib.URIRef("http://example.org/embedding")
TEXT_NODE_URI = rdflib.URIRef("http://example.org/text")

"""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sc: <https://schema.org/>

SELECT DISTINCT ?b ?f ?i WHERE {
    ?a <http://example.org/text> ?b.
    ?a <http://example.org/embedding> ?d.
    ?d <http://www.w3.org/1999/02/22-rdf-syntax-ns#first> ?f.
    ?d <http://www.w3.org/1999/02/22-rdf-syntax-ns#rest> ?g.
    ?g ?h ?i.
    FILTER NOT EXISTS { ?g ?h <http://www.w3.org/1999/02/22-rdf-syntax-ns#nil> }
}


PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix sc: <https://schema.org/>
PREFIX  list: <http://jena.hpl.hp.com/ARQ/list#>

SELECT ?ds ?meta ?longtext ?val WHERE {
    ?ds ?meta ?longtext.
    ?collection <http://example.org/text> ?longtext.
    ?collection <http://example.org/embedding> ?headnode.
    ?headnode rdf:rest*/rdf:first ?val
  FILTER NOT EXISTS {?ds <http://example.org/text> ?longtext}
}



"""

def create_embeddings(graph, model_name, char_threshold):
    """
    Create embeddings for text fields in the graph
    that exceed a specified character length.
    """
    logging.info(f"Loading model {model_name}...")
    #model = SentenceTransformer(model_name)

    for s, p, o in graph.triples((None, None, None)):
        if isinstance(o, rdflib.Literal) and o.datatype == XSD.string and len(o) > char_threshold:
            logging.info(f"Creating embedding for: {p} {o}")

            # Generate embedding
            #embedding_vector = model.encode(str(o)).tolist()
            embedding_vector = [0.2, 0.1, 0.3]  # Example fixed embedding vector for demonstration

            # Create a new blank node to represent the text node with embedding
            text_node = BNode()

            # Link the text node to the literal
            graph.add((text_node, TEXT_NODE_URI, o))

            # Convert embedding vector to RDF list (collection)
            collection_node = BNode()
            collection = Collection(graph, collection_node)

            for value in embedding_vector:
                # Ensure each element is typed as a float
                collection.append(Literal(value, datatype=XSD.float))

            # Link the text node to the embedding collection
            graph.add((text_node, EMBEDDING_URI, collection_node))

    logging.info("Embedding creation complete.")

def main():
    parser = argparse.ArgumentParser(description="Process a Turtle file and create embeddings.")
    parser.add_argument("input_file", type=str, help="Input Turtle file")
    parser.add_argument("output_file", type=str, help="Output Turtle file")
    parser.add_argument("--model", type=str, default="sentence-transformers/all-MiniLM-L6-v2",
                        help="Sentence Transformer model to use")
    parser.add_argument("--char-threshold", type=int, default=100,
                        help="Character length threshold for creating embeddings")

    args = parser.parse_args()

    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting RDF Embedder")

    # Load RDF graph
    graph = rdflib.Graph()
    graph.parse(args.input_file, format="turtle")

    create_embeddings(graph, args.model, args.char_threshold)

    # Serialize output
    graph.serialize(destination=args.output_file, format="turtle")
    logging.info(f"Output written to {args.output_file}")

if __name__ == "__main__":
    main()
