import streamlit as st
import streamlit.components.v1 as components

st.markdown('''
    <style>
    .rectangle {
        position: absolute;
        width: 100px;
        height: 100px;
        background-color: red;
    }
    </style>
''', unsafe_allow_html=True)


rectangles = []
def create_rectangle(x, y):
    rectangles.append({"x": x, "y": y, "w": 100, "h": 100})
def move_rectangle(i, dx, dy):
    rectangles[i]["x"] += dx
    rectangles[i]["y"] += dy
def delete_rectangle(i):
    rectangles.pop(i)
canvas_width = 600
canvas_height = 400
st.empty()
st.markdown('''
    <div id='canvas' style='position: relative; width: 600px; height: 400px; background-color: #ddd;'></div>
''', unsafe_allow_html = True)

if st.button("Add Rectangle"):
    create_rectangle(0, 0)

for i, rectangle in enumerate(rectangles):
    st.write(f"""
        <div id='rectangle-{i}' class='rectangle' style='left: {rectangle["x"]}px; top: {rectangle["y"]}px;'></div>
    """, unsafe_allow_html=True)

    components.dnd(
        f"rectangle-{i}", move_rectangle, delete_func=delete_rectangle, args=(i,)
    )
