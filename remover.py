#import ElementTree
from xml.etree import ElementTree 
#set input file
import Tkinter,tkFileDialog
root = Tkinter.Tk()
file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
tree = ElementTree.parse(file) 
# load all of the name columns and check if they start with VFX_ (to search another column - replace //name with the name of the column)
for searchresult in tree.findall("//name"): 
	if searchresult.text.startswith('VFX_'):
		# list found results
		print "Found this: ", searchresult.text
		datalist = list(searchresult.text)
		#Don't mess with line below:
		numofchars = 0
		# This is a loop that removes the last character until numofchars hits the targe value
		# modify the value below to choose how many characters should be removed. 
		while numofchars < 4:
			datalist.pop()
			numofchars += 1

		
		print "Changed to this: ", "".join(datalist)
		searchresult.text="".join(datalist)

#write results back to new file
myFormats = [
    ('SCRATCH XML','*.xml')]

root = Tkinter.Tk()
fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the file as...")
if len(fileName ) > 0:
	tree.write(fileName)