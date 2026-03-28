# The Transformer Architecture

This document visually breaks down the Transformer architecture, the foundational model of modern AI, as explored in **Phase 2: Deep AI (Let's build GPT)**.

## Core Encoder-Decoder Flow

First proposed in the 2017 paper *"Attention Is All You Need"*, the transformer removed recurrent layers entirely, relying exclusively on an attention mechanism to model global dependencies.

```mermaid
graph LR
    classDef input fill:#1a5c1a,stroke:#3c933c,stroke-width:2px,color:#fff;
    classDef block fill:#174ea6,stroke:#4a82da,stroke-width:2px,color:#fff;
    classDef attention fill:#5a1b7a,stroke:#8a4bAa,stroke-width:2px,color:#fff;
    classDef feedfw fill:#8b1a1a,stroke:#cb4a4a,stroke-width:2px,color:#fff;

    subgraph "Encoder Block (N layers)"
        Inp[Input Embeddings] --> Pos[Positional Encoding]
        Pos --> MHA1(Multi-Head Self-Attention)
        MHA1 --> AddNorm1((Add & Norm))
        AddNorm1 --> FFN1(Feed Forward Network)
        FFN1 --> AddNorm2((Add & Norm))
    end

    subgraph "Decoder Block (N layers)"
        Out[Output Embeddings] --> Pos2[Positional Encoding]
        Pos2 --> MMHA(Masked Multi-Head Attention)
        MMHA --> AddNorm3((Add & Norm))
        AddNorm2 -. "Key / Value" .-> CA(Cross-Attention)
        AddNorm3 -. "Query" .-> CA
        CA --> AddNorm4((Add & Norm))
        AddNorm4 --> FFN2(Feed Forward Network)
        FFN2 --> AddNorm5((Add & Norm))
        AddNorm5 --> Linear[Linear Layer]
        Linear --> Softmax[Softmax Probabilities]
    end

    class Inp,Out,Pos,Pos2 input
    class MHA1,MMHA,CA attention
    class AddNorm1,AddNorm2,AddNorm3,AddNorm4,AddNorm5 block
    class FFN1,FFN2,Linear,Softmax feedfw
```

## Attention Mechanism (Scaled Dot-Product)
At the heart of the transformer is the self-attention formula:
`Attention(Q, K, V) = softmax( (Q·K^T) / sqrt(d_k) ) V`

- **Q (Query):** What the current token is looking for.
- **K (Key):** What information the token holds.
- **V (Value):** The actual information.
- The dot product between Query and Key determines the "attention score" or relevance between any two tokens in the sequence.
