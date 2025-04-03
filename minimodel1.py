# import torch
# from diffusers import StableDiffusionPipeline
# pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16)

# pipe = pipe.to("cuda")


# #audio_to_text

# import speech_recognition as sr
# from googletrans import Translator
# from fastdtw import fastdtw
# import numpy as np

# recognizer = sr.Recognizer()
# audio_file_path = "E:\MINI project 2 data collection\audio.wav\sample1aud.wav"

# def extract_mfcc(audio_file_path):
#     with sr.AudioFile(audio_file_path) as source:
#         audio_data = recognizer.record(source)
#     return recognizer.recognize_google(audio_data, language='ta-IN')

# try:
#     recognized_text = extract_mfcc(audio_file_path)
#     print("Transcript: " + recognized_text)
# except sr.UnknownValueError:
#     print("Audio Recognizer could not understand the audio")
# except sr.RequestError as e:
#     print(f"Could not request results from the audio search: {e}")

# audio_file2_path = "E:\MINI project 2 data collection\audio.wav\sample2aud.wav"

# try:
#     recognized_text2 = extract_mfcc(audio_file2_path)
#     print("Transcript: " + recognized_text2)
# except sr.UnknownValueError:
#     print("Audio Recognizer could not understand the second audio")
# except sr.RequestError as e:
#     print(f"Could not request results from the second audio search: {e}")

# mfcc_features1 = np.array([1, 2, 3, 4, 5])
# mfcc_features2 = np.array([2, 3, 4, 5, 6])

# distance, path = fastdtw(mfcc_features1, mfcc_features2)

# print("DTW Distance between the two audio files:", distance)

# translator = Translator()
# translated_text1 = translator.translate(recognized_text, src='ta', dest='en')
# translated_text2= translator.translate(recognized_text2, src='ta', dest='en')
# print("Translated Text: " + translated_text1.text)
# print("Translated Text: " + translated_text2.text)

# #model

# from PIL import Image

# def image_grid(imgs, rows, cols):
#     assert len(imgs) == rows*cols

#     w, h = imgs[0].size
#     grid = Image.new('RGB', size=(cols*w, rows*h))
#     grid_w, grid_h = grid.size

#     for i, img in enumerate(imgs):
#         grid.paste(img, box=(i%cols*w, i//cols*h))
#     return grid

# #images

# num_images = 3
# prompt = ["Two cats are sitting on a couch, eating spaghetti and watching TV"] * num_images

# images = pipe(prompt).images

# grid = image_grid(images, rows=1, cols=3)
# grid
import torch
print(torch.cuda.is_available())