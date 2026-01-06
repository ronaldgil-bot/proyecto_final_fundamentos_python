from PIL import Image, ImageDraw

imagenes = []

for i in range(5):
    img = Image.new("RGB", (200, 200), "white")
    dibujo = ImageDraw.Draw(img)

    dibujo.rectangle(
        [20 + i*20, 50, 80 + i*20, 150],
        fill="red"
    )

    imagenes.append(img)

imagenes[0].save(
    "animacion.gif",
    save_all=True,
    append_images=imagenes[1:],
    duration=400,
    loop=0
)

print("GIF creado correctamente")