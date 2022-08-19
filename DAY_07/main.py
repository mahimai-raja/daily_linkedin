import socket   
hostname=socket.gethostname()   
private=socket.gethostbyname(hostname)   
print(f'Your Computer Name is : {hostname}')   
print(f'Your Computer IP Address is : {private}')

public = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
public.connect(("8.8.8.8", 80))
print(public.getsockname()[0])
public.close()
