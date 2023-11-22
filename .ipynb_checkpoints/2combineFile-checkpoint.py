import os
import xarray as xr

# 指定文件夹路径
folder_path = 'D:\2_gradulate\first_class\ese5023\nc'
output_folder = 'D:\2_gradulate\first_class\ese5023\ESE5023_Assignments_12332288'
nc_files = [f for f in os.listdir(folder_path) if f.endswith('.nc4')]
ds_list = [xr.open_dataset(os.path.join(folder_path, nc_file)) for nc_file in nc_files]
combined_ds = xr.concat(ds_list, dim="time")
# 保存合并后的数据集为nc文件
output_file = os.path.join(output_folder, f"GLDAS.nc")
combined_ds.to_netcdf(output_file)
