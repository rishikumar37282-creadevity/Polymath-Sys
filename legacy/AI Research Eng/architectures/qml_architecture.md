# Variational Quantum Circuit (QML) Architecture

This document breaks down the core component of Quantum Machine Learning (QML): the Hybrid Classical-Quantum network using a Parameterized Quantum Circuit (PQC), central to **Phase 3: The Frontier**.

## Variational Quantum Eigensolver / Classifier

A Variational Quantum Circuit acts as a machine learning model where mathematical parameters (like angles in rotation gates) are optimized classically, but evaluated quantumly.

```mermaid
graph TD
    classDef classical fill:#1a5c1a,stroke:#3c933c,stroke-width:2px,color:#fff;
    classDef quantum fill:#5a1b7a,stroke:#8a4bAa,stroke-width:2px,color:#fff;
    classDef measure fill:#174ea6,stroke:#4a82da,stroke-width:2px,color:#fff;
    classDef optim fill:#8b1a1a,stroke:#cb4a4a,stroke-width:2px,color:#fff;

    Data((Classical Data X)) --> Encode[Data Encoding / Feature Map]
    
    subgraph "QPU (Quantum Processing Unit)"
        Encode --> Init(|0...0> State Prep)
        Init --> PQC{Parameterized Quantum Circuit U(θ)}
        PQC --> Meas[Measurement Z / Expectation Value]
    end
    
    subgraph "CPU (Classical Processing Unit)"
        Meas --> Loss[Loss Function Evaluation]
        Loss --> Grad[Gradient Calculation]
        Grad --> Optimizer(Classical Optimizer: Adam/SGD)
        Optimizer -. "Updates parameters θ" .-> PQC
    end

    class Data classical
    class Init,PQC quantum
    class Encode,Meas measure
    class Loss,Grad,Optimizer optim
```

## The Quantum Gradient (Parameter-Shift Rule)
Unlike classical backpropagation, quantum circuits must be evaluated on hardware. To calculate the gradient of a quantum parameter θ, QML avoids finite-difference approximations by using the precise **Parameter Shift Rule**:

`∇f(θ) = c * [ f(θ + s) - f(θ - s) ]`

The gradient is exact, evaluated by running the same circuit twice with parameters shifted forward and backward by a macroscopic constant `s`.
