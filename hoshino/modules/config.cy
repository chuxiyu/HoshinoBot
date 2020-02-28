from nonebot.default_config import *

SUPERUSERS = [1742309284]   
COMMAND_START = {''}    
HOST = '127.0.0.1'      
PORT = 8080             

IS_CQPRO = true

# 资源库文件夹  Nonebot访问本机资源
RESOURCE_DIR = 'C:\Users\dell\HoshinoBot-master/.hoshino/res/'

# 资源库 URL  用于docker中的酷Q读取宿主机资源，注意以'/'结尾
# 若留空则图片均采用base64发送，开销较大但部署方便
RESOURCE_URL = ''

# 启用的模块
MODULES_ON = {
    'botmanage',
    'groupmaster',
    'priconne',
    'kancolle',
    'subscribe',
    'setu',
    'translate',
}
