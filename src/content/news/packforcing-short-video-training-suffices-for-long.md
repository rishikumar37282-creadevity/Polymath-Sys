---
title: "PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference"
pubDate: 2026-03-26
description: "Autoregressive video diffusion models have demonstrated remarkable progress, yet they remain bottlenecked by intractable linear KV-cache growth, temporal repetition, and compounding errors during long..."
author: "Xiaofeng Mao"
link: "http://arxiv.org/abs/2603.25730v1"
tags: ["Research", "Paper"]
---

Autoregressive video diffusion models have demonstrated remarkable progress, yet they remain bottlenecked by intractable linear KV-cache growth, temporal repetition, and compounding errors during long-video generation. To address these challenges, we present PackForcing, a unified framework that efficiently manages the generation history through a novel three-partition KV-cache strategy. Specifically, we categorize the historical context into three distinct types: (1) Sink tokens, which preserve early anchor frames at full resolution to maintain global semantics; (2) Mid tokens, which achieve a massive spatiotemporal compression (32x token reduction) via a dual-branch network fusing progressive 3D convolutions with low-resolution VAE re-encoding; and (3) Recent tokens, kept at full resolution to ensure local temporal coherence. To strictly bound the memory footprint without sacrificing quality, we introduce a dynamic top-$k$ context selection mechanism for the mid tokens, coupled with a continuous Temporal RoPE Adjustment that seamlessly re-aligns position gaps caused by dropped tokens with negligible overhead. Empowered by this principled hierarchical context compression, PackForcing can generate coherent 2-minute, 832x480 videos at 16 FPS on a single H200 GPU. It achieves a bounded KV cache of just 4 GB and enables a remarkable 24x temporal extrapolation (5s to 120s), operating effectively either zero-shot or trained on merely 5-second clips. Extensive results on VBench demonstrate state-of-the-art temporal consistency (26.07) and dynamic degree (56.25), proving that short-video supervision is sufficient for high-quality, long-video synthesis. https://github.com/ShandaAI/PackForcing

[Read full paper at ArXiv](http://arxiv.org/abs/2603.25730v1)
