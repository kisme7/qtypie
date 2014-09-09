qtypie v1.1 - SSH Botnet

Developed by Kismet						      

Disclamier: I do not take any responsibilty for what you do with this project	  


How to use?: 													    
																		    
1) Place udp.py, and http.py on your servers in your home directory 
	
	Example: /root or /home/username/ 
	
	Note: Whatever the ssh credentials are for that user

2) Go to qtypie.py and edit the configs at the bottom.  

3) Locate addClient('ip', 'username', 'password') 

4) Change it to meet your SSH server credentails
	
	Exmaple: addClient('127.0.0.1', 'temp', 'temp')
	
	Note: You can add more than 1 ;) 

5) If you added to scripts when asked to send the command use these formats as examples
	
	Example: python dos.py 127.0.0.1 65500 120
	
	Example: python http.py http://www.google.com

6) After you've finished you can run qtypie!
	
	Run: python qtypie.py
															   
XMPP: kismet@exploit.im          
Twitter: temsiK_                 
Github: http://github.com/kisme7
