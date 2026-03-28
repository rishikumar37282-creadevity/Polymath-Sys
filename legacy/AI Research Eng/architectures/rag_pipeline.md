# RAG Pipeline Architecture

This document outlines the standard architecture for a Retrieval-Augmented Generation (RAG) system, as covered in **Phase 1: Foundations** and expanded in **Phase 2: Deep AI**.

## Core System Flow

The RAG pipeline solves the "hallucination problem" by forcing the Large Language Model to construct its answer strictly from retrieved knowledge context rather than relying on its parametric memory.

```mermaid
graph TD
    classDef user fill:#1a5c1a,stroke:#3c933c,stroke-width:2px,color:#fff;
    classDef process fill:#174ea6,stroke:#4a82da,stroke-width:2px,color:#fff;
    classDef model fill:#5a1b7a,stroke:#8a4bAa,stroke-width:2px,color:#fff;
    classDef db fill:#8b1a1a,stroke:#cb4a4a,stroke-width:2px,color:#fff;

    subgraph Data Ingestion
        Doc[Private Documents] --> Chunk(Text Splitter)
        Chunk --> Embed[Embedding Model]
        Embed --> VDB[(Vector Database)]
        class Doc,Chunk process
        class Embed model
        class VDB db
    end

    subgraph Retrieval Generation
        User((User Query)) --> QueryEmbed[Embedding Model]
        QueryEmbed --> Search{Similarity Search}
        VDB -.-> Search
        Search --> Context[Retrieved Chunks]
        User --> Prompt[LLM Prompt Builder]
        Context --> Prompt
        Prompt --> LLM{Large Language Model}
        LLM --> Response((Final Answer))
        
        class User,Response user
        class QueryEmbed,LLM model
        class Search,Context,Prompt process
    end
```

## Key Components

1. **Document Loader & Splitter:** Handles messy inputs (PDFs, Markdown, raw text). Chunks text into manageable overlaps (e.g., 1000 tokens with 200 token overlap) to preserve context boundaries.
2. **Embedding Model:** Transforms text chunks into high-dimensional vectors. (e.g., `text-embedding-ada-002` or open-source `bge-large-en`).
3. **Vector Database:** Specialized data store (like ChromaDB, Pinecone, or FAISS) optimized for fast Approximate Nearest Neighbors (ANN) searches.
4. **LLM Synthesis:** The retrieved contexts are prepended to the user query with strict instructions to "answer only using the provided context."
