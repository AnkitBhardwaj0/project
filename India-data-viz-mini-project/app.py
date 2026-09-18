import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
df=pd.read_csv('india.csv')
list_of_states=list(df['State'].unique())
list_of_states.insert(0,'over all india')

st.sidebar.title('India data visualization')

selected_state=st.sidebar.selectbox('select a state',list_of_states)
primary = st.sidebar.selectbox('select primary parameter ',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('select secondary parameter ',sorted(df.columns[5:]))

plot=st.sidebar.button('plot Graph')

if plot:
     st.text('size represent primary parameter')
     st.text('color represent secondary parameter')
     if selected_state=='over all india':
          #plot for india
          center={'lat':df['Latitude'].mean(),'lon':df['Longitude'].mean()}
          fig=px.scatter_map(df,lat='Latitude',lon='Longitude',center=center,zoom=4,size=primary,color=secondary,size_max=35,width=1200,height=700,map_style='carto-positron',hover_name='District',color_continuous_scale='IceFire')
          st.plotly_chart(fig,use_container_width=True)
          
     else:
          #plot for state
          state_df=df[df['State']==selected_state]
          center={'lat':state_df['Latitude'].mean(),'lon':state_df['Longitude'].mean()}
          fig=px.scatter_map(state_df,lat='Latitude',lon='Longitude',center=center,zoom=4,size=primary,color=secondary,size_max=35,width=1200,height=700,map_style='carto-positron',hover_name='District',color_continuous_scale='Viridis')
          st.plotly_chart(fig,use_container_width=True)