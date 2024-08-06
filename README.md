# SEM-Processing-Toolkit
This toolkit is designed to provide researchers with tools for processing and analyzing SEM images, including features for defining regions of interest, extracting traits, and labeling traits with low confidence

## Project Structure
- **data/**: Contains raw, processed data, and results
  - **raw/**: Raw SEM images and data
  - **processed/**: Processed dadta and intermediate results
  - **results/**: Final results, reports and outputs
- **notebooks/**: Jupyter notebooks for different stages of the analysis
  - **1_image_preprocessing.ipynb**: Preprocesses SEM images
  - **2_contour_detection_filtering.ipynb**: Detects and filters contours
  - **3_roi_definition_analysis.ipynb**: Defines ROIS and extract traits
  - **4_advanced_trait_extraction.ipynb**: Extracts advanced traits
  - **5_machine_learning_integration.ipynb**: Integrates machine learning models
  - **6_results_aggregation_export.ipynb**: AGgregates and exports results
  - **7_user_interface_documentation.ipynb**: Provides user instructions and documentation
- **src/**: Source code for preprocessing, contour detection, trait extraction, and machine learning
  - **__init__.py**: Makes 'src' a package
  - **preprocessing.py**: Image preprocessing functions
  - **contour_detection.py**: Contour detection and filtering functions
  - **roi_analysis.py**: ROI definition and analysis functions
  - **trait_extraction.py**: Advanced trait extraction functions
  - **ml_models.py**: Machine learning models and related functions
  - **results_export.py**: Functions for aggregating and exporting results
  - **utils.py**: Utility functions
- **tests/**: Unit tests for the source code
  - **test_preprocessing.py**: Tests for preprocessing functions
  - **test_contour_detection.py**: Tests for contour detection functions
  - **test_roi_analysis.py**: Tests for ROI analysis functions
  - **test_trait_extraction.py**: Tests for trait extraction functions
  - **test_ml_models.py**: Tests for machine learning models
  - **test_results_export.py**: Tests for results export functions

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/RickGummy/SEM-Processing-Toolkit.git
   ```
2. Navigate to the project directory:
   ```bash
   cd SEM-Processing-Toolkit
   ```
3. Create a virutal environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows use 'venv\Scripts\activate
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Open JupyterLab:
```bash
jupyter lab
