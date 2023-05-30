from Database_function.c_Data import *
a = Router()
# ghi ra file cau hinh 
#chon cau hinh file 
thiet_bi ="mx5"
ip_lo0="10.254.200.222"
file_name_read =thiet_bi+".conf"
content = open(file_name_read,"r+")
ab = content.read()
new_content = ab.replace("10.254.200.254",ip_lo0)
#write file
file_name_write = thiet_bi+"_01.conf"
configuration = open(file_name_write,"r+")
configuration.write(new_content)
# tien hanh cau hinh tren thiet bi
#a.configuration_router("10.254.200.5","nguyennd","pass",file_name_write)