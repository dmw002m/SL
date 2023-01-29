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

st.markdown('</div>', unsafe_allow_html=True)

# Add the draggable functionality
st.write("""
<script>
  function dragStart(event) {
    event.dataTransfer.setData("text", event.target.id);
  }
  
  function allowDrop(event) {
    event.preventDefault();
  }
  
  function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    event.target.appendChild(document.getElementById(data));
  }
</script>
""", unsafe_allow_html=True)

st.write("""
<script>
  function drag(event) {
    event.dataTransfer.setData("text", event.target.id);
    event.dataTransfer.setData("x", event.clientX);
    event.dataTransfer.setData("y", event.clientY);
  }
  
  function drop(event) {
    event.preventDefault();
    var data = event.dataTransfer.getData("text");
    var rect = document.getElementById(data);
    var x = event.clientX - event.dataTransfer.getData("x") + parseInt(rect.style.left);
    var y = event.clientY - event.dataTransfer.getData("y") + parseInt(rect.style.top);
    rect.style.left = x + "px";
    rect.style.top = y + "px";
  }
  
  var canvas = document.getElementById("canvas");
  canvas.addEventListener("drop", drop);
  canvas.addEventListener("dragover", function(event) {
    event.preventDefault();
  });
</script>
""", unsafe_allow_html=True)
