#Vẽ logo MixiGaming chỉ với 3 dòng Code
import ascii_magic
output = ascii_magic.from_image_file("tuna.jpg", columns=200, char="#")
ascii_magic.to_terminal(output)
