import streamlit as st
import intro
import pollution
import sales
import conclusion

st.set_page_config(page_title='EDA', page_icon=':car:', layout="wide")


'''def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("../css/style.css")'''

st.title('El coche eléctrico en Europa')

st.sidebar.text('Navegación')

menu = st.sidebar.selectbox('Menu:',
                            options=['Intro', 'Contaminación', 'Ventas', 'Conclusiones'])


config = {'displayModeBar': False}

if menu == 'Intro':
    intro.intro()
    # st.sidebar.button("Hablemos de contaminacion")

elif menu == 'Contaminación':
    pollution.pollution(config)

elif menu == 'Ventas':
    sales.sales(config)

elif menu == 'Conclusiones':
    conclusion.conclusion()

else:
    intro.intro()
