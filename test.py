import nsnitro
import nsresources
import json

nitro = nsnitro.NSNitro('localhost', 'api_user', 'api_user')
nitro.login()
service = nsresources.NSService()
#service.get(nitro, "aurora_userservice_mp-be002")
#print service.get_name()
service.disable(nitro, "aurora_userservice_mp-be002")
#service.get(nitro, "aurora_userservice_mp-be002")
#print service.get_svrstate()
