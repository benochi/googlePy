wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for item, colors in wardrobe.items():
	for color in colors:
		print("{} {}".format(color, item))
