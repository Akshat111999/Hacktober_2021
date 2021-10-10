import  socket 
recv_ip="192.168.1.5" # write your local ip address
recv_port=4444  #    0 - 1024  -- you can check free udp port netstat -nulp

#  creating  udp socket
#               ip type v4    ,    uDp  
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 4 >  3  :  # here you can any condition which should always be true
    msg=input("plz  enter your message :   ")
#  converting  str  to bytes-like object 
    nmsg=msg.encode('ascii')
#  sending  data  to target  
    s.sendto(nmsg,(recv_ip,recv_port)) 
#  recv data  from  server
    print("\n")
    print(s.recvfrom(100))
s.close()
