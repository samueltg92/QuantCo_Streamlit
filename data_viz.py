import streamlit as st
import pandas as pd
import numpy as np
import plotly as plt
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components
from plotly.subplots import make_subplots

st.image('Data/Logos/Quantlabs_logo_horizontal.png', width=250)
st.sidebar.header('Menú de navegación')

menu = st.sidebar.selectbox('Selecciona un año', ('Inicio','About', 'Disclaimer', '2022', '2023', '2024'))

if menu == 'About':
        st.subheader('About')
        st.write('''The Quant Company es una FinTech mexicana que ofrece soluciones digitales para ayudar a la transformación de la industria de la inversión
            en mercados financieros, a través de la generación de portafolios de inversión automatizados, rentables y estables.

            \nFue fundado en 2022, en Latinoamerica por Santiago Flores y Samuel Tamayo, con el objetivo de ofrecer protección al patrimonio de los inversionistas, de
            los movimientos economicos que afectan el valor del capital.
            
            \nLa empresa actualmente tiene diversos portafolios en mercados de capital liquido (renta variable) que ofrece a nuestros clientes oportunidades de 
            diversificacion de su patrimonio.
            ''')

        st.subheader('Organigrama de la empresa')
        col1,col2,col3 = st.columns(3,gap='large')

        col1.subheader('Thiago Flores')
        col1.text('Cofounder')
        col1.image('Data/fotos/foto_thiago.jpg', width=150)

        col2.subheader('Sam Gaviria')
        col2.text('Cofounder')
        col2.image('Data/fotos/foto_sam.jpg', width=150)

        col3.subheader('Beto Queeq')
        col3.text('Angel Investor')
        col3.image('Data/fotos/foto_beto.jpg', width=150)


if menu == 'Disclaimer':
    st.subheader('Disclaimer')
    st.write('''
            \nLa negociación en el mercado de divisas conlleva un alto nivel de riesgo y no es adecuada para todos los inversores. Un alto
            apalancamiento puede funcionar tanto a su favor como en contra. Antes de tomar una decisión sobre el comercio de divisas, un inversor
            debe considerar cuidadosamente sus objetivos, experiencia y nivel de riesgo. El rendimiento pasado no es necesariamente indicativa de
            resultados futuros. Es posible perder parte o todo el capital inicial invertido. Por lo tanto, no debes invertir dinero que no puedas permitirte
            perder. El inversor debe ser consciente de los riesgos asociados con el comercio de divisas y, en caso de duda, tratar de buscar ayuda de
            un asesor financiero independiente.
            \nTambién existen riesgos asociados con el uso de un sistema de comercio basado en internet, que incluyen hardware, software y fallas en
            la conexión a internet. Ninguno de los corredores controla la intensidad de la señal, la configuración de su equipo o la confiabilidad de sus
            conexiones, no pueden ser responsables de fallas de comunicación, distorsiones o retrasos durante el comercio por internet. Los
            corredores tienen sistemas de archivo y planes de contingencia para minimizar la posibilidad de fallas del sistema de su lado.
            DeepAtlas/The Quant Company no es un bróker y no lleva a cabo actividades de corretaje en el sentido de las leyes que lo cobijan. No brinda
            asesoría financiera, no emite recomendaciones, no media en la implementación de estrategias de trading y no realiza ninguna otra
            actividad que requiera licencias especiales. DeepAtlas tampoco es un intermediario o agente de una empresa de inversión (en nuestro
            caso del bróker Roboforex). El servicio de DeepAtlas/The Quant Company no es parte del contrato; los clientes firman un contrato
            directamente con el corredor seleccionado.
             ''')


if menu == 'Inicio':
    st.title('Presentación de resultados Quant Labs')
    st.write('''Bienvenido al nuevo formato de presentación de resultados de Quant Labs. Aquí podrá encontrar toda la 
             información relacionada con los resultados de nuestro portafolio general, de manera mensual.
             
             \nEn esta presentación de resultados, se evidenciará el performance del capital de nuestros inversionitas.
             Los insights clave que se tendrán en cuenta serán insigths de rendimients (%), riesgo traducido en la métrica de 
             "drawdown", la proyección futura y la presentación del portafolio de activos donde se invierte el capital.
             Todos los indicadores acá presentados, se encuentran en el portafolio de Roboforex y Binance.


             \nRecomendamos que configure el aplicativo siguiendo los siguientes pasos:
             \n1. Presione en el menú de navegación superior derecho y seleccione "Settings" (≡).
             \n2. Dentro del menú Settings, en la opción de APPAERANCE, marque la casilla "Wide mode".
             \n3. Cierre la ventana de Settings y continúe navegando por el aplicativo.
             \n------------------------------------------------------------------------------------------------------------------
             \nPara comenzar a navegar, siga los siguientes pasos:
             \n1. Seleccione un año en el menú de navegación lateral izquierdo. 
             \n2. Seleccione un mes.
             ''')

#---------------------------------2022-----------------------------------#

if menu == '2022':
    meses = st.sidebar.selectbox('Selecciona un mes', ('Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'))
    
    def mes(mes):
        if meses == mes:
            print(st.title(f'Resultados {meses} {menu}'))
            
    
    mes(meses)

#---------------------------------AGOSTO---------------------------------#
    if meses == 'Agosto':
        
        submenu = st.sidebar.selectbox('Selecciona una opción', ('Acumulado', 'DeepAtlas CopyFx', 'Binance', 'DeepAtlas vs EURUSD'))
        
        if submenu == 'Acumulado':
            acumulado = 'Data/2022/1. Agosto 2022/calculos_finales_agosto2022.xlsx'
            acu = pd.read_excel(acumulado, sheet_name= 0)
            acu = acu.set_index('datetime')
            x = acu.index
            y = acu['Balance']
            z = acu['d_ret']
            w = acu['ARR x 80dias']

            fig1 = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig1.update_layout(title='Balance Acumulado Agosto 2022', xaxis_title='Fecha', yaxis_title='Balance')
            st.plotly_chart(fig1)
            
            st.write('''
                     Se inició con un capital de 15,877 dólares
                    debido a las pruebas que faltaban por
                    hacer en la cuenta demo de DeepAtlasFx.
                    Además, no se usó un 33% del capital
                    para las cuentas de trading manual,
                    debido a problemas logísticos. Aun así,
                    hubo un crecimiento del portafolio total,
                    del 2.02%. Para el mes de septiembre, se
                    iniciará con un capital de $24,998.25
                    debido al pago de salarios.
                     ''')

            fig2 = go.Figure(go.Scatter(x=x, y=z, mode='lines', name='Crecimiento porcentual', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Agosto 2022', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)

            st.subheader('''
                         :blue[Crecimiento del 2.02% del balance]
                         ''')
            st.write('''
                    - El mayor aportante fue la cuenta de DeepAtlasFx con un crecimiento neto de 4.18%.
                    \n- Trader2 obtuvo una utilidad neta del 2.49%.
                     ''')
            
            fig3 = go.Figure(go.Scatter(x=x, y=w, mode='lines', name='Annual Return Rate x 80dias', line_shape='spline'))
            fig3.update_layout(title='Annual Return Rate x 80dias Agosto 2022', xaxis_title='Fecha', yaxis_title='Annual Return Rate')
            st.plotly_chart(fig3)
            
            st.subheader('''
                         :blue[Se proyectan retornos del 8% en promedio al terminar el año 2022]
                         ''')
            st.write('''
                     - En promedio se esperan, por los cuatro meses subsiguientes, retornos de un 2% aproximadamente para cada mes.
                     \n- La proyección dada se da basada en el 2.02% generado en el mes de agosto.
                     ''')
        
        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2022/1. Agosto 2022/Registro_de_operaciones_Roboforex_Agosto2022.xlsx"
            df = pd.read_excel(roboforexMT4)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            #fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            #st.plotly_chart(fig)
            st.plotly_chart(fig2)
            
            st.subheader('''
                         :blue[DeepAtlas CopyFx crece un 5.15%]
                         ''')
            st.write('''
                    El mes de Agosto comienza con una utilidad neta de 5.15%, aportando así, por peso ponderado, la mayor utilidad al portafolio. 
                     ''')
        
        if submenu == 'Binance':
            binance = "Data/2022/1. Agosto 2022/Registro_de_operaciones_Binance_Agosto2022.xlsx"
            ##Sam
            df = pd.read_excel(binance, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Sam Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)
            ##Thiago
            df2 = pd.read_excel(binance, sheet_name= 1)
            df2 = df2.set_index('datetime')
            df2['pct_change'] = df2['Balance'].pct_change().cumsum() *100
            x2 = df2.index
            y3 = df2['Balance']
            y4 = df2['pct_change']
            fig3 = go.Figure(go.Scatter(x=x2, y=y4, mode='lines', name='Crecimiento', line_shape='spline'))
            fig3.update_layout(title='Crecimiento porcentual Thiago Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig3)
            
        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 3.48% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas 
                     es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/1. Agosto 2022/DAMT4_vs_EURUSD_Agosto2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200)
            
#---------------------------------SEPTIEMBRE---------------------------------#
    if meses == 'Septiembre':
        submenu = st.sidebar.selectbox('Selecciona una opción', ('Acumulado', 'DeepAtlas CopyFx', 'DeepAtlas MT5', 'Binance', 'Roboforex 7369598', 'Roboforex 72116376', 'DeepAtlas vs EURUSD'))
        
        if submenu == 'Acumulado':
            acumulado = 'Data/2022/2. Septiembre2022/calculos_finales.xlsx'
            acu = pd.read_excel(acumulado, sheet_name= 0)
            acu = acu.set_index('mdate')
            x = acu.index
            y = acu['Balance']
            z = acu['d_ret']
            w = acu['max_dd']
            v = acu['ARR x 80dias']
            u = acu['ARR x 80dias acu']

            fig1 = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig1.update_layout(title='Balance Acumulado Septiembre 2022', xaxis_title='Fecha', yaxis_title='Balance')
            st.plotly_chart(fig1)
            
            st.write('''
                     La diferencia actual tan amplia es
                    debido a la adición de un capital
                    faltante correspondiente al de trading
                    manual de Binance del trader #3 y
                    del capital de diversificación que
                    tenía como objetivo la apertura de
                    una cuenta de Darwinex. Se decidió
                    prescindir de esta última, ya que por
                    movimientos internos, se
                    complicó la apertura de la cuenta.
                     ''')

            fig2 = go.Figure(go.Scatter(x=x, y=z, mode='lines', name='Crecimiento porcentual', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Septiembre 2022', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)
            
            st.write('''
                    Para el mes de septiembre, el portafolio general tuvo un crecimiento de 1.7%, lo cuál representa un decrecimiento de 0.32% con respecto al mes anterior.
                    Esta utilidad menor, fue debido a los rendimientos negativos de las cuentas de trading manual en Binance, restando al total un 2.86%.
                    ''')

            fig3 = go.Figure(go.Scatter(x=x, y=w, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo Septiembre 2022', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            st.plotly_chart(fig3)
            
            st.write('''
                     A pesar de las caídas en el
                    balance de las dos cuentas de 
                    trading manual en Binance, el 
                    drawdown máximo generado para 
                    este mes fue de un 1%.
                    ''')

            fig4 = make_subplots(rows=1, cols=1, shared_xaxes=True, subplot_titles=('Annual return rate acumulado'))
            fig4.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Annual Return Rate x 80dias', line_shape='spline'))
            fig4.add_trace(go.Scatter(x=x, y=u, mode='lines', name='Retorno acumulado', line_shape='spline', line = dict(color='red')))
            fig4.update_layout(title='Annual Return Rate x 80dias Septiembre 2022', xaxis_title='Fecha', yaxis_title='Annual Return Rate')
            st.plotly_chart(fig4)
            
            st.subheader(':blue[Retornos por debajo de lo proyectado]')
            st.write('Para este mes no se logró superar los retornos esperados, esto debido principalmente al bajo performance de las dos cuentas de trading manual.')
            st.subheader(':blue[Proyección basada en resultados del mes de agosto]')
            st.write('La proyección dada es basada en el 2.02% generado en el mes de agosto, mes en el que se inicia operaciones en el año 2022.')
                    
        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2022/2. Septiembre2022/Registro_de_operaciones_Roboforex_Septiembre2022.xlsx"
            df = pd.read_excel(roboforexMT4)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.write('''
                     DeepAtlas fue la cuenta que más aportó este mes
                    con un crecimiento total del 5.10%, representando 
                    un 0.05% menos que el mes anterior.
                    ''')
        
        if submenu == 'DeepAtlas MT5':
            roboforexMT5 = "Data/2022/2. Septiembre2022/Registro_de_operaciones_RoboforexMT5_Septiembre2022.xlsx"
            df = pd.read_excel(roboforexMT5)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='hv'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='hv'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            
            st.subheader(':blue[Apertura de cuenta individual en MT5]')
            st.write('''La apertura de la nueva cuenta comercial, con parámetros que permitían maximizar los
                    retornos, fue una buena decisión que logró su objetivo inicial, asegurándonos incrementar en
                    un 0.75% nuestro portafolio total en un periodo de dos semanas.
                    ''')
        
        if submenu == 'Binance':
            binance = "Data/2022/2. Septiembre2022/Registro_de_operaciones_Binance_Septiembre2022.xlsx"
            ##Sam
            df = pd.read_excel(binance, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Sam Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)
            ##Thiago
            df2 = pd.read_excel(binance, sheet_name= 1)
            df2 = df2.set_index('datetime')
            df2['pct_change'] = df2['Balance'].pct_change().cumsum() *100
            x2 = df2.index
            y3 = df2['Balance']
            y4 = df2['pct_change']
            fig3 = go.Figure(go.Scatter(x=x2, y=y4, mode='lines', name='Crecimiento', line_shape='spline'))
            fig3.update_layout(title='Crecimiento porcentual Thiago Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig3)
            
        if submenu == 'Roboforex 7369598':
            roboforex7369598 = 'Data/2022/2. Septiembre2022/Registro_de_operaciones_7369598.xlsx'
            df = pd.read_excel(roboforex7369598, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados Roboforex 7369598')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)
                        
        if submenu == 'Roboforex 72116376':
            roboforex72116376 = 'Data/2022/2. Septiembre2022/Registro_de_operaciones_72116376.xlsx'
            df = pd.read_excel(roboforex72116376, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados roboforex72116376')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)            
            
        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 3.41% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas CopyFx
                     es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/2. Septiembre2022/DAMT5_vs_EURUSD_Septiembre2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200)     
            
#---------------------------------OCTUBRE-----------------------------------#
    if meses == 'Octubre':
        submenu = st.sidebar.selectbox('Selecciona una opción', ('Acumulado', 'DeepAtlas CopyFx', 'DeepAtlas MT5', 'Binance', 'Roboforex 7369598', 'Roboforex 72116376', 'DeepAtlas vs EURUSD'))

        if submenu == 'Acumulado':
            acumulado = 'Data/2022/3. Octubre2022/calculos_finales_octubre2022.xlsx'
            acu = pd.read_excel(acumulado, sheet_name= 0)
            acu = acu.set_index('mdate')
            x = acu.index
            y = acu['Balance']
            z = acu['d_ret']
            w = acu['max_dd']
            v = acu['ARR x 80dias']
            u = acu['ARR x 80dias acu']

            fig1 = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig1.update_layout(title='Balance Acumulado Octubre 2022', xaxis_title='Fecha', yaxis_title='Balance')
            st.plotly_chart(fig1)

            st.write('''
            Se espera llegar a punto de equilibrio
            al finalizar el año 2022.
            Se comienza el mes de noviembre de
            2022 con un capital de $48,053 usd
            que seguirá siendo diversificado de
            igual forma, como lo fue en octubre de 2022.

            ''')

            fig2 = go.Figure(go.Scatter(x=x, y=z, mode='lines', name='Crecimiento porcentual', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Octubre 2022', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)

            st.write('''
                El portafolio total tuvo un crecimiento de un 5.89%,
                representando un crecimiento en las utilidades del 0.1%
                respecto al mes de septiembre.
            ''')

            fig3 = go.Figure(go.Scatter(x=x, y=w, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo Octubre 2022', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            st.plotly_chart(fig3)

            st.write(''' 
                Hubo un drawdown máximo del -2.41% del capital inicial
                para el mes de octubre, creciendo con respecto al mes
                de septiembre un 1.51%.

            ''')
            
            fig4 = make_subplots(rows=1, cols=1, shared_xaxes=True, subplot_titles=('Annual return rate acumulado'))
            fig4.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Annual Return Rate x 80dias', line_shape='spline'))
            fig4.add_trace(go.Scatter(x=x, y=u, mode='lines', name='Retorno acumulado', line_shape='spline', line = dict(color='red')))
            fig4.update_layout(title='Annual Return Rate x 80dias Octubre 2022', xaxis_title='Fecha', yaxis_title='Annual Return Rate')
            st.plotly_chart(fig4)

            st.subheader(':blue[Retornos por encima de lo proyectado]')
            st.write('El mes de octubre superó por un poco más del doble, las utilidades esperadas del 2% proyectadas para el resto del 2022.')

            st.subheader(':blue[Proyección basada en resultados del mes de septiembre]')
            st.write('La proyección dada se da basada en el 2.02% generado en el mes de septiembre, mes en el que se inicia operaciones en el año 2022.')

        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2022/3. Octubre2022/Registro_de_operaciones_Roboforex_Octubre2022.xlsx"
            df = pd.read_excel(roboforexMT4)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='hvh'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.write('DeepAtlasMT4 fue la cuenta que más creció este mes con un total del 5.89%.')

        if submenu == 'DeepAtlas MT5':
            roboforexMT5 = "Data/2022/3. Octubre2022/Registro_de_operaciones_RoboforexMT5_Octubre2022.xlsx"
            df = pd.read_excel(roboforexMT5)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.write('DeepAtlasMT5 creció un 5.53%, aportándole más al crecimiento total, debido a su peso ponderado.')

        if submenu == 'Binance':
            binance = "Data/2022/3. Octubre2022/Registro_de_operaciones_Binance_Octubre2022.xlsx"
    
            df = pd.read_excel(binance, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Sam Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)
        
        if submenu == 'Roboforex 7369598':
            roboforex7369598 = 'Data/2022/3. Octubre2022/Registro_de_operaciones_7369598.xlsx'
            df = pd.read_excel(roboforex7369598, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados Roboforex 7369598')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)
        
        if submenu == 'Roboforex 72116376':
            roboforex72116376 = 'Data/2022/3. Octubre2022/Registro_de_operaciones_72116376.xlsx'
            df = pd.read_excel(roboforex72116376, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2= df['pct_change']
            # y2 = df['pct_change'].resample('D').sum()


            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados roboforex72116376')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)  

        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 3.55% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas CopyFx
            es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/3. Octubre2022/DAMT5_vs_EURUSD_Octubre2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200) 

#---------------------------------NOVIEMBRE---------------------------------#
    if meses == 'Noviembre':
        submenu = st.sidebar.selectbox('Selecciona una opción', ('Acumulado', 'DeepAtlas CopyFx', 'DeepAtlas MT5', 'Binance', 'Roboforex 7369598', 'Roboforex 72116376', 'DeepAtlas vs EURUSD'))

        if submenu == 'Acumulado':
            acumulado = 'Data/2022/4. Noviembre2022/calculos_finales.xlsx'
            acu = pd.read_excel(acumulado, sheet_name= 0)
            acu = acu.set_index('mdate')
            x = acu.index
            y = acu['Balance']
            z = acu['d_ret']
            w = acu['max_dd']
            v = acu['ARR x 80dias']
            u = acu['ARR x 80dias acu']

            fig1 = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig1.update_layout(title='Balance Acumulado Noviembre 2022', xaxis_title='Fecha', yaxis_title='Balance')
            st.plotly_chart(fig1)

            st.write('''Se comienza el mes de diciembre de 2022 con un capital de $46,976 usd,
                un -0.294% menos que el mes pasado. 
                Aún se proyecta llegar a punto de equilibrio al finalizar el año 2022.''')

            fig2 = go.Figure(go.Scatter(x=x, y=z, mode='lines', name='Crecimiento porcentual', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Noviembre 2022', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)

            st.write('El portafolio total decreció un -0.294% debido a retiros para realizar pagos necesarios que serían usados para ampliar el portafolio de estrategias.')


            fig3 = go.Figure(go.Scatter(x=x, y=w, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo Noviembre 2022', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            st.plotly_chart(fig3)

            st.write('''La retracción máxima o drawdown máximo del mes de noviembre fue de -0.294%. El riesgo en el mes de octubre se logró contener por debajo del 1%, lo cual
                    demuestra que se mantiene un portafolio de bajo riesgo.''')

            
            fig4 = make_subplots(rows=1, cols=1, shared_xaxes=True, subplot_titles=('Annual return rate acumulado'))
            fig4.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Annual Return Rate x 80dias', line_shape='spline'))
            fig4.add_trace(go.Scatter(x=x, y=u, mode='lines', name='Retorno acumulado', line_shape='spline', line = dict(color='red')))
            fig4.update_layout(title='Annual Return Rate x 80dias Noviembre 2022', xaxis_title='Fecha', yaxis_title='Annual Return Rate')
            st.plotly_chart(fig4)

            st.subheader(':blue[Retornos por debajo de lo proyectado]')
            st.write('El mes de noviembre no cumplió con el retorno proyectado para este mes, debido a retiros necesarios para reinvertir en infraestructura necesaria.')
            st.subheader(':blue[Proyección basada en resultados del mes de octubre]')
            st.write('La proyección dada se da basada en el 2.02% generado en el mes de octubre, mes en el que se inicia operaciones en el año 2022. ')

        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2022/4. Noviembre2022/Registro_de_operaciones_Roboforex_Noviembre2022.xlsx"
            df = pd.read_excel(roboforexMT4)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='hvh'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            
            st.plotly_chart(fig)
            st.plotly_chart(fig2)

        if submenu == 'DeepAtlas MT5':
            roboforexMT5 = "Data/2022/4. Noviembre2022/Registro_de_operaciones_RoboforexMT5_Noviembre2022.xlsx"
            df = pd.read_excel(roboforexMT5)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig)
            st.plotly_chart(fig2)

            st.write('- DeepAtlasMT5 fue la cuenta que más creció este mes con un total del 6.21%.')
            st.write('- El capital de la cuenta del Trader1 se traslada a la cuenta de DeepAtlasMT5.')

        if submenu == 'Binance':
            binance = "Data/2022/4. Noviembre2022/Registro_de_operaciones_Binance_Noviembre2022.xlsx"
            
            df = pd.read_excel(binance, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Sam Binance', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)

        if submenu == 'Roboforex 7369598':
            roboforex7369598 = 'Data/2022/4. Noviembre2022/Registro_de_operaciones_7369598.xlsx'
            df = pd.read_excel(roboforex7369598, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados Roboforex 7369598')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3)
        
        if submenu == 'Roboforex 72116376':
            roboforex72116376 = 'Data/2022/4. Noviembre2022/Registro_de_operaciones_72116376.xlsx'
            df = pd.read_excel(roboforex72116376, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2= df['pct_change']
            # y2 = df['pct_change'].resample('D').sum()


            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados roboforex72116376')

            st.plotly_chart(fig)
            st.plotly_chart(fig2)
            st.plotly_chart(fig3) 

        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 1.78% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas CopyFx
            es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/4. Noviembre2022/DAMT5_vs_EURUSD_Noviembre2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200) 
            
#---------------------------------DICIEMBRE---------------------------------#
    if meses == 'Diciembre':
        submenu = st.sidebar.selectbox('Selecciona una opción', ('Acumulado', 'DeepAtlas CopyFx', 'DeepAtlas MT5', 'Roboforex 7369598', 'Roboforex 72116376', 'DeepAtlas vs EURUSD'))
        if submenu == 'Acumulado':
            acumulado = 'Data/2022/5. Diciembre2022/calculos_finales.xlsx'
            acu = pd.read_excel(acumulado, sheet_name= 0)
            acu = acu.set_index('mdate')
            x = acu.index
            y = acu['Balance']
            z = acu['d_ret']
            w = acu['max_dd']
            v = acu['ARR x 80dias']
            u = acu['ARR x 80dias acu']

            fig1 = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig1.update_layout(title='Balance Acumulado Diciembre 2022', xaxis_title='Fecha', yaxis_title='Balance')
            st.plotly_chart(fig1)

            st.write('''Para el mes de diciembre se retiraron $35.580 usd, lo cual representó una reducción del 72% del balance general del portafolio interno. Debido a esto, 
                     se tuvieron que pausar la estrategias de DeepAtlasMT5 y las dos cuentas de Roboforex donde se diversificaba el capital en diferentes operadores.''')

            fig2 = go.Figure(go.Scatter(x=x, y=z, mode='lines', name='Crecimiento porcentual', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual diciembre 2022', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            st.plotly_chart(fig2)

            st.write('''
                     A pesar del retiro del 72% del balance general, se logró un crecimiento porcentual de 2.02%. Esto, gracias a la venta de un portafolio de algortimos, la venta de
                     nuestro algoritmo de tick scalping para las cuentas de empresas de fondeo y las utilidades generadas por DeepAtlas CopyFx.
                     ''')


            fig3 = go.Figure(go.Scatter(x=x, y=w, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo Diciembre 2022', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            st.plotly_chart(fig3)

            st.write(''' 
                    Para este mes se logró contener el drawdown máximo a un -0.77%, lo cual es un buen resultado, ya que de esta manera se pudo mantener el riesgo de pérdida bajo. 
                     ''')

            
            fig4 = make_subplots(rows=1, cols=1, shared_xaxes=True, subplot_titles=('Annual return rate acumulado'))
            fig4.add_trace(go.Scatter(x=x, y=v, mode='lines', name='Annual Return Rate x 80dias', line_shape='spline'))
            fig4.add_trace(go.Scatter(x=x, y=u, mode='lines', name='Retorno acumulado', line_shape='spline', line = dict(color='red')))
            fig4.update_layout(title='Annual Return Rate x 80dias Diciembre 2022', xaxis_title='Fecha', yaxis_title='Annual Return Rate')
            st.plotly_chart(fig4)

            st.subheader(':blue[Retornos según lo proyectado]')
            st.write('''
                     Para el mes de diciembre se logró cerrar el año con un retorno según lo proyectado desde el mes de agosto de 2022 (2.02% mensual), lo cual representó un cumplimiento de proyección
                     de final de año al 94.9%. Esto quiere decir que de un total de 8.09% proyectado a final de año, se logró cerrar con un 7.68% de retorno.
                     ''')

        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2022/5. Diciembre2022/Registro_de_operaciones_Roboforex_Diciembre2022.xlsx"
            roboforexMT4DD = "Data/2022/Acumulado/DeepAtlasCopyFx.xlsx"
            df = pd.read_excel(roboforexMT4, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            
            df2 = pd.read_excel(roboforexMT4DD, sheet_name= 0)
            df2 = df2.set_index('datetime')            
            
            x = df.index
            x2 = df2.index
            y = df['Balance']
            y2 = df['pct_change']
            y3 = df2['max_dd'] *100

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='hvh'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            
            fig3 = go.Figure(go.Scatter(x=x2, y=y3, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            
            st.plotly_chart(fig)
            st.write('''
                    El mes de diciembre para la cuenta de DeepAtlas CopyFx fue un mes de crecimiento, a pesar de un retiro de $1.000 usd
                    para un cliente de The Quant Company. Este retiro fue compensado con un depósito por el mismo valor, por concepto de 
                    la venta de un algoritmo de tick scalping para empresas de fondeo.
                    ''')
            
            st.plotly_chart(fig2)
            st.write('''
                    El crecimiento para este mes, fue de 4.34%, lo cual representa un crecimiento de un 1.38% menos que el mes anterior.
                    Esta baja en el crecimiento, fue debido a la baja liquidez en el mercado operado que se traduce en baja volatilidad, por
                    lo cual, DeepAtlas, opera en una menor frecuencia.
                    ''')
            
            st.plotly_chart(fig3)
            st.write('''
                    El drawdown máximo para este mes, fue de -0.69%, lo cual es un buen resultado, ya que de esta manera se pudo 
                    mantener el riesgo de pérdida bajo y teniendo en cuenta los resultados de los 4 meses pasados, fue el drawdown más bajo.
                     ''')

        if submenu == 'DeepAtlas MT5':
            roboforexMT5 = "Data/2022/5. Diciembre2022/Registro_de_operaciones_RoboforexMT5_Diciembre2022.xlsx"
            df = pd.read_excel(roboforexMT5)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']
            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')
            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas MT5', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            
            st.plotly_chart(fig)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada de DeepAtlas MT5, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')
            
            st.plotly_chart(fig2)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada de DeepAtlas MT5, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')

        if submenu == 'Roboforex 7369598':
            roboforex7369598 = 'Data/2022/5. Diciembre2022/Registro_de_operaciones_7369598.xlsx'
            df = pd.read_excel(roboforex7369598, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2 = df['pct_change']

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual Roboforex 7369598', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados Roboforex 7369598')

            st.plotly_chart(fig)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada #7369598 de Roboforex, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')
            
            st.plotly_chart(fig2)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada #7369598 de Roboforex, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')            
            
            st.plotly_chart(fig3)


        if submenu == 'Roboforex 72116376':
            roboforex72116376 = 'Data/2022/5. Diciembre2022/Registro_de_operaciones_72116376.xlsx'
            df = pd.read_excel(roboforex72116376, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100            
            x = df.index
            y = df['Balance']
            y2= df['pct_change']
            # y2 = df['pct_change'].resample('D').sum()


            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='spline'))
            fig2.update_layout(title='Crecimiento porcentual roboforex72116376', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            fig3 = px.pie(df, values='Balance', names='Item', title='Activos operados roboforex72116376')

            st.plotly_chart(fig)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada #72116376 de Roboforex, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')
                           
            st.plotly_chart(fig2)
            st.write('''
                    Este mes, no se obtuvieron resultados de crecimiento en la cuenta diversificada #72116376 de Roboforex, debido a que se
                    generó un retiro por parte de un cliente, de la totalidad del capital asignado a esta cuenta.
                     ''')   
                        
            st.plotly_chart(fig3) 

        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 1.84% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas CopyFx
            es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/5. Diciembre2022/DAMT4_vs_EURUSD_Diciembre2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200)

if menu == '2023':
    meses = st.sidebar.selectbox('Selecciona un mes', ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'))
    
    def mes(mes):
        if meses == mes:
            print(st.title(f'Resultados {meses} {menu}'))
    
    mes(meses)
    
#---------------------------------ENERO 2023---------------------------------#
    if meses == 'Enero':
        submenu = st.sidebar.selectbox('Selecciona una opción', ('DeepAtlas CopyFx', 'DeepAtlas vs EURUSD'))

        if submenu == 'DeepAtlas CopyFx':
            roboforexMT4 = "Data/2023/1. Enero 2023/Registro_de_operaciones_Roboforex_Enero2023.xlsx"
            roboforexMT4DD = "Data/2023/1. Enero 2023/calculos_finales_Enero2023.xlsx"
            df = pd.read_excel(roboforexMT4, sheet_name= 0)
            df = df.set_index('datetime')
            df['pct_change'] = df['Balance'].pct_change().cumsum() *100
            
            df2 = pd.read_excel(roboforexMT4DD, sheet_name= 1)
            df2 = df2.set_index('datetime')            
            
            x = df.index
            x2 = df2.index
            y = df['Balance']
            y2 = df['pct_change']
            y3 = [x for x in df2['d_ret'] if x < 0]

            fig = go.Figure(go.Scatter(x=x, y=y, mode='lines', name='Balance', line_shape='spline'))
            fig.update_layout(title='Crecimiento del balance DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento ($)')

            fig2 = go.Figure(go.Scatter(x=x, y=y2, mode='lines', name='Crecimiento', line_shape='hvh'))
            fig2.update_layout(title='Crecimiento porcentual DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Crecimiento (%)')
            
            fig3 = go.Figure(go.Scatter(x=x2, y=y3, mode='lines', name='Drawdown máximo', line_shape='spline'))
            fig3.update_layout(title='Drawdown máximo DeepAtlas CopyFx', xaxis_title='Fecha', yaxis_title='Drawdown (%)')
            
            st.plotly_chart(fig)
            st.write('''
                    pass.
                    ''')
            
            st.plotly_chart(fig2)
            st.write('''
                    pass.
                    ''')
            
            st.plotly_chart(fig3)
            st.write('''
                    pass.
                     ''')

        if submenu == 'DeepAtlas vs EURUSD':
            st.write('''Este mes se logró un alpha de 1.84% con respecto al par de divisas EURUSD, lo cuál muestra que la estrategia de DeepAtlas CopyFx
            es más rentable que el par de divisas en el que opera.''')
            benchmark = "Data/2022/5. Enero2022/DAMT4_vs_EURUSD_Enero2022.html"
            html = open(benchmark, 'r', encoding='utf-8').read()
            components.html(html, height=7000, width=1200)