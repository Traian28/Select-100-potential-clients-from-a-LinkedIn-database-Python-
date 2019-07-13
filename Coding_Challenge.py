from tkinter import*
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog

try:
	root = Tk()
	root.withdraw() #Remove tkinter background console
	MessageBox.showinfo("Welcome","Please select the PEOPLE.in file to filter")

	rute = FileDialog.askopenfilename(title="Open file")
	file = open (rute,'r')
	newlist=[] #auxiliar list to segment the data of each line of the file
	keywords1 = ['software','computer','internet','technology','telecommunications','electronics','development','games'] #keywords according to Industry field
	keywords2 = ['president','manager','director','chief','partner','associate','executive'] #keywords according to CurrentRole field

	try:
		for line in file :
			if line[-1] == '\n': #delete line break 
				line = line[:-1]
			lista = line.split("|")	#insert elements separated by | in a list so it is easier to handle it
			flag = False #this flag is use in order not to insert duplicate IDs and also to avoid continue looking for keywords when the ID has already been selected
			for key1 in keywords1:
				if key1 in lista[5].lower():
					for key2 in keywords2:
						if key2 in lista[3].lower():
							newlist.append(lista) #if at least one of the industry and role keywords exist then the ID is added to the new list
							flag = True #change the flag to true to stop the search of keywords
					if flag:
						break
				if flag:
					break				

		newlist.sort(reverse=True, key=lambda x: (x[6],x[7])) #as there are more than 100 potential clients, sort it by numberOfRecomendations and by NumberOfConnections
		newlist=newlist[0:100] #select only the first 100 potential clients of the complete list
		file.close()
		rute=rute.replace('people.in','people.out')
		newfile = open (rute,'w')

		for linea in newlist:
			newfile.write(linea[0]+'\n') #insert the Id of the potential clients into the new file

		newfile.close()

		MessageBox.showinfo ("Program OK","A file called PEOPLE.out with the ID of 100 potential clients has been generated."+"\n"+"\n"+"The new file is in the same location as PEOPLE.in")

	except: MessageBox.showerror ("Error","The selected file is not the correct one.")

except FileNotFoundError:
	MessageBox.showerror ("Error","Please select the location of PEOPLE.in file.")