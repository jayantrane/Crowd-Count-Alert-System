import os
import torch
import numpy as np
import pandas as pd

from src.crowd_count import CrowdCounter
from src import network
from src.data_loader import ImageDataLoader
from src import utils
from scipy.io import loadmat


def testimage(modelname, camname):
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = False
    vis = False
    save_output = False
    
    #test data and model file path
    if camname == 0:
        data_path =  '../data/test/images/'
    else:
        data_path =  '../data/test/images2/'
    
    if modelname == 'A':
        model_path = './final_models/cmtl_shtechA_204.h5'
    else:
        model_path = './final_models/cmtl_shtechB_768.h5'
    print("Model name:" , modelname," Camname: ", camname)
    gt_flag = False
    if gt_flag:
        gt_path = '../dataset/ShanghaiTech/part_A/test_data/ground_truth/'
    
    
    # =============================================================================
    # for i in range(1, 4):
    #     gt_name = os.path.join(gt_path,'img_' + format(i, '04') + '_ann.mat')
    #     print(gt_name)
    #     x = loadmat(gt_name)
    #     print (len(x['annPoints']))
    # 
    # =============================================================================
    output_dir = './output/'
    
    model_name = os.path.basename(model_path).split('.')[0]
    file_results = os.path.join(output_dir,'results_' + model_name + '_.txt')
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    
    output_dir = os.path.join(output_dir, 'density_maps_' + model_name)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    #load test data
    data_loader = ImageDataLoader(data_path, shuffle=False, gt_downsample=True, pre_load=True)
    
    net = CrowdCounter()
          
    trained_model = os.path.join(model_path)
    network.load_net(trained_model, net)
    net.cuda()
    net.eval()
    mae = 0.0
    mse = 0.0
    i = 1
    #df = pd.read_csv("../etcount.csv")
    #df = df.set_index('IMG_NAME')
    #df['GROUND_TRUTH'] = 0.0
    #df['MTL-v4-A10'] = 0.0
    
    
    for blob in data_loader:    
        if gt_flag:
            gt_name = os.path.join(gt_path, 'GT_'+format(blob['fname'].split('.')[0]) + '.mat')
            x = loadmat(gt_name)
            #gt_count = len(x['image_info'][0][0][0][0][0])
            #df.at[blob['fname'].split('.')[0], 'GROUND_TRUTH'] = gt_count
            i+=1                
        im_data = blob['data']
        density_map = net(im_data)
        density_map = density_map.data.cpu().numpy()
        x = len(density_map[0][0])
        y = len(density_map[0][0][0])
        half = (int)(x/2);
        density_map1 = density_map[0][0][0:half][:]
        density_map2 = density_map[0][0][half:][:]
        
        print(x, y)
        et_c1 = np.sum(density_map1)
        et_c2 = np.sum(density_map2)
        side = 'none'
        if et_c1 > et_c2:
            side = 'right'
        else:
            side = 'left'
        print(et_c1, et_c2)
        et_count = np.sum(density_map)

        print (blob['fname'].split('.')[0],' Model Estimated count : ',et_count )
        #df.at[blob['fname'].split('.')[0], 'MTL-v4-A'] = et_count
        if vis:
            utils.display_results(im_data, density_map)
        if save_output:
            utils.save_density_map(density_map, output_dir, 'output_' + blob['fname'].split('.')[0] + '.png')
    
    return (et_count, side)      
            
    #df.to_csv('../etcount.csv')

#testimage('A', 1)