import requests
from pydantic import BaseModel,Field,RootModel,field_validator,field_serializer
import streamlit as st
import source
from source import Root


try:
    data_str = source.download_youbike()
except Exception as e:
    st.error(e)

else:
    root = Root.model_validate_json(data_str)
    data = root.model_dump()

    areas:list[str] = list(set(map(lambda value:value['行政區'],data)))

    def area_change():
        print("Hello!")

    # option = st.selectbox("請選擇行政區",areas)
    # st.write("您選擇:", option)

    with st.sidebar:
        st.selectbox(":orange[請選擇行政區]",options=areas,on_change=area_change,key='sarea')
        st.session_state




