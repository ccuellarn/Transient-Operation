from flask import Flask, render_template, request
from datetime import datetime
import numpy as np
import pandas as pd
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord, EarthLocation, AltAz

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    datos_tabla = None
    
    if request.method == 'POST':
        # Obtener parámetros del formulario
        latitud = float(request.form.get('latitud'))
        longitud = float(request.form.get('longitud'))
        fecha_inicio = request.form.get('fecha_inicio')
        fecha_fin = request.form.get('fecha_fin')
        escala_tiempo_unidad = request.form.get('escala_tiempo_unidad')
        escala_tiempo_valor = int(request.form.get('escala_tiempo_valor'))
        limite_altitud = int(request.form.get('limite_altitud'))
        magnitud_minima = float(request.form.get('magnitud_minima'))
        parametro_k = float(request.form.get('parametro_k'))
        magnitud_referencia = float(request.form.get('magnitud_referencia'))
        tiempo_exposicion = int(request.form.get('tiempo_exposicion'))
        
        # Obtener alertas de objetos
        nombres = request.form.getlist('nombre_objeto[]')
        ras = request.form.getlist('ra_objeto[]')
        decs = request.form.getlist('dec_objeto[]')
        mags = request.form.getlist('mag_objeto[]')
        
        alertas = {
            'Name': nombres,
            'RA': ras,
            'DEC': decs,
            'Mag': [float(mag) for mag in mags]
        }
        
        # Preparar parámetros para las funciones
        observer = (latitud, longitud)
        date_i = fecha_inicio.replace('T', ' ') + ':00'
        date_f = fecha_fin.replace('T', ' ') + ':00'
        timescale = [escala_tiempo_unidad, escala_tiempo_valor]
        m_min = magnitud_minima
        K = parametro_k
        m_ref = magnitud_referencia
        t_expo = tiempo_exposicion
        many = len(alertas['Name']) + 1
        
        # Llamar a las funciones de cálculo
        data_observations = Observations(
            observer=observer,
            alert=pd.DataFrame(alertas),
            Date_i=date_i,
            Date_f=date_f,
            time_scale=timescale,
            rango=many,
            limit=limite_altitud,
            m_min=m_min
        )
        
        time_array = CreateTime(date_i, date_f, timescale)
        general_time = Time(date_i, format='iso', scale='utc') + np.arange(len(time_array)) * (
            escala_tiempo_valor * u.minute if escala_tiempo_unidad == 'm' else 
            escala_tiempo_valor * u.second if escala_tiempo_unidad == 's' else 
            escala_tiempo_valor * u.hour
        )
        
        order = OrderLimits(
            Data=data_observations,
            rango=many,
            Time=time_array,
            General_time=general_time,
            t_expo=t_expo,
            K=K,
            m_ref=m_ref
        )
        
        if isinstance(order, pd.DataFrame) and not order.empty:
            # Convertir el DataFrame a un formato adecuado para la plantilla
            datos_tabla = []
            for _, row in order.iterrows():
                datos_tabla.append({
                    'hora': Time(row['Time'], format='iso').iso.split()[1][:8],
                    'objeto': row['Name'],
                    'ra': row['RA'],
                    'dec': row['DEC'],
                    'magnitud': f"{row['Mag']:.2f}",
                    'tiempo_exposicion': f"{row['Time expo']:.2f}s",
                    'prioridad': f"{(K * (m_ref - row['Mag']) / row['Time expo']):.2f}"
                })
    
    return render_template('planificador_astro.html', 
                        datos_tabla=datos_tabla,
                        año_actual=datetime.now().year)

# Funciones astronómicas proporcionadas
def DeltaTime(Date_i, Date_f, t_scale):
    scale = t_scale[0]
    sc = t_scale[1]

    a = Time(Date_i, format='iso', scale='utc').datetime.hour-24
    b = Time(Date_f, format='iso', scale='utc').datetime.hour

    if scale == 's':
        len_ = int((b-a) / (sc/3600))
        t_ = np.linspace(a, b, len_)
   
    if scale == 'm':
        len_ = int((b-a) / (sc/60))
        t_ = np.linspace(a, b, len_)
    
    if scale == 'h':
        len_ = int((b-a) / sc)
        t_ = np.linspace(a, b, len_)
    
    return t_

def CreateTime(Date_i, Date_f, t_scale):
    time_midnight = Time(Time(Date_i, format='iso', scale='utc').iso.split()[0] + ' 00:00:00', 
                        format='iso', scale='utc')
    delta = DeltaTime(Date_i, Date_f, t_scale)*u.hour
    return time_midnight + delta

def Observations(observer, alert, Date_i, Date_f, time_scale, rango, limit, m_min):
    time = CreateTime(Date_i, Date_f, time_scale)
    lat_conv, lon_conv = observer
    observer_loc = EarthLocation(lat=lat_conv*u.deg, lon=lon_conv*u.deg)
    Big_Data = []
    
    alert['Label'] = range(1, rango)
    alert['V mag'] = alert['Mag'] <= m_min
    alert = alert[alert['V mag'] != False].drop(['V mag'], axis=1)

    for each_time in time:
        celestial_coord = SkyCoord(ra=alert['RA'], dec=alert['DEC'])
        altaz_coord = celestial_coord.transform_to(AltAz(obstime=each_time, location=observer_loc))
        state = altaz_coord.alt > limit*u.deg
        
        alert['Observable'] = state
        alert['Az'] = altaz_coord.az.deg
        alert['Alt'] = altaz_coord.alt.deg
        
        Data = alert.copy()
        Big_Data.append(Data)

    return pd.concat(Big_Data, axis=0)

def ExpositionTime(K, m, m_ref):
    return K*(10**(0.4*(m - m_ref)))

def OrderLimits(Data, rango, Time, General_time, t_expo, K, m_ref):
    targets = []
    order = []

    for i in range(1, rango):
        Target = Data.loc[Data['Label'] == i].copy()
        if Target.empty:
            continue
        
        Target['Time'] = Time
        Target['Time expo'] = ExpositionTime(K, Target['Mag'], m_ref)
        Target = Target[(Target['Observable'] != False) & (Target['Time expo'] <= t_expo)]

        if not Target.empty:
            targets.append(Target)

    if not targets:
        return pd.DataFrame()

    obs = pd.concat(targets, axis=0).reset_index(drop=True).drop(['Observable'], axis=1)

    first_target = obs[obs['Time'] == Time[0]]
    if not first_target.empty:
        first_target = first_target.sort_values(by='Alt', ascending=False, na_position='first').head(1)
        first_target['Time'] = General_time[0]
        order.append(first_target)
        time_flag = General_time[0] + first_target['Time expo'].iloc[0] * u.second
        position_flag = first_target
    else:
        time_flag = General_time[0]
        position_flag = pd.DataFrame()

    for i in range(1, len(Time)):
        priority = obs.loc[obs['Time'] == Time[i]].sort_values('Alt', ascending=False, na_position='first').head(1)
        current_time = General_time[i]

        if priority.empty:
            continue

        priority['Time'] = current_time

        if not priority.empty:
            if time_flag >= current_time:
                if not position_flag.empty and position_flag['Label'].iloc[0] == priority['Label'].iloc[0]:
                    order.append(priority)
                else:
                    position_flag['Time'] = current_time
                    order.append(position_flag)
            else:
                order.append(priority)
                time_flag = current_time + priority['Time expo'].iloc[0] * u.second
                position_flag = priority

    if not order:
        return pd.DataFrame()
        
    return pd.concat(order, axis=0).reset_index(drop=True).drop(['Az', 'Alt'], axis=1)

if __name__ == '__main__':
    app.run(debug=True)