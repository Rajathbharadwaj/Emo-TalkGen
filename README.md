
# Emo-TalkGen

Evaluating Multimodal Synthesis for Emotionally Expressive Talking Head
Generation using Diffusion models and 3DMM



## Problem Statement

This thesis explores a novel dual-decoder architecture integrated with 3D Morphable Models (3DMM) for talking head video generation. One decoder targets the nuanced facial dynamics influenced by emotional and contextual cues, while the other focuses on the precise synchronization of lip movements and expressions linked to spoken audio. This architecture is designed to test whether separating these aspects into dual decoders can enhance the coherence and lifelikeness of talking head animations beyond traditional single-decoder systems. Additionally, this approach aims to assess how the separate processing of audio cues and facial geometry could improve the fidelity and emotional expressiveness of the animations. The effectiveness of this innovative system in real-world scenarios remains a key area of research, with a focus on its potential to deliver more realistic and emotionally resonant talking head videos.


### Inputs

- Audio Cues: Direct speech features such as tone, pitch, and pace, processed to control lip synchronization and basic facial expressions.

- Facial Dynamics Data: Emotional and contextual cues, along with 3DMM parameters, are processed to influence broader facial expressions, subtle movements, and precise geometric adjustments.


### Output
- Video Frames: A sequence of video frames depicting a talking head, where the performance in terms of lip-sync accuracy, nuanced facial expressions, and geometric precision is evaluated against established benchmarks.

This study seeks not only to understand the baseline performance of the dual-decoder and 3DMM integration but also to investigate whether the architecture's distinct separation of facial dynamics and geometry processing can yield improvements in emotional expressiveness and realism compared to conventional single-decoder systems.


## Proposed Architecture & Methodology

![Architecture](https://github.com/Rajathbharadwaj/Emo-TalkGen/blob/main/architecture.png)

## Progress

[x] Implementation

[] Experiments

[] Readings

