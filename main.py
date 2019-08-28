# -*- coding: utf-8 -*-

#python main.py -c sample_testset/crops/ -f sample_testset/images/ -o out.json

import cv2, glob, time, argparse, json


class MD:
    data_dictionary = {}
    print("class MD")
    def template_matcher(self,full_img,crop_img):
        #print("in template_matcher")
        method = eval('cv2.TM_CCOEFF_NORMED')
        res = cv2.matchTemplate(full_img,crop_img,method)#threshold=0.8          
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val>0.8:
            print("max_val",max_val) 
            return max_loc , max_val
            
    
    def get_match(self, full,crops,outputFileName):
        print("in get_match")
        self.data_dictionary = {}
        for full_image in glob.glob(full+"*"):
            self.sub_dictionary = {}
            full_img = cv2.imread(full_image)
            h1, w1, c1 = full_img.shape
            for crop_image in glob.glob(crops+"*"):
                crop_img = cv2.imread(crop_image)
                h2, w2, c2 = crop_img.shape
                if c1==c2 and h2<=h1 and w2<=w1:
                    method = eval('cv2.TM_CCOEFF_NORMED')
                    res = cv2.matchTemplate(full_img,crop_img,method)   
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
                    if max_val>0.98:
                        print("max_val",max_val) 
                        full_name = full_image.split("/")[-1].replace(".jpg","")
                        crop_name = crop_image.split("/")[-1].replace(".jpg","")
                        print(full_name,crop_name)
                        self.sub_dictionary[crop_name] = [max_loc[0],max_loc[1],max_loc[0]+w2,max_loc[1]+h2]    
            self.data_dictionary[full_name] = self.sub_dictionary
            print(self.data_dictionary)
  
        self.data_dictionary = json.dumps(self.data_dictionary)
        self.data_dictionary  = json.loads(self.data_dictionary )
        with open(outputFileName, 'w') as fp:
           
            json.dump(self.data_dictionary, fp, indent=5)
                
    
    
    
def main():
    print("in main")
    startTime = time.time()
    mdObject = MD()
    ap = argparse.ArgumentParser()
    ap.add_argument("-c", "--crops", required=True,
	help="crops image location")
    ap.add_argument("-f", "--full", required=True,
	help="full image location")
    ap.add_argument("-o", "--out", required=True,
	help="output file name")
    args = vars(ap.parse_args())
    cropsLocation = args['crops']
    fullImageLocation = args['full']
    outputFileName = args['out']
    print("cropsLocation:",cropsLocation)
    print("fullImageLocation:",fullImageLocation)
    print("outputFileName:",outputFileName)   
    
    mdObject.get_match(fullImageLocation,cropsLocation,outputFileName)
    
    
    endTime = time.time()
    print("---------Total Processing Time--------",endTime - startTime)
    
    
    
    
if __name__ == "__main__":
    main()
    
    
    
    
    