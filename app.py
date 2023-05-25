from flask import Flask, render_template,request,url_for
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
model=pickle.load(open('mym1.0.pkl','rb'))
df=pd.read_csv('mobile_cleaned.csv')
color=list(df['mobile_color'].unique())
color.sort()
resolution=list(df['resolution'].unique())
resolution.sort()
os=list(df['os'].unique())
os.sort()
num_cores=list(df['num_cores'].unique())
num_cores.sort()
int_memory=list(df['int_memory'].unique())
int_memory.sort()
ram=list(df['ram'].unique())
ram.sort()
brands=list(df['Brand'].unique())
primary_cam=list(df['primary_cam'].unique())
primary_cam.sort()
secondary_cam=list(df['secondary_cam'].unique())
secondary_cam.sort()
tertiary_cam=list(df['tertiary_cam'].unique())
tertiary_cam.sort()
quaternary_cam=list(df['quaternary_cam'].unique())
quaternary_cam.sort()
f_cam_primary=list(df['f_cam_primary'].unique())
f_cam_primary.sort()
f_cam_secondary=list(df['f_cam_secondary'].unique())
f_cam_secondary.sort()
modelsByBrand = {}
for i in brands:
    key=i
    value=list(df['mobile_name'][(df['Brand']==i)].unique())
    value.sort()
    modelsByBrand[key]=value

@app.route('/')
def index():
    return render_template("index.html", brands=brands, modelsByBrand=modelsByBrand,color=color,resolution=resolution,
                           os=os,num_cores=num_cores,int_memory=int_memory,ram=ram,primary_cam=primary_cam,
                           secondary_cam=secondary_cam,tertiary_cam=tertiary_cam,quaternary_cam=quaternary_cam,
                           f_cam_primary=f_cam_primary,f_cam_secondary=f_cam_secondary)



@app.route('/predict', methods=['GET', 'POST'])
def predict():
   
    try:
        brand = request.form.get('brand')
        mobile_name = request.form.get('model')
        mobile_color = request.form.get('color')
        Sims = int(request.form.get('Sims'))
        disp_size = float(request.form.get('display_size'))
        num_cores = request.form.get('num_cores')
        os = request.form.get('os')
        resolution = request.form.get('resolution')
        mp_speed = float(request.form.get('mp_speed'))
        int_memory = int(request.form.get('int_memory'))
        ram = int(request.form.get('ram'))
        battery_power = int(request.form.get('battery'))
        fiveG_connectivity = request.form.get('5G_connectivity')
        VOLTE_connectivity = request.form.get('VOLTE_connectivity')
        fourG_connectivity = request.form.get('4G_connectivity')
        threeG_connectivity = request.form.get('3G_connectivity')
        twoG_connectivity = request.form.get('2G_connectivity')
        primary_cam = int(request.form.get('primary_cam'))
        secondary_cam = int(request.form.get('secondary_cam'))
        tertiary_cam = int(request.form.get('tertiary_cam'))
        quaternary_cam = int(request.form.get('quaternary_cam'))
        Low_light_sensor = request.form.get('Low_light_sensor')
        f_cam_primary = int(request.form.get('f_cam_primary'))
        f_cam_secondary = int(request.form.get('f_cam_secondary'))

        
                
        # Perform prediction
        prediction = model.predict(pd.DataFrame(
            columns=['mobile_name', 'mobile_color', 'Sims', 'disp_size',
                     'resolution', 'os', 'num_cores', 'mp_speed', 'int_memory', 'ram',
                     'battery_power', 'Brand', '5G_connectivity', 'VOLTE_connectivity',
                     '4G_connectivity', '3G_connectivity', '2G_connectivity', 'primary_cam',
                     'secondary_cam', 'tertiary_cam', 'quaternary_cam', 'Low_light_sensor',
                     'f_cam_primary', 'f_cam_secondary'],
            data=np.array([mobile_name, mobile_color, Sims, disp_size,
                           resolution, os, num_cores, mp_speed, int_memory, ram,
                           battery_power, brand, fiveG_connectivity, VOLTE_connectivity,
                           fourG_connectivity, threeG_connectivity, twoG_connectivity, primary_cam,
                           secondary_cam, tertiary_cam, quaternary_cam, Low_light_sensor,
                           f_cam_primary, f_cam_secondary]).reshape(1, 24)))[0]
        
        output = int(prediction)
        lower_limit = output - 500
        upper_limit = output + 500
        
        resulting_string = str(lower_limit) +' - ' + str(upper_limit)

        return render_template('results.html', predicted=resulting_string)
    
    except ValueError as e:
        error_message = ''
        if 'could not convert string to float' in str(e):
            error_message='Please enter numeric values in case under the Display size and Clock speed options'
        elif 'invalid literal for int() with base 10' in str(e):
            error_message='Please enter integer values under the Battery option'
        else:
            error_message='Unknown issue, please re-enter your inputs again'
        
        return render_template('error.html', error_message=error_message)
    except TypeError as e:
        error_message=''
        if 'int() argument must be a string, a bytes-like object or a number' in str(e):
            error_message='Please fill out all the options'
        return render_template('error.html', error_message=error_message)

    return None

if __name__ == "__main__":
    app.run()