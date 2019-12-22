from PIL import Image

im1 = Image.open("image.png")

listaImagens = [im1]

im1.save("arquivo.pdf", "PDF" ,resolution=100.0, save=True, append_image=listaImagens)
