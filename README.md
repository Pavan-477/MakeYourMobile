
# MakeYourMobile

This is an end to end Machine Learning project that predicts the price of your own tailor made Android phone.

It can even predict the price of an existing smartphone by passing it specifications.

You can add only the components you want in your mobile and pay only for them.

App allows customisation at 24 levels such as :

- Mobile design (127 models to choose from)
- UI (8 UIs to choose from)
- Android version (10,Pie,Oreo,Nougat....you name it , we have it)
- Display size (4-7 inches)
- Display type (qHD,FHD+,FHD,HD+)
- Clock speed (1-3 Ghz)
- Cores (Octa core,Quad core,Single core)
- Battery capacity
- Internal memory (8GB - 512GB)
- RAM (1GB -12GB)
- Main camera(5MP(min requirement) - 108 MP)
- Additional cameras (we've got UW,Telephoto and depth too .. Not  camera centric ?? we can skip these cameras for you)
- Selfie camera (2MP-44MP!!)
- 5g , 4g, VoLTE, 3g ,2g(add them all or add only what you want)

Based on these inputs the application is able to estimate the price of your mobile phone .

Its has achieved 91% accuracy on test data and 81% accuracy on 20 cross folds data.


## Project link
https://makeyourmobile.onrender.com
## Tech Stack

- Python
- Numpy
- Pandas
- Matplotlib
- Seaborn
- Sci-kit learn
- Pickle
- Flask
- HTML
- Gunicorn
- Waitress



## Installation

Install all the necessary libraries using pip

```bash
  pip install -r requirements.txt
```
    
##  Working
1)Imported all the necessary libraries and the dataset.

2)Checked the distribution and flow of the data.

3)Performed intensive EDA for easier interpretation of the data.

4)Visualized the data.

5)Performed Data Wrangling.

6)Modelling with baseline regression model.

7)Checking the performance with other regression models.

8)Going with the model that best explains the variance .

9)Automated the entire process through pipelines.

10)Dumping the model in a pickle file .

11)Deploying it in flask. 

12)Deploying the application on render.
## Deployment

To deploy this project run

```bash
  gunicorn app:app
```


## Author

- [@Pavan Kumar V](https://github.com/Pavan-477)

