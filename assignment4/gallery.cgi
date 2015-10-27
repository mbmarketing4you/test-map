#!/usr/bin/python
import os
from shared import *

class ImageTile():
	"""Class that holds the thumbnails and photo paths, used for easy generation of page.
	fileName should be without the extension, so we can refer to the thumbnail and text
	"""
	def getTitle(self, path):
		with open(path, 'r') as file:
			return file.read()

	def __init__(self, fileName):
		self.fileName = fileName[:-4] # safe because we control what format goes in that folder
		self.filePath = os.path.join(UPLOAD_DIR, self.fileName) #also of no extension
		self.imgFilePath = self.filePath + ".jpg"
		self.title = self.getTitle(self.filePath + ".txt")
		self.thumbnail = self.filePath + "_tn.jpg"

	def tile(self):
		return """<img src="%(thumbnail)s" alt="%(filePath)s" /> <br/>
				<h1> %(title)s </h1> <br/>
				<a href="edit.cgi?id=%(filename)s"> Edit </a> 
				<a href="delete.cgi?id=%(filename)s"> Delete </a>
				<br/>
		""" % {'thumbnail': self.thumbnail, 'filePath': self.filePath, 
				'title': self.title, 'filename': self.fileName}

def generateTiles():
	listOfFiles = os.listdir(UPLOAD_DIR)
	pictures = []
	htmlString = "<tr>" # start table row
	for a in range(len(listOfFiles)):
		if '.txt' in listOfFiles[a]: # string checking has issues, avoid _tn, just use txt. 
			pictures.append(listOfFiles[a])
		# if '.txt' == fileName[-4:] or 'tn' == fileName[-6:-4]:
		# if "_tn" in fileName or ".txt" in fileName: # it's werid this doesn't work...
	for i in range(len(pictures)):
		if(i%4 == 0 and i != 0):
			htmlString += "</tr> <tr>" #next row
		htmlString += "<td>%(tile)s</td>" % {'tile': ImageTile(pictures[i]).tile()}
	htmlString += "</tr>"
	return htmlString


body = """<a href="gallery.cgi"><button type=button>Refresh</button></a> 
		  <a href="upload.cgi"><button type=button>Upload New Picture</button></a>
		  <table>
		  	%(allTiles)s
		  </table>
	   """ % { 'allTiles': generateTiles() }


strings = {
	'windowTitle': "Picture Gallery",
	'title': "Picture Gallery",
	'body': body
}

print HTML_TEMPLATE % strings