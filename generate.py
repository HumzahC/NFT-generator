#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image 
from IPython.display import display 
import random
import json


# In[2]:


# Each image is made up a series of traits
# The weightings for each trait drive the rarity and add up to 100%

background = ["Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose",] 
background_weights = [16.4,3,16.4,9,9,16.4,16.4,16.4,7]

cat = ["Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose","White"]
cat_weights = [15.4,3,15.4,9,9,15.4,15.4,15.4,7,5]

nose = ["Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose","White"] 
nose_weights = [15.4,3,15.4,9,9,15.4,15.4,15.4,7,5]

glasses = ["Blank","Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose","White","BlueAv","GoldAv","GreenAv","LightblueAv","LimeAv", "OrangeAv", "PurpleAv", "RedAv", "RoseAv","WhiteAv"]
glasses_weights = [21,6.7,1.5,6.7,4.5,4.5,6.7,6.7,6.7,4.5,2.5,  5.6,0.4,5.6,3.4,3.4,5.6,5.6,5.6,3.4,1.4]

head = ["Blank","Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose","White","BlueCrown","GoldCrown","GreenCrown","LightblueCrown","LimeCrown", "OrangeCrown", "PurpleCrown", "RedCrown", "RoseCrown","WhiteCrown","BlueHat","GoldHat","GreenHat","LightblueHat","LimeHat", "OrangeHat", "PurpleHat", "RedHat", "RoseHat","WhiteHat"]
head_weights = [15.02,  4.14,  1,  4.14,  3,  3, 4.14,  4.14,  4.14,  2.3,  1.6,      3.39,  0.25,  3.39,  2.25,  2.25, 3.39,  3.39,  3.39,  1.55,  0.85,      3.89,  0.75,  3.89,  2.75,  2.75, 3.89,  3.89,  3.89,  2.05,  1.35]

neck = ["Blank","Blue","Gold","Green","Lightblue","Lime", "Orange", "Purple", "Red", "Rose","White","BluePearl","GoldPearl","GreenPearl","LightbluePearl","LimePearl", "OrangePearl", "PurplePearl", "RedPearl", "Rose","WhitePearl"]
neck_weights = [10,6.7,1.5,6.7,4.5,4.5,6.7,6.7,6.7,4.5,2.5,6.7,1.5,6.7,4.5,4.5,6.7,6.7,6.7,4.5,2.5]

# Dictionary variable for each trait. 
# Each trait corresponds to its file name

background_files = {
    "Blue":"blue",
    "Gold":"gold",
    "Green":"green",
    "Lightblue":"lightblue",
    "Lime":"lime",
    "Orange":"orange",
    "Purple":"purple",
    "Red":"red",
    "Rose":"rose"
}
cat_files = {
    "Blue":"cat-polished-blue",
    "Gold":"cat-polished-gold",
    "Green":"cat-polished-green",
    "Lightblue":"cat-polished-lightblue",
    "Lime":"cat-polished-lime",
    "Orange":"cat-polished-orange",
    "Purple":"cat-polished-purple",
    "Red":"cat-polished-red",
    "Rose":"cat-polished-rose",
    "White":"cat-polished-white"
    
}

nose_files = {
    "Blue":"blue-nose",
    "Gold":"gold-nose",
    "Green":"green-nose",
    "Lightblue":"lightblue-nose",
    "Lime":"lime-nose",
    "Orange":"orange-nose",
    "Purple":"purple-nose",
    "Red":"red-nose",
    "Rose":"rose-nose",
    "White":"white-nose"
    
          
}
glasses_files = {
    "Blank": "glasses-blank",
    "Blue":"glasses-blue",
    "Gold":"glasses-gold",
    "Green":"glasses-green",
    "Lightblue":"glasses-lightblue",
    "Lime":"glasses-lime",
    "Orange":"glasses-orange",
    "Purple":"glasses-purple",
    "Red":"glasses-red",
    "Rose":"glasses-rose",
    "White":"glasses-white",
    
    "BlueAv":"aviators-blue",
    "GoldAv":"aviators-gold",
    "GreenAv":"aviators-green",
    "LightblueAv":"aviators-lightblue",
    "LimeAv":"aviators-lime",
    "OrangeAv":"aviators-orange",
    "PurpleAv":"aviators-purple",
    "RedAv":"aviators-red",
    "RoseAv":"aviators-rose",
    "WhiteAv":"aviators-white",
    
}

head_files = {
    "Blank": "cap-blank",
    "Blue":"cap-blue",
    "Gold":"cap-gold",
    "Green":"cap-green",
    "Lightblue":"cap-lightblue",
    "Lime":"cap-lime",
    "Orange":"cap-orange",
    "Purple":"cap-purple",
    "Red":"cap-red",
    "Rose":"cap-rose",
    "White":"cap-white",
    
    "BlueCrown":"crown-blue",
    "GoldCrown":"crown-gold",
    "GreenCrown":"crown-green",
    "LightblueCrown":"crown-lightblue",
    "LimeCrown":"crown-lime",
    "OrangeCrown":"crown-orange",
    "PurpleCrown":"crown-purple",
    "RedCrown":"crown-red",
    "RoseCrown":"crown-rose",
    "WhiteCrown":"crown-white",
    
    "BlueHat":"hat-blue",
    "GoldHat":"hat-gold",
    "GreenHat":"hat-green",
    "LightblueHat":"hat-lightblue",
    "LimeHat":"hat-lime",
    "OrangeHat":"hat-orange",
    "PurpleHat":"hat-purple",
    "RedHat":"hat-red",
    "RoseHat":"hat-rose",
    "WhiteHat":"hat-white",

}

neck_files = {
    "Blank": "bowtie-blank",
    "Blue":"bowtie-blue",
    "Gold":"bowtie-gold",
    "Green":"bowtie-green",
    "Lightblue":"bowtie-lightblue",
    "Lime":"bowtie-lime",
    "Orange":"bowtie-orange",
    "Purple":"bowtie-purple",
    "Red":"bowtie-red",
    "Rose":"bowtie-rose",
    "White":"bowtie-white",
    
    "BluePearl":"pearl-blue",
    "GoldPearl":"pearl-gold",
    "GreenPearl":"pearl-green",
    "LightbluePearl":"pearl-lightblue",
    "LimePearl":"pearl-lime",
    "OrangePearl":"pearl-orange",
    "PurplePearl":"pearl-purple",
    "RedPearl":"pearl-red",
    "RosePearl":"pearl-rose",
    "WhitePearl":"pearl-white",
    
}


# In[3]:


## Generate Traits

TOTAL_IMAGES = 300 # Number of random unique images we want to generate

all_images = [] 

# A recursive function to generate unique image combinations
def create_new_image():
    
    new_image = {} #

    # For each trait category, select a random trait based on the weightings 
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Cat"] = random.choices(cat, cat_weights)[0]
    new_image ["Nose"] = random.choices(nose, nose_weights)[0]
    new_image ["Glasses"] = random.choices(glasses, glasses_weights)[0]
    new_image ["Head"] = random.choices(head, head_weights)[0]
    new_image ["Neck"] = random.choices(neck, neck_weights)[0]
    
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
    
    
# Generate the unique combinations based on trait weightings
for i in range(TOTAL_IMAGES): 
    
    new_trait_image = create_new_image()
    
    all_images.append(new_trait_image)
    


# In[4]:


# Returns true if all images are unique
def all_images_unique(all_images):
    seen = list()
    return not any(i in seen or seen.append(i) for i in all_images)

print("Are all images unique?", all_images_unique(all_images))


# In[5]:


# Add token Id to each image
i = 0
for item in all_images:
    item["tokenId"] = i
    i = i + 1


# In[6]:


print(all_images)


# In[7]:


# Get Trait Counts

background_count = {}
for item in background:
    background_count[item] = 0
    
cat_count = {}
for item in cat:
    cat_count[item] = 0

nose_count = {}
for item in nose:
    nose_count[item] = 0
    
neck_count = {}
for item in neck:
    neck_count[item] = 0 
    
glasses_count = {}
for item in glasses:
    glasses_count[item] = 0 
    
head_count = {}
for item in head:
    head_count[item] = 0   
     
   
    
for image in all_images:
    background_count[image["Background"]] += 1
    cat_count[image["Cat"]] += 1
    nose_count[image["Nose"]] += 1
    glasses_count[image["Glasses"]] += 1
    head_count[image["Head"]] += 1
    neck_count[image["Neck"]] += 1

    
print(background_count)
print(cat_count)
print(nose_count)
print(glasses_count)
print(head_count)
print(neck_count)


# In[8]:


#### Generate Metadata for all Traits 
METADATA_FILE_NAME = './metadata/all-traits.json'; 
with open(METADATA_FILE_NAME, 'w') as outfile:
    json.dump(all_images, outfile, indent=7)


# In[9]:



  
#### Generate Images    
for item in all_images:

  im1 = Image.open(f'./trait-layers/backgrounds/{background_files[item["Background"]]}.png').convert('RGBA')
  im2 = Image.open(f'./trait-layers/cat/{cat_files[item["Cat"]]}.png').convert('RGBA')
  im3 = Image.open(f'./trait-layers/nose/{nose_files[item["Nose"]]}.png').convert('RGBA')
  im4 = Image.open(f'./trait-layers/glasses/{glasses_files[item["Glasses"]]}.png').convert('RGBA')
  im5 = Image.open(f'./trait-layers/head/{head_files[item["Head"]]}.png').convert('RGBA')
  im6 = Image.open(f'./trait-layers/neck/{neck_files[item["Neck"]]}.png').convert('RGBA')
  
  #Create each composite
  com1 = Image.alpha_composite(im1, im2)
  com2 = Image.alpha_composite(com1, im3)
  com3 = Image.alpha_composite(com2, im4)
  com4 = Image.alpha_composite(com3, im5)
  com5 = Image.alpha_composite(com4, im6)

  
  
  #Convert to RGB
  rgb_im = com5.convert('RGB')
  file_name = str(item["tokenId"]) + ".png"
  rgb_im.save("./images/" + file_name)
  
  
  


# In[10]:


#### Generate Metadata for each Image    

f = open('./metadata/all-traits.json',) 
data = json.load(f)


IMAGES_BASE_URI = "ADD_IMAGES_BASE_URI_HERE"
PROJECT_NAME = "ADD_PROJECT_NAME_HERE"

def getAttribute(key, value):
    return {
        "trait_type": key,
        "value": value
    }
for i in data:
    token_id = i['tokenId']
    token = {
        "image": IMAGES_BASE_URI + str(token_id) + '.png',
        "tokenId": token_id,
        "name": PROJECT_NAME + ' ' + str(token_id),
        "attributes": []
    }
    token["attributes"].append(getAttribute("Background", i["Background"]))
    token["attributes"].append(getAttribute("Cat", i["Cat"]))
    token["attributes"].append(getAttribute("Nose", i["Nose"]))
    token["attributes"].append(getAttribute("Glasses", i["Glasses"]))
    token["attributes"].append(getAttribute("Head", i["Head"]))
    token["attributes"].append(getAttribute("Neck", i["Neck"]))
    
    
    with open('./metadata/' + str(token_id), 'w') as outfile:
        json.dump(token, outfile, indent=7)
f.close()


# In[ ]:





# In[11]:


[generate.ipynb]


# In[ ]:




