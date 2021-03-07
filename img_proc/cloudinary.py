import requests
from cloudinary.uploader import upload
import cloudinary
from config import log

cloudinary.config(
  cloud_name = 'dtmd0zvey',  
  api_key = '336926953387248',  
  api_secret = 'XiFAv-ZuHYCjEnGqfxP4-XxnLhQ'  
)


diametr_dict = {'w_85': [20.00, 21.99],
                'w_90': [22.00, 23.99],
                'w_100': [24.00, 25.99],
                'w_105': [26.00, 27.99],
                'w_115': [28.00, 29.99],
                'w_120': [30.00, 31.99],
                'w_130': [32.00, 33.99],
                'w_135': [34.00, 35.99],
                'w_140': [36.00, 37.99],
                'w_150': [38.00, 40.99],
                'w_154': [41.00, 43.99],
                'w_156': [44.00, 47.99]
                }
              

def upload(link:str, art:str) -> None:
  cloudinary.uploader.upload(link, public_id = art)

def get_width(d:str) -> str:
  d = float(d)
  for key, value in diametr_dict.items():
    if d >= value[0] and d <= value[1]:
      return key

def get_small_img(d:str, art:str):
  width = get_width(d)
  url= 'https://res.cloudinary.com/dtmd0zvey/image/upload/e_trim:20/c_fit,{}/b_rgb:ffffff,bo_0px_solid_rgb:ffffff,c_lpad,f_jpg,g_center,h_300,o_100,q_100,w_170/{}.png'.format(width, art)
  filename= art + '.jpg'
  response=requests.get(url)
  if response.status_code==200:
    with open(r'/home/anton/AI_Image/small/' + filename,'wb') as imgfile:
      imgfile.write(response.content)
      log.info('Art: {} Diametr: {} Small img was save succsess'.format(art, d))
  else:
    log.error('Art: {} Diametr: {} Small img was save with error'.format(art, d))

def get_big_img(art:str):
  url_2= 'https://res.cloudinary.com/dtmd0zvey/image/upload/e_trim:20/c_fit,w_440/f_jpg,q_100/'+ art +'.png'
  filename= art + '.jpg'
  response=requests.get(url_2)
  if response.status_code==200:
    with open(r'/home/anton/AI_Image/big/' + filename,'wb') as imgfile:
      imgfile.write(response.content)
      log.info('Art: {}. Big img was save succsess'.format(art))
  else:
    log.info('Art: {}. Big img was save with error'.format(art))


