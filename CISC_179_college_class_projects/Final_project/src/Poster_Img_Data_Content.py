from PIL import Image, ImageTk
class PosterImgData_Content:
    def __init__(self):
        self.posterImgList = ["stock_poster1_img.jpg", "stock_poster2_img.jpg"]
    def poster1Func(self, tk, para2):
        #! poster 1
        try:
           para2.openImg = Image.open(self.posterImgList[0])
           para2.openImg = para2.openImg.resize((670, 350), Image.LANCZOS)
           para2.poster1 = ImageTk.PhotoImage(para2.openImg)
           para2.poster_label = tk.Label(para2.top_frame, image=para2.poster1)
           return para2.poster_label
        #? Display error message if there's any error occurs while creating the poster 1
        except Exception as e:
            print(f"Poster Image Error: {e}.\n"+\
                f"Method: poster1Func().\n"+\
                f"Class: PosterImgData_Content.\n"+\
                f"File: Poster_Img_Data_Content.py.\n")

    def poster2Func(self, tk, para2):
        #! poster 2
        try:
            para2.openImg2 = Image.open(self.posterImgList[1])
            para2.openImg2 = para2.openImg2.resize((670, 350), Image.LANCZOS)
            para2.poster2 = ImageTk.PhotoImage(para2.openImg2)
            para2.poster_label2 = tk.Label(para2.top_frame, image=para2.poster2)
            return para2.poster_label2
        #? Display error message if there's any error occurs while creating the poster 2
        except Exception as e:
            print(f"Poster Image Error: {e}.\n"+\
                f"Method: poster2Func().\n"+\
                f"Class: PosterImgData_Content.\n"+\
                f"File: Poster_Img_Data_Content.py.\n")

PosterImgagesData = PosterImgData_Content()
        


    