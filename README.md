# Computer Vision Constellation Classifier

This project focuses on computer vision and involves two subdivisions: collecting the data and developing a constellation classifier model for 12 constellations and its deployment using Streamlit, and a constellation classifier model for all 88 constellations recognized by the International Astronomical Union (IAU). The latter model is built from scratch by collecting images for all 88 classes and performing data augmentation to enhance the dataset for deep learning and computer vision models. The final model is then deployed using Streamlit.

## Installation

To use this project, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/UTPAL14641/Constellation_detector.git
   ```

2. Navigate to the project directory:
   for 1st:
   ```bash
   cd Constellation_detector/constellation_12_class
   ```
   for 2nd:
    ```bash
   cd Constellation_detector/constellation_88_class
   ```
4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the project:

   ```bash
   python main.py
   ```

## Usage

To use the constellation classifier models, follow the instructions provided in the Streamlit interface. The application will allow you to select an image and predict the constellation it corresponds to.

## Data

### 12 Constellations
The dataset for the 12 constellations classifier model consists of images for each constellation. These images were collected from multiple sources from the internet and furthur augmented.

### 88 Constellations
The dataset for the 88 constellations classifier model is created by collecting images for each of the 88 constellations recognized by the IAU(International Astronomical Union ). Data augmentation techniques are applied to enhance the dataset, making it suitable for training deep learning and computer vision models.

## Models

### 12 Constellations
The  CNN based custom model for the 12 constellations classifier is trained and used for deployment. Different parameters were adjusted to improve the accuracy of the model.

### 88 Constellations
The model for the 88 constellations classifier is trained from scratch using the dataset created for this purpose. Several different model architecture were tested upon including CNN based ones and transfer learning on models:MobileNetV2, Vgg16 etc or combination of both and parameters were adjusted to find the best of them.

## Discussion

Throughout the project, several challenges were encountered, including data collection, data augmentation, and developing a good deep learning model. It can be furthur expanded by developing a live version of it and developing it to simultaneously identify several different constellations from same image. Another thing that one can work on is integrating other models to display various informations related to these constellations along with the identification. We can also develop a dataset to counter the noise in the images due to the other stars.

## Contributing

Contributions to this project are welcome. To contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push the changes to your forked repository.
5. Open a pull request in the main repository.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries about the project, feel free to contact me at [utpalraj040503@gmail.com].

## Furthur readings:
If you are interested to learn more about the research related to these topics you can start on from this paper from stanford:
https://web.stanford.edu/class/ee368/Project_Spring_1415/Reports/Ji_Liu_Wang.pdf
