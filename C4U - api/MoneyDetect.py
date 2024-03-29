import glob
import cv2



def getMoneyValue(myPic):
	index = {}
	images = {}
	dataset="/home/Arty0091/mysite/DB"
	for imagePath in glob.glob(dataset + "/*.png"):
		filename = imagePath[imagePath.rfind("/") + 1:]
		image = cv2.imread(imagePath)
		images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
		hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
			[0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist, hist).flatten()
		index[filename] = hist

	filename=myPic
	image = cv2.imread(filename)
	images[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],
		[0, 256, 0, 256, 0, 256])
	hist = cv2.normalize(hist, hist).flatten()
	index[filename] = hist


	method=cv2.HISTCMP_BHATTACHARYYA
	results = {}
	reverse = False
	for (k, hist) in index.items():
		d = cv2.compareHist(index[myPic], hist, method)
		results[k] = d
	results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)
	if(results[1][0]<0.5) : return "It's " + results[1][1][0:3]+' Dirham'
	else: return "This is not money, you can try again"
