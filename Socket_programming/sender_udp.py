import  socket 
recv_ip="192.168.1.5" #write your local ip address
recv_port=4444  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4    ,    uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#  fitting    ip and port  with udp socket 
s.bind((recv_ip,recv_port))

#   recv  data  from  client  
while  4  >  2  :  # here you can any condition which should always be true
    data=s.recvfrom(100)  
    print("\nmessage  from sender  ",data[0])
    print("sender IP + port --socket  ",data[1])
#  reply to sender  
    rply=input("type your rply  : ")
    n_rply=rply.encode('ascii') #  converting  str  to bytes-like object
    s.sendto(n_rply,data[1])

s.close()
