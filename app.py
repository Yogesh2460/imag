import streamlit as st
from PIL import Image, ImageDraw, ImageFont

st.title("🖼️ Text to Image Generator")

text = st.text_input("Enter your text:", "Hello, Streamlit!")

if st.button("Generate Image"):
    img = Image.new('RGB', (600, 300), color='white')
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    x = (600 - text_width) // 2
    y = (300 - text_height) // 2
    draw.text((x, y), text, font=font, fill='black')

    img.save("output.png")
    st.image("output.png", caption="Generated Image")
