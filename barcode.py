import treepoem

user_options={"columns":14}
#user_options={"eclevel":5,"columns":14, "width":20, "height":2}	#use this if you want to specify dimensions (inches) before the barcode generation
size=1000,250 #width, height in pixels

with open("data.txt","r") as f:
	for n,line in enumerate(f,1):
		text = line.replace("\\n","\n")
		image = treepoem.generate_barcode(barcode_type='pdf417', data=text, options=user_options)
		#image.convert('1').save(str(n)+".png")	#use this instead of the following line
		image.convert('1').resize(size).save(str(n)+".png")