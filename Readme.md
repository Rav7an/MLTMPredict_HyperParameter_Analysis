# Experiment Analysis: DNA Sequence Encoding Strategies

This experiment builds upon the work in [MLTMPredict](https://github.com/v-h-gn/MLTMPredict) and utilizes the codebase from that repository as a foundation.

## Purpose
The primary objective of this experiment is to evaluate the impact of different encoding methods (specifically `average` vs. `pad`) and vector dimensions on the accuracy of a DNA Melting Temperature prediction model trained using an XGBoost regressor.

## Sequence Representation
The core challenge lies in how variable-length DNA sequences are represented numerically before being used as input features for the machine learning model.

Consider the following two sequences:
- **Sequence 1:** `ATCGGA` (Length: 6)
- **Sequence 2:** `AATG` (Length: 4)

Using a 3-gram (trigram) model, these sequences are decomposed as follows:
- **Sequence 1:** `ATC`, `TCG`, `CGG`, `GGA` (4 subsequences)
- **Sequence 2:** `AAT`, `ATG` (2 subsequences)

This creates a dimensionality mismatch: Sequence 1 has 4 components, while Sequence 2 has only 2. Standard machine learning models typically require fixed-size input vectors.

## Encoding Strategies
To address this, we define a function $R$ that maps subsequences to numerical vectors (Same approach in the BioVec paper). We explore two distinct strategies to handle the variable lengths:

### 1. Average Pooling
In this method, the vectors of all subsequences are averaged to produce a single fixed-size vector.

*Example (assuming Vector Dimension = 3):*
- **Seq 1:** `[1,1,1], [2,2,2], [3,3,3], [4,4,4]` $\rightarrow$ Average $\rightarrow$ `[2.5, 2.5, 2.5]`
- **Seq 2:** `[5,5,5], [6,6,6]` $\rightarrow$ Average $\rightarrow$ `[5.5, 5.5, 5.5]`

**Pros:** Ensures consistent feature dimensions regardless of sequence length.
**Cons:** Loss of sequential context and position information.

### 2. Padding
In this method, sequences are padded with zeros to match the length of the longest sequence in the dataset. This preserves the individual subsequence vectors.

*Example:*
- **Seq 1:** `[1,1,1], [2,2,2], [3,3,3], [4,4,4]`
- **Seq 2:** `[5,5,5], [6,6,6], [0,0,0], [0,0,0]` (Padded)

**Pros:** Preserves sequential context information.
**Cons:** Results in high-dimensional, sparse feature vectors.

## Running the Experiment
The experiment logic is contained within `built.ipynb`.

### Environment Setup
To run the experiment effortlessly, it is recommended to use Conda to set up an environment with **Python <= 3.8**.

Run the setup scripts to install dependencies:
1. `python environment_setup1.py`
2. `python environment_setup2.py`

Once the environment is ready, you can execute `built.ipynb` to train the models and visualize the results.
