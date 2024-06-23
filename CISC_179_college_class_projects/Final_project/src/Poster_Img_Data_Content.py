from PIL import Image, ImageTk
class PosterImgData_Content():
    def __init__(self):
        self.posterImgList = ["stock_poster1_img.jpg", "stock_poster2_img.jpg"]
        
    def poster1Func(self, tk, para2):
        #poster1
        para2.openImg = Image.open(self.posterImgList[0])
        para2.openImg = para2.openImg.resize((670, 350), Image.LANCZOS)
        para2.poster1 = ImageTk.PhotoImage(para2.openImg)
        para2.poster_label = tk.Label(para2.top_frame, image=para2.poster1)
        return para2.poster_label

    def poster2Func(self, tk, para2):
        #poster2
        para2.openImg2 = Image.open(self.posterImgList[1])
        para2.openImg2 = para2.openImg2.resize((670, 350), Image.LANCZOS)
        para2.poster2 = ImageTk.PhotoImage(para2.openImg2)
        para2.poster_label2 = tk.Label(para2.top_frame, image=para2.poster2)
        return para2.poster_label2

PosterImgagesData = PosterImgData_Content()
        


    