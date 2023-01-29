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

st.write(
    """
<script>
  var rectangles = document.getElementsByClassName("rectangle");
  for (var i = 0; i < rectangles.length; i++) {
    rectangles[i].setAttribute("draggable", "true");
    rectangles[i].setAttribute("ondragstart", "dragStart(event)");
    rectangles[i].setAttribute("ondrop", "drop(event)");
    rectangles[i].setAttribute("ondragover", "allowDrop(event)");
  }
</script>
""",
    unsafe_allow_html=True,
)
