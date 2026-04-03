class AiModel:
    api="kkfghjklm567"
    
    def __init__(self):

        pass

    def Create_ai_image(self,image_name,pixel,color):

        self.image_name=image_name
        self.pixel=pixel
        self.color=color



        print("creating ai image")

        return f"your image name is {self.image_name} and pixel is {self.pixel} and color is {self.color}"
    
    def Create_ai_video(self,video_name,duration,quality):
        self.video_name=video_name
        self.duration=duration
        self.quality=quality

        print("creating ai video")

        return f"your video name is {self.video_name} and duration is {self.duration} and quality is {self.quality}"
    
    def Create_ai_text(self,text_name,language,word_count):
        self.text_name=text_name
        self.language=language
        self.word_count=word_count

        print("creating ai text")

        return f"your text name is {self.text_name} and language is {self.language} and word count is {self.word_count}"
    
    @classmethod
    def Show_api(cls):
        print(f"the api key is {cls.api}")

    @staticmethod
    def Show_info():
        print("this is ai model class that can create ai image,video and text")



ai=AiModel()
print(ai.Create_ai_image("sunset",1080,"red"))
print(ai.Create_ai_video("nature",60,"hd"))
print(ai.Create_ai_text("hello world","english",100))
AiModel.Show_api()
AiModel.Show_info()

